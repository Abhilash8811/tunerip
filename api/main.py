# FastAPI + yt-dlp converter API
from __future__ import annotations

import asyncio
import os
import re
import shutil
import time
import uuid
from pathlib import Path
from typing import Literal

import yt_dlp
try:
    import imageio_ffmpeg  # type: ignore
    FFMPEG_LOCATION = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:  # noqa: BLE001
    FFMPEG_LOCATION = shutil.which("ffmpeg")

from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, field_validator

# Add local bin to PATH for Deno
bin_path = os.path.join(os.path.dirname(__file__), "bin", "bin")
if os.path.exists(bin_path):
    os.environ["PATH"] = f"{bin_path}:{os.environ.get('PATH', '')}"

STORAGE_DIR = Path(os.environ.get("STORAGE_DIR", "/tmp/ytconvert"))
STORAGE_DIR.mkdir(parents=True, exist_ok=True)

FILE_TTL_SECONDS = int(os.environ.get("FILE_TTL_SECONDS", "1800"))
MAX_DURATION_SECONDS = int(os.environ.get("MAX_DURATION_SECONDS", "10800"))

PROXY = os.environ.get("YTDLP_PROXY") or None
COOKIES_FILE = os.environ.get("YTDLP_COOKIES_FILE") or None

if COOKIES_FILE and os.path.exists(COOKIES_FILE):
    try:
        import tempfile
        _tmp_cookies = os.path.join(tempfile.gettempdir(), "yt_cookies_writable.txt")
        shutil.copy(COOKIES_FILE, _tmp_cookies)
        COOKIES_FILE = _tmp_cookies
    except Exception as e:
        print(f"Warning: Failed to copy cookies file to writable location: {e}")

YOUTUBE_URL_RE = re.compile(
    r"^(?:(?:https?://)?(?:www\.|m\.|music\.)?"
    r"(?:youtube\.com/(?:watch\?v=|shorts/|embed/|v/|playlist\?list=)|youtu\.be/)"
    r"[\w\-?=&/.]+|ytsearch\d*:.+)$"
)

AUDIO_FORMATS = {"mp3", "m4a", "ogg", "wav", "opus"}
AUDIO_BITRATES = {"128", "192", "256", "320"}
VIDEO_HEIGHTS = {"360", "480", "720", "1080", "1440", "2160"}

app = FastAPI(title="ytconvert-api", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# In-memory job store
JOBS: dict[str, dict] = {}


class ConvertRequest(BaseModel):
    url: str
    format: Literal["mp3", "m4a", "ogg", "wav", "opus", "mp4"] = "mp3"
    quality: str = "320"

    @field_validator("url")
    @classmethod
    def check_url(cls, v: str) -> str:
        v = v.strip()
        if not YOUTUBE_URL_RE.match(v):
            raise ValueError("Invalid YouTube URL")
        return v

    @field_validator("quality")
    @classmethod
    def check_quality(cls, v: str) -> str:
        if v in AUDIO_BITRATES or v in VIDEO_HEIGHTS:
            return v
        raise ValueError("Invalid quality")


def _cleanup_old_files() -> None:
    now = time.time()
    for entry in STORAGE_DIR.iterdir():
        try:
            if entry.is_dir() and now - entry.stat().st_mtime > FILE_TTL_SECONDS:
                shutil.rmtree(entry, ignore_errors=True)
        except OSError:
            continue
    for jid in list(JOBS.keys()):
        if now - JOBS[jid].get("updated_at", now) > FILE_TTL_SECONDS:
            JOBS.pop(jid, None)


def _progress_hook(job_id: str):
    def hook(d: dict) -> None:
        job = JOBS.get(job_id)
        if not job:
            return
        status = d.get("status")
        job["updated_at"] = time.time()
        if status == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 0
            downloaded = d.get("downloaded_bytes") or 0
            pct = int((downloaded / total) * 90) if total else 10
            job["progress"] = min(90, max(job.get("progress", 0), pct))
            job["state"] = "downloading"
        elif status == "finished":
            job["progress"] = 95
            job["state"] = "processing"
    return hook


def _ydl_opts_audio(job_id: str, out_dir: Path, fmt: str, bitrate: str) -> dict:
    pp = [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": fmt,
        "preferredquality": bitrate if fmt == "mp3" else "0",
    }]
    opts = {
        "format": "bestaudio/best",
        "outtmpl": str(out_dir / "%(title).80s.%(ext)s"),
        "postprocessors": pp,
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "restrictfilenames": False,
        "progress_hooks": [_progress_hook(job_id)],
        "concurrent_fragment_downloads": 4,
        "extractor_args": {"youtube": {"client": ["android", "web"], "skip": ["dash", "hls"]}},
        "nocheckcertificate": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        },
        "geo_bypass": True,
    }
    if FFMPEG_LOCATION:
        opts["ffmpeg_location"] = FFMPEG_LOCATION
    if PROXY:
        opts["proxy"] = PROXY
    if COOKIES_FILE and os.path.exists(COOKIES_FILE):
        opts["cookiefile"] = COOKIES_FILE
    return opts


def _ydl_opts_video(job_id: str, out_dir: Path, height: str) -> dict:
    opts = {
        "format": f"bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best[height<={height}][ext=mp4]/best[height<={height}]",
        "merge_output_format": "mp4",
        "outtmpl": str(out_dir / "%(title).80s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "progress_hooks": [_progress_hook(job_id)],
        "concurrent_fragment_downloads": 4,
        "extractor_args": {"youtube": {"client": ["android", "web"], "skip": ["dash", "hls"]}},
        "nocheckcertificate": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        },
        "geo_bypass": True,
    }
    if FFMPEG_LOCATION:
        opts["ffmpeg_location"] = FFMPEG_LOCATION
    if PROXY:
        opts["proxy"] = PROXY
    if COOKIES_FILE and os.path.exists(COOKIES_FILE):
        opts["cookiefile"] = COOKIES_FILE
    return opts


def _run_conversion(job_id: str, url: str, fmt: str, quality: str) -> None:
    job = JOBS[job_id]
    out_dir = STORAGE_DIR / job_id
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        if fmt == "mp4":
            opts = _ydl_opts_video(job_id, out_dir, quality)
        else:
            opts = _ydl_opts_audio(job_id, out_dir, fmt, quality)

        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if "entries" in info:
                entries = list(info["entries"])
                if not entries:
                    raise RuntimeError("No search results found.")
                info = entries[0]

            duration = info.get("duration") or 0
            if duration and duration > MAX_DURATION_SECONDS:
                raise RuntimeError(
                    f"Video is too long ({duration}s). Max {MAX_DURATION_SECONDS}s."
                )
            
            job["title"] = info.get("title") or "video"
            job["thumbnail"] = info.get("thumbnail")
            job["duration"] = duration
            job["updated_at"] = time.time()

            # Use the actual video URL for the final download
            final_url = info.get("webpage_url") or info.get("url") or url
            ydl.download([final_url])

        files = sorted(out_dir.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
        if not files:
            raise RuntimeError("Conversion produced no file")
        final = files[0]
        job["file"] = str(final)
        job["filename"] = final.name
        job["size"] = final.stat().st_size
        job["progress"] = 100
        job["state"] = "done"
        job["updated_at"] = time.time()
    except Exception as e:  # noqa: BLE001
        msg = re.sub(r"\x1b\[[0-9;]*m", "", str(e))
        msg = re.sub(r"ERROR:\s*", "", msg)
        if "Sign in to confirm" in msg or "bot" in msg.lower():
            msg = (
                "YouTube rate-limited this server. Retry in a minute, or configure "
                "YTDLP_PROXY (residential proxy) / YTDLP_COOKIES_FILE on the backend "
                "to bypass bot detection."
            )
        job["state"] = "error"
        job["error"] = msg
        job["updated_at"] = time.time()


@app.get("/healthz")
def healthz() -> dict:
    return {"ok": True, "yt_dlp": yt_dlp.version.__version__}


@app.get("/api/debug")
def debug(q: str = "hello") -> JSONResponse:
    import subprocess
    ffmpeg_version = "Not found"
    deno_version = "Not found"
    if FFMPEG_LOCATION:
        try: ffmpeg_version = subprocess.check_output([FFMPEG_LOCATION, "-version"], stderr=subprocess.STDOUT).decode().split("\n")[0]
        except Exception as e: ffmpeg_version = f"Error: {e}"
    
    # Check if Deno is in PATH
    try: deno_version = subprocess.check_output(["deno", "--version"], stderr=subprocess.STDOUT).decode().split("\n")[0]
    except Exception as e: deno_version = f"Error: {e}"

    url = f"ytsearch1:{q}"
    opts = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "noplaylist": True,
        "extractor_args": {"youtube": {"client": ["tv_embedded"], "skip": ["dash", "hls"]}},
        "nocheckcertificate": True,
    }
    
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return JSONResponse({"status": "ok", "info_title": info.get("title"), "deno": deno_version})
    except Exception as e:
        return JSONResponse({"status": "error", "error": str(e), "deno": deno_version, "ffmpeg": ffmpeg_version})


@app.get("/api/info")
def info(url: str) -> JSONResponse:
    if not YOUTUBE_URL_RE.match(url):
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")
    opts = {
        "quiet": True, 
        "no_warnings": True, 
        "skip_download": True, 
        "noplaylist": True,
        # Revert to web client for metadata fetching as it's more reliable for search
        "extractor_args": {"youtube": {"client": ["web"]}},
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        },
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
    if PROXY:
        opts["proxy"] = PROXY
    if COOKIES_FILE and os.path.exists(COOKIES_FILE):
        opts["cookiefile"] = COOKIES_FILE
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            data = ydl.extract_info(url, download=False)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=str(e))
    return JSONResponse({
        "title": data.get("title"),
        "duration": data.get("duration"),
        "thumbnail": data.get("thumbnail"),
        "uploader": data.get("uploader"),
        "view_count": data.get("view_count"),
    })


@app.post("/api/convert")
def convert(req: ConvertRequest, background_tasks: BackgroundTasks) -> dict:
    _cleanup_old_files()
    fmt = req.format
    if fmt in AUDIO_FORMATS and req.quality not in AUDIO_BITRATES:
        raise HTTPException(status_code=400, detail="Bad bitrate for audio format")
    if fmt == "mp4" and req.quality not in VIDEO_HEIGHTS:
        raise HTTPException(status_code=400, detail="Bad height for video format")

    job_id = uuid.uuid4().hex[:16]
    JOBS[job_id] = {
        "id": job_id,
        "state": "queued",
        "progress": 0,
        "created_at": time.time(),
        "updated_at": time.time(),
        "format": fmt,
        "quality": req.quality,
        "url": req.url,
    }
    background_tasks.add_task(_run_conversion, job_id, req.url, fmt, req.quality)
    return {"job_id": job_id}


@app.get("/api/status/{job_id}")
def status(job_id: str) -> dict:
    job = JOBS.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Unknown job")
    return {
        "id": job["id"],
        "state": job.get("state"),
        "progress": job.get("progress", 0),
        "title": job.get("title"),
        "thumbnail": job.get("thumbnail"),
        "duration": job.get("duration"),
        "size": job.get("size"),
        "filename": job.get("filename"),
        "error": job.get("error"),
    }


@app.get("/api/download/{job_id}")
def download(job_id: str) -> FileResponse:
    job = JOBS.get(job_id)
    if not job or job.get("state") != "done":
        raise HTTPException(status_code=404, detail="File not ready")
    path = job.get("file")
    if not path or not os.path.exists(path):
        raise HTTPException(status_code=410, detail="File expired")
    return FileResponse(
        path,
        filename=os.path.basename(path),
        media_type="application/octet-stream",
    )


async def _periodic_cleanup() -> None:
    while True:
        try:
            _cleanup_old_files()
        except Exception:  # noqa: BLE001
            pass
        await asyncio.sleep(300)


@app.on_event("startup")
async def _startup() -> None:
    asyncio.create_task(_periodic_cleanup())

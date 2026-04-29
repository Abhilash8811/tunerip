# TuneRip — YouTube to MP3 & MP4 Converter

Fast, ad-free YouTube-to-MP3/MP4 converter. Static frontend + FastAPI backend powered by yt-dlp and FFmpeg.

## Structure

```
web/        Static frontend (HTML/CSS/JS). Deployable to any static host.
  index.html
  build.js          # Generates /pages/*.html SEO landing pages
  pages/            # Pre-rendered SEO landing pages (mp4, shorts, playlist, 320kbps, ...)
  assets/           # JS, CSS, favicon
  sitemap.xml
  robots.txt
api/        FastAPI backend that wraps yt-dlp.
  main.py
  pyproject.toml
  Dockerfile
```

## Local development

### Backend

```bash
cd api
pip install "fastapi>=0.115" "uvicorn[standard]>=0.30" "pydantic>=2.7" "yt-dlp>=2025.1.0"
# ffmpeg must be available on PATH
uvicorn main:app --reload --port 8000
```

Environment variables:

- `STORAGE_DIR` — where temp files live (default `/tmp/ytconvert`, `/data` in Docker).
- `FILE_TTL_SECONDS` — how long finished files stay on disk (default 1800).
- `MAX_DURATION_SECONDS` — max source video length (default 10800 = 3 hours).
- `YTDLP_PROXY` — optional outbound proxy URL (recommended for production; residential proxies avoid YouTube bot-detection).
- `YTDLP_COOKIES_FILE` — path to a Netscape-format cookies.txt for accessing age-restricted content.

### Frontend

```bash
cd web
node build.js             # Rebuild SEO landing pages
python3 -m http.server 3000
# Open http://localhost:3000/?api=http://localhost:8000
```

The frontend talks to the API base passed via `?api=<base>` query parameter, `window.__API_BASE__`, or same-origin `/api`.

## Deploy

### Backend (Fly.io)

Use the Devin deploy tool (or `fly launch` + `fly deploy`). The included Dockerfile installs ffmpeg and binds `/data` as a persistent volume.

### Frontend (any static host)

Upload the contents of `web/` to any static host (devinapps, Netlify, Vercel, Cloudflare Pages). Update `window.__API_BASE__` or the `?api=` parameter to point at your deployed backend, or add a CDN rewrite so `/api/*` proxies to the backend.

## Production notes

- YouTube aggressively rate-limits cloud-provider IPs. For reliable production traffic, configure `YTDLP_PROXY` to a residential/mobile proxy pool (e.g. Bright Data, Oxylabs, Smartproxy).
- Cookies from a logged-in YouTube account (exported via the `Get cookies.txt LOCALLY` extension) dramatically reduce bot-detection and unlock age-restricted content. Mount the file and set `YTDLP_COOKIES_FILE`.
- Set `FILE_TTL_SECONDS` higher if users tend to download slowly, but balance it against disk usage.
- Update the `https://example.com/` placeholder in `<link rel="canonical">`, OG tags, `sitemap.xml`, and `robots.txt` once you have a production domain.

## Responsible use

Intended for personal use with your own content, royalty-free material, public-domain works, or content you have rights to download. Respect copyright law and the YouTube Terms of Service in your jurisdiction.

FROM python:3.12-slim

# ffmpeg is required by yt-dlp post-processing
RUN apt-get update \
 && apt-get install -y --no-install-recommends ffmpeg curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    STORAGE_DIR=/data

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --upgrade pip \
 && pip install "fastapi>=0.115" "uvicorn[standard]>=0.30" "pydantic>=2.7" "yt-dlp>=2025.1.0" "python-multipart>=0.0.9"

COPY main.py ./

RUN mkdir -p /data
VOLUME ["/data"]

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -fsS http://127.0.0.1:8000/healthz || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]

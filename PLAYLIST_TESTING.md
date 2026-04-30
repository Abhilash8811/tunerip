# Testing Playlist Downloader Locally

## The Issue

The playlist downloader feature requires the `/api/playlist` endpoint, which exists in the code but is not yet deployed to the production API server at `https://api.yt2mp3.lol`.

## Solution: Run API Locally

### Prerequisites

1. Python 3.11 or higher
2. Install dependencies:
   ```bash
   cd api
   pip install -e .
   ```

### Running the API Server

**On Windows:**
```bash
run_api_local.bat
```

**On Linux/Mac:**
```bash
chmod +x run_api_local.sh
./run_api_local.sh
```

**Or manually:**
```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Using the Local API

Once the API is running on `http://localhost:8000`, open your website with the API parameter:

```
http://localhost:8080/youtube-playlist-downloader?api=http://localhost:8000
```

Or if using a live server:
```
http://127.0.0.1:5500/web/youtube-playlist-downloader?api=http://localhost:8000
```

The frontend will automatically use your local API instead of the production one.

## Deploying to Production

To make the playlist feature work on the live site, you need to:

1. Deploy the updated `api/main.py` to your production server
2. Restart the API service

### If using Render/Vercel/Railway:
- Push the changes to GitHub (already done ✅)
- The platform should auto-deploy the new version
- Wait for deployment to complete
- Restart the service if needed

### If using a VPS:
```bash
cd /path/to/tunerip
git pull origin main
cd api
pip install -e .
# Restart your API service (systemd, pm2, etc.)
```

## Testing

Once the API is running (locally or production), test with a playlist URL like:
```
https://www.youtube.com/playlist?list=PLwLSw1_eDZI3pfSGYuLYNhx-r4jK1qzTB
```

You should see the playlist UI with all videos listed.

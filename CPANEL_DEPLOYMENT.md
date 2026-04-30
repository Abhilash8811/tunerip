# Deploying to cPanel Server

## Quick Deployment Steps

### 1. Connect to Terminal
You're already in the cPanel terminal (as shown in your screenshot).

### 2. Navigate to Project Directory
```bash
cd ~/tunerip
```

### 3. Pull Latest Changes
```bash
git pull origin main
```

### 4. Run Deployment Script
```bash
cd api
chmod +x deploy_cpanel.sh
./deploy_cpanel.sh
```

## Manual Deployment (if script fails)

### Step 1: Update Code
```bash
cd ~/tunerip
git pull origin main
cd api
```

### Step 2: Activate Virtual Environment
```bash
# If venv doesn't exist, create it:
python3 -m venv venv

# Activate it:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install --upgrade pip
pip install fastapi uvicorn yt-dlp pydantic python-multipart imageio-ffmpeg
```

### Step 4: Stop Old Process
```bash
# Find the process
ps aux | grep uvicorn

# Kill it (replace XXXX with the actual PID)
kill XXXX

# Or kill all uvicorn processes:
pkill -f "uvicorn main:app"
```

### Step 5: Start New Process
```bash
# Start in background
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &

# Check if it's running
ps aux | grep uvicorn
```

### Step 6: Check Logs
```bash
tail -f api.log
```

Press `Ctrl+C` to stop viewing logs.

## Verify Deployment

Test the API endpoint:
```bash
curl http://localhost:8001/healthz
```

Should return: `{"ok":true,"yt_dlp":"..."}`

Test the playlist endpoint:
```bash
curl "http://localhost:8001/api/playlist?url=https://www.youtube.com/playlist?list=PLwLSw1_eDZI3pfSGYuLYNhx-r4jK1qzTB"
```

## Update Frontend to Use Your Server

If your API is running on port 8001, update the API_BASE in `web/assets/app.js`:

```javascript
var API_BASE = "http://YOUR_SERVER_IP:8001";
```

Or use the domain if you have one configured.

## Troubleshooting

### Port Already in Use
```bash
# Find what's using the port
lsof -i :8001

# Kill it
kill -9 PID
```

### Permission Denied
```bash
chmod +x deploy_cpanel.sh
```

### Python Not Found
```bash
# Try python3
which python3

# Or check available Python versions
ls /usr/bin/python*
```

### Check if API is Running
```bash
ps aux | grep uvicorn
netstat -tulpn | grep 8001
```

## Keeping API Running (Process Manager)

For production, consider using a process manager to keep the API running:

### Option 1: Using screen
```bash
screen -S tunerip-api
cd ~/tunerip/api
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4
# Press Ctrl+A then D to detach
# Reattach with: screen -r tunerip-api
```

### Option 2: Using nohup (already in script)
```bash
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &
```

### Option 3: Create a systemd service (if you have sudo)
Ask your hosting provider to set this up for you.

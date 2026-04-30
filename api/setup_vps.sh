#!/usr/bin/env bash
# TunerIP Master Setup Script for VPS/Shared Hosting
set -e

echo "Starting TunerIP Setup on your 8GB Server..."

# 1. Check for sudo and install dependencies if possible
if command -v sudo >/dev/null 2>&1; then
    echo "Sudo detected, installing system dependencies..."
    sudo apt-get update && sudo apt-get install -y python3-pip python3-venv ffmpeg curl git unzip || true
else
    echo "No sudo detected. Skipping system package installation. (Assuming FFmpeg is already installed by host)"
fi

# 2. Install Deno (JS runtime for yt-dlp)
echo "Installing Deno..."
mkdir -p bin
curl -fsSL https://deno.land/x/install/install.sh | DENO_INSTALL=./bin sh
export PATH="$PWD/bin/bin:$PATH"

# 3. Clone/Update the repository
if [ -d "tunerip" ]; then
    cd tunerip
    git pull origin main
else
    git clone https://github.com/Abhilash8811/tunerip.git
    cd tunerip
fi

# 4. Set up Python environment
echo "Setting up Python environment..."
cd api
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -e .

# 5. Create storage directory
mkdir -p /tmp/ytconvert

# 6. Start the API
echo "Starting TunerIP API..."
PORT=8000
# Kill any existing process on port 8000
fuser -k $PORT/tcp || true
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port $PORT --workers 4 > api.log 2>&1 &

echo "------------------------------------------------"
echo "Setup Complete!"
echo "Your API is now running on: http://122.176.149.109:8000"
echo "Check api.log for any errors."
echo "------------------------------------------------"

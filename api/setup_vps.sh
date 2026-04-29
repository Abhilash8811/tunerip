#!/usr/bin/env bash
# TunerIP Master Setup Script for VPS (8GB RAM Optimization)
set -e

echo "Starting TunerIP Setup on your 8GB Server..."

# 1. Update and install basic dependencies
sudo apt-get update && sudo apt-get install -y \
    python3-pip \
    python3-venv \
    ffmpeg \
    curl \
    git \
    unzip

# 2. Install Deno (JS runtime for yt-dlp)
echo "Installing Deno..."
curl -fsSL https://deno.land/x/install/install.sh | sh
export DENO_INSTALL="$HOME/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"

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

# 6. Start the API with 8GB RAM optimizations (Workers = 4)
echo "Starting TunerIP API..."
nohup uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 > api.log 2>&1 &

echo "------------------------------------------------"
echo "Setup Complete!"
echo "Your API is now running on: http://122.176.149.109:8000"
echo "Check api.log for any errors."
echo "------------------------------------------------"

#!/usr/bin/env bash
# Deploy updated API to cPanel server
set -e

echo "=== Deploying TunerIP API Updates ==="

# Navigate to the project directory
cd ~/tunerip || { echo "Error: tunerip directory not found"; exit 1; }

# Pull latest changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull origin main

# Navigate to API directory
cd api

# Activate virtual environment (create if doesn't exist)
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -e .

# Find and kill existing API process
echo "Stopping existing API process..."
pkill -f "uvicorn main:app" || echo "No existing process found"

# Wait a moment for the port to be released
sleep 2

# Start the API server
echo "Starting API server..."
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &

# Get the process ID
API_PID=$!
echo "API started with PID: $API_PID"

# Wait a moment and check if it's running
sleep 3
if ps -p $API_PID > /dev/null; then
    echo ""
    echo "=== Deployment Successful! ==="
    echo "API is running on port 8001"
    echo "Check logs: tail -f ~/tunerip/api/api.log"
    echo ""
else
    echo ""
    echo "=== Deployment Failed! ==="
    echo "Check logs: cat ~/tunerip/api/api.log"
    echo ""
    exit 1
fi

#!/usr/bin/env bash
# Stop the TunerIP API server

echo "Stopping TunerIP API..."

# Method 1: Kill by process name
pkill -9 -f "uvicorn main:app"

# Method 2: Kill by port
lsof -ti:8001 | xargs kill -9 2>/dev/null

# Method 3: Kill by port (alternative)
fuser -k 8001/tcp 2>/dev/null

echo "API stopped. Waiting for port to be released..."
sleep 2

# Check if anything is still running
if lsof -i:8001 >/dev/null 2>&1; then
    echo "WARNING: Port 8001 is still in use!"
    lsof -i:8001
else
    echo "Port 8001 is now free."
fi

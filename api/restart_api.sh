#!/usr/bin/env bash
# Quick restart of the API without pulling new code

echo "=== Restarting TunerIP API ==="

cd ~/tunerip/api || { echo "Error: api directory not found"; exit 1; }

# Stop existing process
echo "Stopping API..."
pkill -9 -f "uvicorn main:app" 2>/dev/null
lsof -ti:8001 | xargs kill -9 2>/dev/null
fuser -k 8001/tcp 2>/dev/null

sleep 3

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found. Run deploy_cpanel.sh first."
    exit 1
fi

source venv/bin/activate

# Start the API
echo "Starting API..."
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &

API_PID=$!
echo "API started with PID: $API_PID"

sleep 3

if ps -p $API_PID > /dev/null; then
    echo ""
    echo "=== Restart Successful! ==="
    echo "API is running on port 8001"
    echo ""
else
    echo ""
    echo "=== Restart Failed! ==="
    echo "Check logs: tail -f ~/tunerip/api/api.log"
    echo ""
    exit 1
fi

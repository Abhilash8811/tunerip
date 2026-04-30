#!/usr/bin/env bash
# Completely kill all API processes including workers and keep_alive

echo "=== Killing TunerIP API Completely ==="
echo ""

# Step 1: Kill the keep_alive script first (so it doesn't restart)
echo "1. Stopping keep_alive.sh script..."
pkill -9 -f "keep_alive.sh"
pkill -9 -f "bash.*keep_alive"
echo "   Done"

# Step 2: Kill all uvicorn processes
echo "2. Killing uvicorn processes..."
pkill -9 -f "uvicorn"
pkill -9 -f "uvicorn main:app"
echo "   Done"

# Step 3: Kill all Python multiprocessing workers
echo "3. Killing Python multiprocessing workers..."
pkill -9 -f "multiprocessing.spawn"
pkill -9 -f "multiprocessing.resource_tracker"
echo "   Done"

# Step 4: Kill any Python process in the tunerip/api directory
echo "4. Killing Python processes in tunerip/api..."
ps aux | grep "tunerip/api/venv/bin/python" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null
echo "   Done"

# Step 5: Kill by port if tools are available
echo "5. Killing processes on port 8001..."
if command -v fuser >/dev/null 2>&1; then
    fuser -k -9 8001/tcp 2>/dev/null
    echo "   Done (fuser)"
else
    echo "   Skipped (fuser not available)"
fi

if command -v lsof >/dev/null 2>&1; then
    lsof -ti:8001 | xargs kill -9 2>/dev/null
    echo "   Done (lsof)"
else
    echo "   Skipped (lsof not available)"
fi

echo ""
echo "Waiting 3 seconds for cleanup..."
sleep 3

# Verify everything is dead
echo ""
echo "=== Verification ==="
REMAINING=$(ps aux | grep -E "(uvicorn|multiprocessing|tunerip/api/venv)" | grep -v grep | wc -l)

if [ "$REMAINING" -eq 0 ]; then
    echo "✓ All API processes killed successfully!"
else
    echo "⚠ Warning: $REMAINING processes still running:"
    ps aux | grep -E "(uvicorn|multiprocessing|tunerip/api/venv)" | grep -v grep
fi

echo ""
echo "=== Done ==="

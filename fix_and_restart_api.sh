#!/usr/bin/env bash
# Complete fix: Stop keep_alive, kill old API, start new API

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         TunerIP API - Complete Fix & Restart              ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Remove keep_alive from crontab
echo "1. Disabling keep_alive.sh from crontab..."
crontab -l 2>/dev/null | grep -v "keep_alive.sh" | crontab -
echo "   ✓ Crontab updated (keep_alive removed)"

# Step 2: Kill keep_alive script
echo "2. Killing keep_alive.sh processes..."
pkill -9 -f "keep_alive.sh"
pkill -9 -f "bash.*keep_alive"
echo "   ✓ Done"

# Step 3: Kill all API processes
echo "3. Killing all API processes..."
pkill -9 -f "uvicorn"
pkill -9 -f "multiprocessing.spawn"
pkill -9 -f "multiprocessing.resource_tracker"
ps aux | grep "tunerip/api/venv/bin/python" | grep -v grep | awk '{print $2}' | xargs kill -9 2>/dev/null
echo "   ✓ Done"

# Step 4: Kill processes on both ports (8000 and 8001)
echo "4. Freeing ports 8000 and 8001..."
fuser -k -9 8000/tcp 2>/dev/null
fuser -k -9 8001/tcp 2>/dev/null
echo "   ✓ Done"

echo ""
echo "Waiting 5 seconds for cleanup..."
sleep 5

# Step 5: Pull latest code
echo ""
echo "5. Updating code from GitHub..."
cd ~/tunerip
git fetch origin main
git reset --hard origin/main
echo "   ✓ Code updated"

# Step 6: Setup environment
echo "6. Setting up Python environment..."
cd ~/tunerip/api
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip --quiet
pip install -e . --quiet
echo "   ✓ Environment ready"

# Step 7: Start API on port 8001
echo "7. Starting API on port 8001..."
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 > api.log 2>&1 &
API_PID=$!
echo "   ✓ API started with PID: $API_PID"

sleep 5

# Step 8: Verify
echo ""
echo "8. Verifying API is running..."
if ps -p $API_PID > /dev/null 2>&1; then
    echo "   ✓ API is running!"
    
    # Test health endpoint
    if command -v curl >/dev/null 2>&1; then
        HEALTH=$(curl -s http://localhost:8001/healthz 2>/dev/null || echo "failed")
        if [[ $HEALTH == *"ok"* ]]; then
            echo "   ✓ Health check passed!"
        else
            echo "   ⚠ Health check failed (but process is running)"
        fi
    fi
    
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                  ✅ SUCCESS!                               ║"
    echo "╠════════════════════════════════════════════════════════════╣"
    echo "║  API is now running on port 8001                           ║"
    echo "║  Process ID: $API_PID                                      ║"
    echo "║  Log file: ~/tunerip/api/api.log                           ║"
    echo "║                                                            ║"
    echo "║  IMPORTANT: Update your frontend API_BASE to:             ║"
    echo "║  http://YOUR_DOMAIN:8001                                   ║"
    echo "║  (or use localhost.run tunnel on port 8001)               ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""
    
    # Show recent logs
    echo "Recent logs:"
    echo "─────────────────────────────────────────────────────────────"
    tail -n 10 api.log
    echo "─────────────────────────────────────────────────────────────"
    
else
    echo "   ✗ API failed to start!"
    echo ""
    echo "Error logs:"
    tail -n 30 api.log
    exit 1
fi

echo ""
echo "To add keep_alive back (optional), run:"
echo "  (crontab -l 2>/dev/null; echo '* * * * * /bin/bash ~/tunerip/api/keep_alive.sh') | crontab -"

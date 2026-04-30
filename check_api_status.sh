#!/usr/bin/env bash
# Check API status and what's using the port

echo "=== TunerIP API Status Check ==="
echo ""

PORT=8001

echo "1. Checking processes using port $PORT:"
echo "----------------------------------------"
if command -v lsof >/dev/null 2>&1; then
    lsof -i :$PORT || echo "No processes found (lsof)"
else
    echo "lsof not available"
fi
echo ""

echo "2. Checking with netstat:"
echo "----------------------------------------"
if command -v netstat >/dev/null 2>&1; then
    netstat -tulpn 2>/dev/null | grep $PORT || echo "No processes found (netstat)"
else
    echo "netstat not available"
fi
echo ""

echo "3. All uvicorn processes:"
echo "----------------------------------------"
ps aux | grep uvicorn | grep -v grep || echo "No uvicorn processes found"
echo ""

echo "4. All Python processes with 'main':"
echo "----------------------------------------"
ps aux | grep -E "python.*main" | grep -v grep || echo "No matching Python processes"
echo ""

echo "5. Recent API logs (if exists):"
echo "----------------------------------------"
if [ -f "$HOME/tunerip/api/api.log" ]; then
    tail -n 20 "$HOME/tunerip/api/api.log"
else
    echo "Log file not found"
fi
echo ""

echo "=== To kill all processes on port $PORT, run: ==="
echo "lsof -ti:$PORT | xargs kill -9"
echo "pkill -9 -f uvicorn"
echo "fuser -k -9 $PORT/tcp"

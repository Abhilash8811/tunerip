#!/usr/bin/env bash
# TunerIP Bulletproof Keep-Alive
# This script ensures the API and Tunnel are always running.
# Add to crontab: * * * * * /bin/bash /home/pornwoo1/keep_alive.sh

export PATH="/usr/local/bin:/usr/bin:/bin:/home/pornwoo1/bin:$PATH"

# 1. Restart API if dead
if ! pgrep -f "uvicorn main:app" > /dev/null; then
    echo "$(date): API was dead, restarting..." >> /home/pornwoo1/tunerip/api/api.log
    cd /home/pornwoo1/tunerip/api
    nohup /home/pornwoo1/tunerip/api/venv/bin/python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 >> /home/pornwoo1/tunerip/api/api.log 2>&1 &
fi

# 2. Restart Tunnel if dead
if ! pgrep -f "nokey@localhost.run" > /dev/null; then
    echo "$(date): Tunnel was dead, restarting..." >> /home/pornwoo1/tunnel.log
    nohup ssh -o StrictHostKeyChecking=no -o ExitOnForwardFailure=yes -o ServerAliveInterval=60 -R 80:localhost:8000 nokey@localhost.run >> /home/pornwoo1/tunnel.log 2>&1 &
fi

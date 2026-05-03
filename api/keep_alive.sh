#!/usr/bin/env bash
# TunerIP Bulletproof Keep-Alive
# This script ensures the API is always running on cPanel shared hosting.
# Add to crontab: * * * * * /bin/bash $HOME/tunerip/api/keep_alive.sh

export PATH="/usr/local/bin:/usr/bin:/bin:$HOME/bin:$PATH"

API_DIR="$HOME/tunerip/api"
LOG_FILE="$API_DIR/api.log"
VENV_PYTHON="$API_DIR/venv/bin/python3"

# Check if API is running
if ! pgrep -f "uvicorn main:app" > /dev/null; then
    echo "$(date): API was dead, restarting..." >> "$LOG_FILE"
    cd "$API_DIR"
    
    # Make sure virtual environment exists
    if [ ! -f "$VENV_PYTHON" ]; then
        echo "$(date): Virtual environment not found, creating..." >> "$LOG_FILE"
        python3 -m venv venv
        source venv/bin/activate
        pip install --upgrade pip --quiet
        pip install -e . --quiet
    fi
    
    # Start the API
    nohup "$VENV_PYTHON" -m uvicorn main:app --host 0.0.0.0 --port 8001 --workers 4 >> "$LOG_FILE" 2>&1 &
    echo "$(date): API restarted with PID $!" >> "$LOG_FILE"
fi

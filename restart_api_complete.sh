#!/usr/bin/env bash
# Complete API Restart Script - Handles everything in one go
# Usage: ./restart_api_complete.sh

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         TunerIP API - Complete Restart Script             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="$HOME/tunerip"
API_DIR="$PROJECT_DIR/api"
API_PORT=8001
WORKERS=4

# Function to print colored messages
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Step 1: Navigate to project directory
print_status "Navigating to project directory..."
if [ ! -d "$PROJECT_DIR" ]; then
    print_error "Project directory not found: $PROJECT_DIR"
    print_status "Cloning repository..."
    cd "$HOME"
    git clone https://github.com/Abhilash8811/tunerip.git
    cd "$PROJECT_DIR"
else
    cd "$PROJECT_DIR"
    print_success "Found project directory"
fi

# Step 2: Pull latest changes from GitHub
print_status "Pulling latest changes from GitHub..."
git fetch origin main
git reset --hard origin/main
print_success "Code updated to latest version"

# Step 3: Stop existing API processes
print_status "Stopping existing API processes..."

# Method 1: Kill by process name
pkill -9 -f "uvicorn main:app" 2>/dev/null && print_success "Killed uvicorn processes" || print_warning "No uvicorn processes found"

# Method 2: Kill by port using lsof
if command -v lsof >/dev/null 2>&1; then
    lsof -ti:$API_PORT | xargs kill -9 2>/dev/null && print_success "Killed processes on port $API_PORT (lsof)" || print_warning "No processes on port $API_PORT (lsof)"
fi

# Method 3: Kill by port using fuser
if command -v fuser >/dev/null 2>&1; then
    fuser -k $API_PORT/tcp 2>/dev/null && print_success "Killed processes on port $API_PORT (fuser)" || print_warning "No processes on port $API_PORT (fuser)"
fi

# Method 4: Kill by port using netstat (fallback)
if command -v netstat >/dev/null 2>&1; then
    PID=$(netstat -tulpn 2>/dev/null | grep ":$API_PORT " | awk '{print $7}' | cut -d'/' -f1)
    if [ ! -z "$PID" ]; then
        kill -9 $PID 2>/dev/null && print_success "Killed process $PID on port $API_PORT (netstat)"
    fi
fi

print_status "Waiting for port to be released..."
sleep 3

# Verify port is free
if lsof -i:$API_PORT >/dev/null 2>&1; then
    print_error "Port $API_PORT is still in use!"
    lsof -i:$API_PORT
    print_error "Please manually kill the process and try again"
    exit 1
else
    print_success "Port $API_PORT is now free"
fi

# Step 4: Setup Python environment
print_status "Setting up Python environment..."
cd "$API_DIR"

if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_success "Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate
print_success "Virtual environment activated"

# Step 5: Install/Update dependencies
print_status "Installing/updating dependencies..."
pip install --upgrade pip --quiet
pip install -e . --quiet
print_success "Dependencies installed"

# Step 6: Create storage directory
print_status "Creating storage directory..."
mkdir -p /tmp/ytconvert
print_success "Storage directory ready"

# Step 7: Start the API server
print_status "Starting API server on port $API_PORT with $WORKERS workers..."
nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port $API_PORT --workers $WORKERS > api.log 2>&1 &
API_PID=$!

print_status "API started with PID: $API_PID"
print_status "Waiting for API to initialize..."
sleep 5

# Step 8: Verify API is running
if ps -p $API_PID > /dev/null 2>&1; then
    print_success "API process is running!"
    
    # Test the health endpoint
    print_status "Testing API health endpoint..."
    if command -v curl >/dev/null 2>&1; then
        HEALTH_CHECK=$(curl -s http://localhost:$API_PORT/healthz 2>/dev/null || echo "failed")
        if [[ $HEALTH_CHECK == *"ok"* ]]; then
            print_success "API health check passed!"
        else
            print_warning "API is running but health check failed"
            print_warning "Response: $HEALTH_CHECK"
        fi
    else
        print_warning "curl not available, skipping health check"
    fi
    
    echo ""
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║                  🎉 DEPLOYMENT SUCCESSFUL! 🎉              ║"
    echo "╠════════════════════════════════════════════════════════════╣"
    echo "║  API Status:    Running                                    ║"
    echo "║  Process ID:    $API_PID                                      ║"
    echo "║  Port:          $API_PORT                                      ║"
    echo "║  Workers:       $WORKERS                                        ║"
    echo "║  Log File:      $API_DIR/api.log                ║"
    echo "╠════════════════════════════════════════════════════════════╣"
    echo "║  Useful Commands:                                          ║"
    echo "║  • View logs:        tail -f $API_DIR/api.log  ║"
    echo "║  • Check status:     ps aux | grep uvicorn                 ║"
    echo "║  • Stop API:         pkill -9 -f uvicorn                   ║"
    echo "║  • Restart:          ./restart_api_complete.sh             ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo ""
    
else
    print_error "API failed to start!"
    print_error "Check the logs for details:"
    echo ""
    tail -n 50 api.log
    echo ""
    exit 1
fi

# Step 9: Show recent logs
print_status "Recent API logs:"
echo "─────────────────────────────────────────────────────────────"
tail -n 20 api.log
echo "─────────────────────────────────────────────────────────────"
echo ""
print_success "All done! Your API is ready to use."

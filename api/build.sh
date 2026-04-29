#!/usr/bin/env bash
set -e

# Install Python dependencies
pip install --upgrade pip
pip install -e .

# Install Deno (JS runtime for yt-dlp)
echo "Installing Deno..."
mkdir -p bin
curl -fsSL https://deno.land/x/install/install.sh | DENO_INSTALL=./bin sh
export PATH="$PWD/bin/bin:$PATH"

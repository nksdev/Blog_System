#!/bin/bash

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$SCRIPT_DIR/blog"
CMS_DIR="$SCRIPT_DIR/cms"

echo "🚀 Starting Blog System"

# Kill old instances
pkill -f "python3 -m http.server 8000" 2>/dev/null || true

# Start local server
cd "$BLOG_DIR"
python3 -m http.server 8000 > /dev/null 2>&1 &
SERVER_PID=$!
echo "✅ Local server running at http://localhost:8000 (PID: $SERVER_PID)"

# Start CMS
echo "✅ Launching CMS Dashboard..."
cd "$CMS_DIR"
python3 blog_cms.py

# Cleanup when CMS closes
kill $SERVER_PID
echo "👋 System stopped."
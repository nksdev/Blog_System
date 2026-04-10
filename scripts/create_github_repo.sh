#!/bin/bash
set -e
echo "🚀 Initializing GitHub Repository for nksdev"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$(dirname "$SCRIPT_DIR")/blog"

cd "$BLOG_DIR"

# Ensure Git User Config
git config user.name "Naman"
git config user.email "naman@example.com"

# Initialize Local Repo
if [ ! -d ".git" ]; then
    git init
    git checkout -b main
fi

# Initial Local State
git add .
git commit -m "Initialize Blog Structure" || echo "Already committed"

# GitHub Creation
read -p "Repository Name [nksdevblog]: " REPO_NAME
REPO_NAME=${REPO_NAME:-nksdevblog}

if gh repo create "$REPO_NAME" --public --description "Tech Blog" --source=. --remote=origin; then
    # Smart Push
    git branch -M main
    git push -u origin main
    echo "✅ Blog Live: https://github.com/nksdev/$REPO_NAME"
else
    echo "❌ Error: Repo exists or GitHub CLI not logged in (run 'gh auth login')."
fi
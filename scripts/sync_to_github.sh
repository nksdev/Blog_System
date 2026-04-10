#!/bin/bash

# Script to sync blog changes to GitHub

set -e

echo "🔄 Syncing Blog to GitHub"
echo "========================="

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$(dirname "$SCRIPT_DIR")/blog"
COMMIT_MESSAGE="Update blog content - $(date +'%Y-%m-%d %H:%M:%S')"

# Check if blog directory exists
if [ ! -d "$BLOG_DIR" ]; then
    echo -e "${RED}Error: Blog directory not found at $BLOG_DIR${NC}"
    exit 1
fi

echo -e "${BLUE}Working directory: $BLOG_DIR${NC}"
echo ""

# Check if git is initialized
if [ ! -d "$BLOG_DIR/.git" ]; then
    echo -e "${YELLOW}Git repository not initialized. Initializing...${NC}"
    cd "$BLOG_DIR"
    git init
    echo -e "${GREEN}✓ Git repository initialized${NC}"
else
    cd "$BLOG_DIR"
fi

# Check if remote is configured
if ! git remote get-url origin &> /dev/null; then
    echo -e "${RED}Error: No Git remote configured${NC}"
    echo "Please add remote with: git remote add origin <repository-url>"
    exit 1
fi

# Check for changes
if git diff --quiet && git diff --cached --quiet; then
    echo -e "${YELLOW}No changes to commit${NC}"
    echo "Blog is already up to date!"
    exit 0
fi

# Show changes
echo -e "${BLUE}Changes to be committed:${NC}"
git status --short
echo ""

# Ask for confirmation
read -p "Do you want to commit and push these changes? (y/n): " confirm
if [ "$confirm" != "y" ]; then
    echo "Operation cancelled."
    exit 0
fi

# Add all changes
echo -e "${BLUE}Adding changes...${NC}"
git add .

# Commit changes
echo -e "${BLUE}Committing changes...${NC}"
git commit -m "$COMMIT_MESSAGE"

echo -e "${GREEN}✓ Changes committed${NC}"

# Push to GitHub
echo -e "${BLUE}Pushing to GitHub...${NC}"
git push origin main

echo -e "${GREEN}✓ Successfully pushed to GitHub!${NC}"
echo ""
echo -e "${GREEN}Your blog has been updated!${NC}"
echo "GitHub Pages will update automatically within a few minutes."
echo ""
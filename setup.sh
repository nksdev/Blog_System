#!/bin/bash

# Complete Blog Setup Automation Script
# This script automates the entire process of setting up a blog with GitHub integration

set -e

echo "🚀 Complete Blog Setup Automation"
echo "=================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLOG_DIR="$SCRIPT_DIR/blog"
CMS_DIR="$SCRIPT_DIR/cms"
SCRIPTS_DIR="$SCRIPT_DIR/scripts"

# Check required tools
echo -e "${BLUE}Checking required tools...${NC}"

# Check Python 3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python 3 found${NC}"

# Check Git
if ! command -v git &> /dev/null; then
    echo -e "${RED}Error: Git is not installed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Git found${NC}"

# Check if GitHub CLI is available
if command -v gh &> /dev/null; then
    echo -e "${GREEN}✓ GitHub CLI found${NC}"
    GH_AVAILABLE=true
else
    echo -e "${YELLOW}⚠ GitHub CLI not found (optional for repo creation)${NC}"
    GH_AVAILABLE=false
fi

echo ""

# Create necessary directories
echo -e "${BLUE}Creating directory structure...${NC}"
mkdir -p "$BLOG_DIR/images"
mkdir -p "$CMS_DIR"
mkdir -p "$SCRIPTS_DIR"
echo -e "${GREEN}✓ Directories created${NC}"

# Check if blog files exist
if [ ! -f "$BLOG_DIR/index.html" ]; then
    echo -e "${RED}Error: index.html not found in blog directory${NC}"
    exit 1
fi

if [ ! -f "$BLOG_DIR/posts.json" ]; then
    echo -e "${RED}Error: posts.json not found in blog directory${NC}"
    exit 1
fi

if [ ! -f "$CMS_DIR/blog_cms.py" ]; then
    echo -e "${RED}Error: CMS script not found${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Blog files found${NC}"

# Make scripts executable
echo -e "${BLUE}Making scripts executable...${NC}"
chmod +x "$SCRIPTS_DIR/create_github_repo.sh" 2>/dev/null || true
chmod +x "$SCRIPTS_DIR/sync_to_github.sh" 2>/dev/null || true
chmod +x "$SCRIPT_DIR/setup.sh" 2>/dev/null || true
echo -e "${GREEN}✓ Scripts made executable${NC}"

echo ""

# GitHub Repository Setup
if [ "$GH_AVAILABLE" = true ]; then
    read -p "Do you want to create a new GitHub repository? (y/n): " create_repo
    
    if [ "$create_repo" = "y" ]; then
        echo -e "${BLUE}Launching GitHub repository creation...${NC}"
        bash "$SCRIPTS_DIR/create_github_repo.sh"
        echo ""
    fi
fi

# Initialize Git repository if not already initialized
if [ ! -d "$BLOG_DIR/.git" ]; then
    echo -e "${BLUE}Initializing Git repository...${NC}"
    cd "$BLOG_DIR"
    git init
    git add .
    git commit -m "Initial commit - Blog setup"
    echo -e "${GREEN}✓ Git repository initialized${NC}"
    cd "$SCRIPT_DIR"
fi

echo ""
echo -e "${GREEN}✓ Setup completed successfully!${NC}"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Start the CMS Dashboard:"
echo -e "   ${YELLOW}cd $CMS_DIR && python3 blog_cms.py${NC}"
echo ""
echo "2. In the CMS:"
echo "   - Enter your GitHub repository name"
echo "   - Create and manage your blog posts"
echo "   - Click 'Sync to GitHub' to publish"
echo ""
echo "3. Manual Sync (if needed):"
echo -e "   ${YELLOW}bash $SCRIPTS_DIR/sync_to_github.sh${NC}"
echo ""
echo -e "${BLUE}Blog Structure:${NC}"
echo "  📁 $BLOG_DIR/       - Your blog website"
echo "  📁 $CMS_DIR/        - CMS Dashboard"
echo "  📁 $SCRIPTS_DIR/    - Automation scripts"
echo ""

# Ask to start CMS
read -p "Do you want to start the CMS Dashboard now? (y/n): " start_cms

if [ "$start_cms" = "y" ]; then
    echo ""
    echo -e "${BLUE}Starting CMS Dashboard...${NC}"
    cd "$CMS_DIR"
    python3 blog_cms.py
else
    echo ""
    echo -e "${BLUE}To start the CMS later, run:${NC}"
    echo -e "${YELLOW}cd $CMS_DIR && python3 blog_cms.py${NC}"
fi

echo ""
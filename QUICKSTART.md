# 🚀 Quick Start Guide

Get your blog up and running in 5 minutes!

## Prerequisites Check

```bash
# Verify Python 3 is installed
python3 --version

# Verify Git is installed
git --version

# Verify tkinter
python3 -c "import tkinter; print('✓ tkinter available')"
```

## Setup (One-Time)

```bash
# Run the automated setup
./setup.sh
```

The setup will:
- ✅ Check all requirements
- ✅ Create directories
- ✅ Initialize Git
- ✅ Optionally create GitHub repo

## Start Your Blog

```bash
# Start everything
./start.sh
```

This opens:
- CMS Dashboard (for managing posts)
- Local server (at http://localhost:8000)

## Create Your First Post

1. **In the CMS Dashboard:**
   - Click "+ New Post"
   - Enter title, category, and content
   - Add images if desired
   - Click "💾 Save Post"

2. **Preview your post:**
   - Click "👁️ Preview"
   - Opens in browser

## Publish to GitHub

### Step 1: Create GitHub Repository

**Option A - Automated:**
```bash
./scripts/create_github_repo.sh
```

**Option B - Manual:**
1. Go to github.com → New repository
2. Name it (e.g., "my-blog")
3. Make it public
4. Don't initialize with README
5. Create

### Step 2: Connect and Push

1. In CMS, enter repository name
2. Click "Connect"
3. Write your posts
4. Click "🚀 Sync to GitHub"

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Settings → Pages
3. Select "main" branch
4. Save
5. Your site is live!

## Your Blog URLs

- **Local:** http://localhost:8000
- **Live:** https://yourusername.github.io/your-repo/

## Common Commands

```bash
# Start the system
./start.sh

# Sync to GitHub
./scripts/sync_to_github.sh

# Start CMS only
cd cms && python3 blog_cms.py

# Start local server only
cd blog && python3 -m http.server 8000
```

## Writing Posts

### Basic HTML Format
```html
<h2>Main Heading</h2>
<p>Your paragraph text here.</p>

<strong>Bold text</strong>
<em>Italic text</em>

<ul>
  <li>List item 1</li>
  <li>List item 2</li>
</ul>

<a href="https://example.com">Link text</a>
```

### Adding Images
1. Click "Browse" in CMS
2. Select image file
3. It's automatically copied and linked

### Toolbar Quick Tags
- **Bold** - Insert bold text
- **Italic** - Insert italic text
- **Heading** - Insert heading
- **Link** - Insert link
- **Image** - Insert image tag
- **List** - Insert list

## Troubleshooting Quick Fixes

### CMS won't start
```bash
# Install tkinter
sudo apt-get install python3-tk  # Linux
brew install python-tk           # macOS
```

### Git authentication error
```bash
# Use SSH instead of HTTPS
cd blog
git remote set-url origin git@github.com:username/repo.git
```

### Port 8000 already in use
```bash
# Kill existing server
pkill -f "python3 -m http.server"

# Or use different port
cd blog && python3 -m http.server 8080
```

## Next Steps

1. ✅ Create your first post
2. ✅ Publish to GitHub
3. ✅ Enable GitHub Pages
4. ✅ Customize your blog design
5. ✅ Write more content!

## Need Help?

- 📖 Read [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) for detailed instructions
- 📖 Read [README.md](README.md) for complete documentation
- 🔧 Check troubleshooting sections in guides

---

**You're all set! Start blogging! 🎉**
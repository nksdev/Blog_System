# Complete Installation & Usage Guide

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Quick Start](#quick-start)
4. [Detailed Usage](#detailed-usage)
5. [Troubleshooting](#troubleshooting)

## 💻 System Requirements

### Required Software
- **Python 3.8 or higher**
- **Git** (any recent version)
- **Tkinter** (usually included with Python)

### Optional Software
- **GitHub CLI** (gh) - for automated repository creation
- **SSH keys** - for secure Git operations

### Operating Systems
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)
- ✅ macOS
- ✅ Windows (with WSL or Git Bash)

## 📥 Installation Steps

### Step 1: Verify Prerequisites

Open your terminal/command prompt and check:

```bash
# Check Python version
python3 --version

# Check Git installation
git --version

# Check tkinter
python3 -c "import tkinter; print('tkinter available')"
```

### Step 2: Install Missing Dependencies

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk git
```

#### macOS
```bash
# Install Python with Homebrew
brew install python3

# Install Git
brew install git
```

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Download Git from [git-scm.com](https://git-scm.com/download/win)
4. Use Git Bash for terminal commands

### Step 3: Install GitHub CLI (Optional but Recommended)

```bash
# Ubuntu/Debian
sudo apt-get install gh

# macOS
brew install gh

# Windows
winget install --id GitHub.cli

# Authenticate
gh auth login
```

### Step 4: Download/Clone the Blog System

If you have the files:
```bash
# Navigate to your project directory
cd ~/projects

# Extract or copy files here
```

If cloning from a repository:
```bash
git clone <repository-url>
cd <repository-name>
```

### Step 5: Run Setup Script

```bash
# Make setup script executable (Linux/macOS)
chmod +x setup.sh

# Run setup
./setup.sh
```

The setup script will:
- ✅ Check all required tools
- ✅ Create necessary directories
- ✅ Make all scripts executable
- ✅ Initialize Git repository
- ✅ Optionally create GitHub repository
- ✅ Launch CMS Dashboard

## 🚀 Quick Start

### Option 1: Automated Start

```bash
# Run the start script
./start.sh
```

This will:
1. Start a local web server (port 8000)
2. Launch the CMS Dashboard
3. Open your blog at http://localhost:8000

### Option 2: Manual Start

```bash
# Start local server (in one terminal)
cd blog
python3 -m http.server 8000

# Start CMS (in another terminal)
cd cms
python3 blog_cms.py
```

## 📝 Detailed Usage

### Creating Your First Post

1. **Launch the CMS Dashboard**
   ```bash
   cd cms
   python3 blog_cms.py
   ```

2. **Connect to GitHub**
   - Enter your GitHub username in the top right field
   - Enter your repository name (e.g., "my-blog")
   - Click "Connect"

3. **Create a New Post**
   - Click the "+ New Post" button (top left)
   - Fill in the post details:
     - **Title**: Your post title
     - **Excerpt**: A brief summary (appears on card)
     - **Category**: Post category (e.g., "Technology", "Tutorial")
     - **Featured Image**: Click "Browse" to select an image
     - **Content**: Write your post content (supports HTML)

4. **Format Your Content**
   - Use the toolbar buttons for quick HTML tags
   - Or write HTML directly in the content area
   - Example HTML:
     ```html
     <p>This is a paragraph.</p>
     <h2>This is a heading</h2>
     <strong>Bold text</strong>
     <em>Italic text</em>
     <ul>
       <li>List item 1</li>
       <li>List item 2</li>
     </ul>
     ```

5. **Save Your Post**
   - Click the "💾 Save Post" button
   - The post is saved to posts.json
   - It appears in the posts list on the left

6. **Preview Your Post**
   - Click "👁️ Preview" to view in browser
   - Opens index.html with your new post

### Setting Up GitHub Repository

#### Option A: Automated Setup (Recommended)

1. Make sure GitHub CLI is installed
2. Run the setup script and choose to create repo
3. Or run directly:
   ```bash
   ./scripts/create_github_repo.sh
   ```

#### Option B: Manual Setup

1. **Create Repository on GitHub**
   - Go to github.com and sign in
   - Click "+" → "New repository"
   - Enter repository name (e.g., "my-blog")
   - Add description
   - Make it **Public** (for GitHub Pages)
   - **Don't** initialize with README
   - Click "Create repository"

2. **Connect Local Repo to GitHub**
   ```bash
   cd blog
   git remote add origin https://github.com/username/repo-name.git
   git branch -M main
   git push -u origin main
   ```

### Publishing Your Blog

#### From CMS Dashboard

1. Make sure you're connected to GitHub
2. Click "🚀 Sync to GitHub" button
3. Wait for the success message
4. Your changes are now on GitHub!

#### Using Sync Script

```bash
./scripts/sync_to_github.sh
```

#### Manual Git Commands

```bash
cd blog
git add .
git commit -m "Update blog content"
git push origin main
```

### Enabling GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Click "Pages" in left sidebar
4. Under "Source":
   - Select "main" branch
   - Keep folder as "/ (root)"
5. Click "Save"
6. Wait 1-3 minutes
7. Your site is live at: `https://username.github.io/repo-name/`

### Managing Images

1. **Adding Images to Posts**
   - In CMS, click "Browse" button next to "Featured Image"
   - Select image from your computer
   - Image is automatically copied to `blog/images/`
   - Path is automatically set (e.g., `images/photo.jpg`)

2. **Adding Inline Images in Content**
   - Use the image toolbar button
   - Or write HTML: `<img src="images/filename.jpg" alt="description">`
   - First upload images via Browse button
   - Then reference them in your content

3. **Supported Image Formats**
   - JPG/JPEG
   - PNG
   - GIF
   - WebP

### Using the Search Feature

The blog has a built-in search that:
- Searches in real-time as you type
- Looks through post titles
- Searches in post excerpts
- Searches in post content
- Instantly filters the post list

### Customizing Your Blog

#### Changing Colors and Styling

Edit `blog/index.html`:

1. Find the `<style>` section
2. Modify CSS variables and styles
3. Update Tailwind classes in HTML
4. Save and sync to GitHub

#### Changing Social Links

Edit `blog/index.html` footer section:

```html
<!-- Find these lines and update URLs -->
<a href="https://www.instagram.com/yourusername" target="_blank">...</a>
<a href="https://www.linkedin.com/in/yourusername" target="_blank">...</a>
<a href="https://www.github.com/yourusername" target="_blank">...</a>
```

#### Adding Custom Pages

1. Create new HTML file in `blog/` directory
2. Link to it from index.html navigation
3. Add any CSS/JS as needed
4. Sync to GitHub

## 🔧 Troubleshooting

### Problem: "No module named tkinter"

**Solution:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk

# Windows
# Reinstall Python and ensure tkinter is selected
```

### Problem: Git authentication failed

**Solution A: Use SSH**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub:
# 1. Go to Settings → SSH keys
# 2. Click "New SSH key"
# 3. Paste key and save

# Update remote URL
cd blog
git remote set-url origin git@github.com:username/repo.git
```

**Solution B: Use Personal Access Token**
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token with `repo` scope
3. Use token as password when prompted

### Problem: Local server won't start

**Solution:**
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill existing process
kill -9 <PID>

# Or use different port
cd blog
python3 -m http.server 8080
```

### Problem: GitHub Pages not updating

**Solution:**
1. Check if files were pushed: `git log`
2. Check GitHub Actions for deployment status
3. Wait 5-10 minutes (deployment takes time)
4. Clear browser cache (Ctrl+Shift+R)
5. Verify GitHub Pages is enabled in Settings

### Problem: CMS won't save posts

**Solution:**
1. Check file permissions: `ls -la blog/`
2. Ensure posts.json is writable
3. Try running CMS with sudo/administrator
4. Check error messages in terminal

### Problem: Images not displaying

**Solution:**
1. Check if images are in `blog/images/` directory
2. Verify paths in posts.json
3. Check file permissions
4. Ensure image formats are supported
5. Clear browser cache

## 📚 Advanced Usage

### Custom Domain Name

1. Buy a domain from registrar (e.g., Namecheap, GoDaddy)
2. In GitHub repository, go to Settings → Pages
3. Under "Custom domain", enter your domain
4. Update DNS records at your registrar:
   ```
   Type: CNAME
   Name: @
   Value: username.github.io
   ```
5. Wait for DNS propagation (24-48 hours)

### Adding Analytics

1. Sign up for Google Analytics
2. Get tracking ID
3. Add to `blog/index.html`:
   ```html
   <head>
     <!-- Add before closing head tag -->
     <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
     <script>
       window.dataLayer = window.dataLayer || [];
       function gtag(){dataLayer.push(arguments);}
       gtag('js', new Date());
       gtag('config', 'GA_MEASUREMENT_ID');
     </script>
   </head>
   ```

### Custom CSS Framework

Replace Tailwind with another framework:
1. Add framework CDN link in `<head>`
2. Update HTML classes to match framework
3. Remove Tailwind script
4. Add custom CSS as needed

## 🎓 Best Practices

1. **Always preview before publishing** - Use the preview button
2. **Write meaningful commit messages** - Makes history clearer
3. **Keep images optimized** - Compress before uploading
4. **Test on mobile** - Use browser dev tools
5. **Backup regularly** - Git provides version control
6. **Use categories** - Helps organize content
7. **Write good excerpts** - Improves SEO
8. **Keep posts concise** - Online readers prefer shorter content

## 📖 Additional Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Python tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)

## 💡 Tips

1. **Keyboard Shortcuts in CMS**
   - Save: Ctrl+S (in some systems)
   - Use toolbar buttons for quick formatting

2. **Search Operators**
   - Use specific terms for better results
   - Search is case-insensitive

3. **Image Optimization**
   - Use images under 500KB
   - Use WebP format for better compression
   - Consider using CDN for large sites

4. **SEO Tips**
   - Use descriptive titles
   - Write good excerpts
   - Add alt text to images
   - Use relevant categories

## 🆘 Getting Help

If you encounter issues:
1. Check this guide first
2. Review error messages carefully
3. Search online for specific errors
4. Check GitHub repository issues
5. Verify all prerequisites are installed

---

Happy blogging! 🎉
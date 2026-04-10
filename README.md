# Blog System with GitHub Integration

A complete, professional blogging system with a modern website and Python Tkinter CMS dashboard that manages everything and syncs with GitHub.

## 🚀 Features

### Blog Website
- ✨ Modern, responsive design using Tailwind CSS
- 🔍 Built-in search functionality
- 📱 Mobile-friendly interface
- 🎨 Professional styling with gradient effects
- 🔗 Social media integration (Instagram, LinkedIn, GitHub)
- 📝 Clean typography and layout
- 🖼️ Support for featured images in posts

### CMS Dashboard
- 🖥️ Full-featured Python Tkinter GUI
- ✍️ Create, edit, and delete blog posts
- 🖼️ Image upload and management
- 📝 Rich text editor with HTML support
- 🔄 Automatic sync to GitHub
- 📊 Post preview in browser
- 🎯 Post categorization
- 📅 Date management

### GitHub Integration
- 🚀 Push updates directly from CMS
- 📦 Complete Git automation
- 🌐 GitHub Pages support
- 🔐 Secure Git operations
- 📝 Commit message automation

## 📁 Project Structure

```
blog-system/
├── blog/
│   ├── index.html          # Main blog website
│   ├── posts.json          # Blog posts data
│   └── images/             # Post images
├── cms/
│   └── blog_cms.py         # CMS Dashboard application
├── scripts/
│   ├── create_github_repo.sh    # Create GitHub repository
│   └── sync_to_github.sh        # Sync changes to GitHub
├── setup.sh              # Complete setup automation
├── start.sh              # Start CMS and local server
└── README.md            # This file
```

## 🛠️ Installation & Setup

### Prerequisites

1. **Python 3** (with tkinter)
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install python3 python3-tk
   
   # macOS
   brew install python-tk
   
   # Windows
   # Python includes tkinter by default
   ```

2. **Git**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install git
   
   # macOS
   brew install git
   
   # Windows
   # Download from https://git-scm.com/download/win
   ```

3. **GitHub CLI (Optional, for automated repo creation)**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install gh
   
   # macOS
   brew install gh
   
   # Windows
   winget install --id GitHub.cli
   ```

### Quick Setup

Run the automated setup script:

```bash
chmod +x setup.sh
./setup.sh
```

The script will:
1. ✅ Check for required tools
2. ✅ Create directory structure
3. ✅ Make scripts executable
4. ✅ Initialize Git repository
5. ✅ Optionally create GitHub repository
6. ✅ Launch CMS Dashboard

### Manual Setup

If you prefer manual setup:

1. **Create directories:**
   ```bash
   mkdir -p blog/images
   mkdir -p cms
   mkdir -p scripts
   ```

2. **Make scripts executable:**
   ```bash
   chmod +x scripts/*.sh
   chmod +x setup.sh start.sh
   ```

3. **Initialize Git (in blog directory):**
   ```bash
   cd blog
   git init
   git add .
   git commit -m "Initial commit"
   cd ..
   ```

## 🚀 Getting Started

### Starting the System

Run the start script to launch both the CMS and local server:

```bash
chmod +x start.sh
./start.sh
```

Or start the CMS directly:

```bash
cd cms
python3 blog_cms.py
```

### Creating Your First Post

1. **Open CMS Dashboard** - The dashboard will open automatically
2. **Connect to GitHub** - Enter your GitHub repository name
3. **Click "+ New Post"** - Create your first blog post
4. **Fill in the details:**
   - Title
   - Excerpt (short summary)
   - Category
   - Featured image (optional)
   - Content (use HTML formatting)
5. **Click "💾 Save Post"** - Save your post
6. **Click "🚀 Sync to GitHub"** - Publish to GitHub

### Creating GitHub Repository

#### Automated (with GitHub CLI)

```bash
./scripts/create_github_repo.sh
```

#### Manual

1. Go to GitHub.com
2. Click "Create repository"
3. Enter repository name and description
4. Make it public
5. Don't initialize with README (we have files already)
6. Copy the repository URL
7. In your blog directory:
   ```bash
   cd blog
   git remote add origin <repository-url>
   git push -u origin main
   ```

### Enabling GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" → "Pages"
3. Under "Source", select "main" branch
4. Click "Save"
5. Your site will be live at: `https://username.github.io/repository-name/`

## 📝 Using the CMS Dashboard

### Post Management

#### Creating a Post
1. Click "+ New Post" button
2. Fill in the post details
3. Write your content (supports HTML)
4. Add images using the "Browse" button
5. Click "💾 Save Post"

#### Editing a Post
1. Select a post from the list on the left
2. Make your changes
3. Click "💾 Save Post"

#### Deleting a Post
1. Select a post from the list
2. Click "🗑️ Delete Post"
3. Confirm deletion

#### Previewing a Post
1. Select a post
2. Click "👁️ Preview" to open in browser

### Content Formatting

The CMS supports HTML formatting. Use these tags:

- **Bold**: `<strong>text</strong>`
- *Italic*: `<em>text</em>`
- Headings: `<h2>Heading</h2>`
- Links: `<a href="url">text</a>`
- Images: `<img src="images/filename.jpg" alt="description">`
- Lists: 
  ```html
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
  </ul>
  ```
- Paragraphs: `<p>Your text</p>`

### Toolbar Buttons

The editor toolbar provides quick insert buttons:
- **Bold** - Insert bold tag
- **Italic** - Insert italic tag
- **Heading** - Insert heading tag
- **Link** - Insert link tag
- **Image** - Insert image tag
- **List** - Insert list tags

## 🔄 Syncing to GitHub

### From CMS Dashboard

1. Make sure you've entered your GitHub repository name
2. Click "🚀 Sync to GitHub" button
3. The CMS will:
   - Add all changes
   - Create a commit
   - Push to GitHub

### Using Script

```bash
./scripts/sync_to_github.sh
```

### Manual Git Commands

```bash
cd blog
git add .
git commit -m "Update blog content"
git push origin main
```

## 🌐 Viewing Your Blog

### Local Preview

When you run `./start.sh`, the blog is available at:
```
http://localhost:8000
```

### Live on GitHub Pages

After enabling GitHub Pages, your blog will be at:
```
https://username.github.io/repository-name/
```

## 📊 Blog Features

### Search Functionality
- Real-time search as you type
- Searches through titles, excerpts, and content
- Instant filtering of posts

### Social Media Links
Your signature links are automatically included:
- Instagram: https://www.instagram.com/namanmic
- LinkedIn: https://www.linkedin.com/
- GitHub: https://www.github.com/nksdev/

### Post Display
- Featured image support
- Date and category display
- Excerpt on card view
- Full content in post view
- Responsive card grid layout

## 🛠️ Troubleshooting

### Git Authentication Issues

If you encounter Git authentication errors:

1. **Set up SSH key:**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   cat ~/.ssh/id_ed25519.pub
   # Copy and add to GitHub SSH keys
   ```

2. **Use Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate new token with repo permissions
   - Use token as password when pushing

### tkinter Not Found

If you get "No module named tkinter":

```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

### GitHub Pages Not Updating

If changes aren't appearing:

1. Check GitHub Actions tab for deployment status
2. Wait a few minutes (deployment takes time)
3. Clear browser cache
4. Check if files were actually pushed

### CMS Won't Start

If the CMS won't open:

1. Check Python is installed: `python3 --version`
2. Check tkinter is available: `python3 -c "import tkinter"`
3. Check file permissions: `chmod +x cms/blog_cms.py`
4. Run with error output: `python3 cms/blog_cms.py`

## 📝 Customization

### Changing Social Links

Edit `blog/index.html` and find the footer section:

```html
<a href="https://www.instagram.com/namanmic" target="_blank">...</a>
<a href="https://www.linkedin.com/" target="_blank">...</a>
<a href="https://www.github.com/nksdev/" target="_blank">...</a>
```

### Styling

The blog uses Tailwind CSS. To customize colors and styling:
1. Edit the Tailwind config in `blog/index.html`
2. Modify the `<style>` section for custom CSS
3. Update color values as needed

### Adding New Features

To add new features:
1. Modify `blog/index.html` for frontend changes
2. Update `cms/blog_cms.py` for CMS changes
3. Test locally before pushing to GitHub

## 📚 Additional Resources

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Python tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## 🤝 Support

For issues or questions:
1. Check this README first
2. Review the troubleshooting section
3. Check GitHub Actions logs for deployment issues
4. Verify Git configuration

## 📄 License

This project is open source and available for personal and commercial use.

## 🎉 Enjoy Blogging!

Created with ❤️ for developers who want a simple, powerful blogging solution.

---

**Quick Start Commands:**
```bash
# Setup everything
./setup.sh

# Start the system
./start.sh

# Sync to GitHub
./scripts/sync_to_github.sh
```
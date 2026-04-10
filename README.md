# Blog_System
A lightweight developer blog platform with CMS integration and GitHub automation, designed for simplicity, speed, and full control.
📌 Features
📝 Static blog system (HTML + JSON based)
⚙️ Custom CMS for managing posts
🔄 GitHub sync automation scripts
🚀 One-command setup & start scripts
📂 Organized project structure
🧠 Developer-friendly workflow
📁 Project Structure
blog_github/
│── blog/                # Static blog frontend
│   ├── index.html
│   ├── posts.json
│   └── images/
│
│── cms/                 # Blog CMS system
│   ├── blog_cms.py
│   └── requirements.txt
│
│── scripts/             # Automation scripts
│   ├── create_github_repo.sh
│   └── sync_to_github.sh
│
│── nksdevblog/          # Git repo workspace
│── outputs/             # Logs / outputs
│── setup.sh             # Initial setup
│── start.sh             # Start services
│── INSTALLATION_GUIDE.md
│── QUICKSTART.md
│── todo.md
⚡ Quick Start
1️⃣ Clone the repository
git clone https://github.com/nksdev/blog_github.git
cd blog_github
2️⃣ Run setup
chmod +x setup.sh
./setup.sh
3️⃣ Start the project
chmod +x start.sh
./start.sh
🧠 CMS Usage
The CMS is built using Python.
Run manually:
cd cms
pip install -r requirements.txt
python blog_cms.py
👉 Use it to:
Add new blog posts
Edit existing posts
Manage JSON content
🔄 GitHub Automation
Create Repo Automatically
./scripts/create_github_repo.sh
Sync Blog to GitHub
./scripts/sync_to_github.sh
🌐 Blog System
Static frontend (index.html)
Data-driven using posts.json
Easily customizable UI
📦 Requirements
Python 3.x
Git
Bash (Linux / Mac / WSL)
🛠️ Future Improvements
🔐 Authentication for CMS
🌍 Deployment automation (Netlify/Vercel)
📊 Analytics integration
🧠 AI-assisted blog writing
🎨 UI enhancements
🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to improve.
📄 License
This project is open-source. Use it freely and modify as needed.
👨‍💻 Author
NKSDev
Cybersecurity student & builder 🚀
💬 Final Note
This project is perfect if you:
Want full control over your blog
Hate heavy frameworks 😤
Love automation + hacking workflows
If you want next level upgrade 😏
I can help you turn this into:
🔥 full hacker-style blogging platform
🤖 AI auto-post generator
🕵️ anonymous blogging system

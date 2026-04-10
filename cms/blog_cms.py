#!/usr/bin/env python3
"""
Blog CMS Dashboard - Final Visibility & Preview Version
Features: High Contrast UI, Tabbed Editor/Preview, Visual Markdown Rendering
"""
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog, colorchooser, simpledialog
import json, os, subprocess, re
from datetime import datetime
import markdown
from PIL import Image, ImageTk

class ModernStyle:
    # UI Constants - High Visibility
    BG_COLOR = '#e8eaed'          # Light Gray Background
    SIDEBAR_BG = '#ffffff'        # White Sidebar
    EDITOR_BG = '#ffffff'         # White Editor
    TEXT_COLOR = '#000000'        # Pure Black Text
    ACCENT_COLOR = '#1a73e8'      # Google Blue
    BTN_BG = '#f1f3f4'            # Light Gray Button BG
    BTN_BORDER = '#dadce0'        # Visible Border Color
    HIGHLIGHT = '#e8f0fe'         # Selection Highlight

class BlogCMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Naman's CMS - Editor & Preview")
        self.root.geometry("1450x900")
        self.root.configure(bg=ModernStyle.BG_COLOR)
        
        # Paths
        self.base_dir = os.path.abspath(os.path.dirname(__file__))
        self.blog_dir = os.path.join(self.base_dir, 'blog')
        self.images_dir = os.path.join(self.blog_dir, 'images')
        self.posts_file = os.path.join(self.blog_dir, 'posts.json')
        self.github_username = 'nksdev' 
        
        # Ensure directories
        if not os.path.exists(self.blog_dir): os.makedirs(self.blog_dir)
        if not os.path.exists(self.images_dir): os.makedirs(self.images_dir)
        
        self.posts = self.load_posts()
        self.current_id = None
        
        # Setup
        self.setup_styles()
        self.setup_ui()
        self.refresh_list()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Clear, Visible Buttons
        style.configure('TButton', 
                        font=('Helvetica', 10, 'bold'), 
                        background=ModernStyle.BTN_BG, 
                        foreground=ModernStyle.TEXT_COLOR, 
                        borderwidth=2, 
                        relief='raised',
                        padding=8) # Increased padding for visibility
        
        style.map('TButton', background=[('active', '#dadce0')])

        # Primary Action Button (Blue)
        style.configure('Action.TButton', 
                        font=('Helvetica', 10, 'bold'), 
                        background=ModernStyle.ACCENT_COLOR, 
                        foreground='white', 
                        borderwidth=0, 
                        relief='flat',
                        padding=10)
        style.map('Action.TButton', background=[('active', '#1557b0')])

        # Danger Button (Red)
        style.configure('Danger.TButton', 
                        font=('Helvetica', 9, 'bold'), 
                        background='#d93025', 
                        foreground='white', 
                        borderwidth=0, 
                        relief='flat',
                        padding=8)

    def load_posts(self):
        if os.path.exists(self.posts_file):
            try:
                with open(self.posts_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def save_posts_json(self):
        with open(self.posts_file, 'w', encoding='utf-8') as f:
            json.dump(self.posts, f, indent=4)

    def setup_ui(self):
        # --- Main Layout ---
        main_container = tk.Frame(self.root, bg=ModernStyle.BG_COLOR)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # --- Sidebar ---
        sidebar = tk.Frame(main_container, bg=ModernStyle.SIDEBAR_BG, width=320, padx=15, pady=15, relief='raised', borderwidth=1)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)

        # Title
        tk.Label(sidebar, text="POSTS", font=('Helvetica', 16, 'bold'), bg=ModernStyle.SIDEBAR_BG, fg=ModernStyle.TEXT_COLOR).pack(pady=(0, 15), anchor='w')
        
        # Search
        tk.Label(sidebar, text="Search:", font=('Helvetica', 10, 'bold'), bg=ModernStyle.SIDEBAR_BG).pack(anchor='w')
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(sidebar, textvariable=self.search_var, bg='white', relief='solid', borderwidth=1, highlightthickness=0)
        search_entry.pack(fill=tk.X, pady=(5, 15), ipady=5)
        self.search_var.trace('w', self.refresh_list)

        # Listbox
        self.listbox = tk.Listbox(sidebar, bg=ModernStyle.SIDEBAR_BG, fg=ModernStyle.TEXT_COLOR, 
                                  selectbackground=ModernStyle.HIGHLIGHT, selectforeground='black',
                                  font=('Helvetica', 11), borderwidth=0, highlightthickness=1, highlightcolor=ModernStyle.ACCENT_COLOR, height=20)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.load_selected)
        
        # Sidebar Buttons
        ttk.Separator(sidebar, orient='horizontal').pack(fill='x', pady=20)
        
        ttk.Button(sidebar, text="+ NEW POST", command=self.new_post, style='Action.TButton').pack(fill=tk.X, pady=5)
        ttk.Button(sidebar, text="DELETE POST", command=self.delete_post, style='Danger.TButton').pack(fill=tk.X, pady=5)
        
        # Git Section
        tk.Label(sidebar, text="GITHUB SETTINGS", font=('Helvetica', 10, 'bold'), bg=ModernStyle.SIDEBAR_BG, fg='gray').pack(pady=(30, 5), anchor='w')
        self.repo_entry = tk.Entry(sidebar, bg='white', relief='solid', borderwidth=1, highlightthickness=0)
        self.repo_entry.insert(0, "repo-name")
        self.repo_entry.pack(fill=tk.X, pady=5, ipady=5)
        ttk.Button(sidebar, text="LINK REMOTE", command=self.set_remote).pack(fill=tk.X, pady=5)

        # --- Main Content Area (Tabs) ---
        content_frame = tk.Frame(main_container, bg=ModernStyle.BG_COLOR)
        content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(content_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab 1: Editor
        self.tab_editor = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_editor, text='  ✍️ EDITOR  ')
        
        # Tab 2: Preview
        self.tab_preview = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_preview, text='  👁️ PREVIEW  ')
        # Bind tab change to refresh preview
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)

        self.setup_editor_tab()
        self.setup_preview_tab()

        # Footer Actions
        footer = tk.Frame(content_frame, bg=ModernStyle.SIDEBAR_BG, height=70, pady=10)
        footer.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(footer, textvariable=self.status_var, bg=ModernStyle.SIDEBAR_BG, fg='gray', font=('Helvetica', 9)).pack(side=tk.LEFT, padx=20)
        
        btn_frame = tk.Frame(footer, bg=ModernStyle.SIDEBAR_BG)
        btn_frame.pack(side=tk.RIGHT, padx=20)
        
        ttk.Button(btn_frame, text="SAVE DRAFT", command=self.save_post_data, width=15).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="SYNC TO GITHUB", command=self.sync_github, width=20).pack(side=tk.LEFT, padx=5)

    def setup_editor_tab(self):
        # Title
        title_frame = tk.Frame(self.tab_editor, bg=ModernStyle.EDITOR_BG)
        title_frame.pack(fill=tk.X, padx=20, pady=15)
        self.title_entry = tk.Entry(title_frame, font=('Helvetica', 22, 'bold'), bg=ModernStyle.EDITOR_BG, fg=ModernStyle.TEXT_COLOR, relief='flat', borderwidth=0)
        self.title_entry.insert(0, "Post Title Here...")
        self.title_entry.pack(fill=tk.X)
        ttk.Separator(title_frame, orient='horizontal').pack(fill='x', pady=(10,0))

        # Toolbar (High Visibility)
        toolbar = tk.Frame(self.tab_editor, bg=ModernStyle.EDITOR_BG, pady=10)
        toolbar.pack(fill=tk.X, padx=10)

        # Tool helper
        def make_tool(txt, cmd):
            btn = tk.Button(toolbar, text=txt, command=cmd, bg='white', fg='black', relief='raised', borderwidth=2, padx=8, pady=2, font=('Helvetica', 10, 'bold'))
            btn.pack(side=tk.LEFT, padx=2)
            return btn

        make_tool(" BOLD ", lambda: self.wrap_selection("**", "**"))
        make_tool(" ITALIC ", lambda: self.wrap_selection("*", "*"))
        make_tool(" H1 ", lambda: self.wrap_selection("# ", ""))
        make_tool(" H2 ", lambda: self.wrap_selection("## ", ""))
        
        tk.Label(toolbar, text="|", bg=ModernStyle.EDITOR_BG, fg='gray').pack(side=tk.LEFT, padx=5)
        
        make_tool(" LINK ", self.insert_link)
        make_tool(" IMG ", self.insert_image_dialog)
        
        tk.Label(toolbar, text="|", bg=ModernStyle.EDITOR_BG, fg='gray').pack(side=tk.LEFT, padx=5)

        make_tool(" COLOR ", self.pick_color)
        make_tool(" CODE ", lambda: self.wrap_selection("```\n", "\n```"))
        
        tk.Label(toolbar, text="|", bg=ModernStyle.EDITOR_BG, fg='gray').pack(side=tk.LEFT, padx=5)

        tk.Button(toolbar, text="UPLOAD IMAGE", bg=ModernStyle.ACCENT_COLOR, fg='white', font=('Helvetica', 10, 'bold'), relief='raised', borderwidth=2, padx=15, command=self.upload_image).pack(side=tk.LEFT, padx=10)

        # Editor Text
        self.content_text = scrolledtext.ScrolledText(self.tab_editor, font=('Consolas', 13), bg=ModernStyle.EDITOR_BG, fg=ModernStyle.TEXT_COLOR, relief='flat', padx=20, pady=20, wrap=tk.WORD)
        self.content_text.pack(fill=tk.BOTH, expand=True)

    def setup_preview_tab(self):
        # Preview Container
        self.preview_text = scrolledtext.ScrolledText(self.tab_preview, font=('Helvetica', 13), bg=ModernStyle.EDITOR_BG, fg=ModernStyle.TEXT_COLOR, relief='flat', wrap=tk.WORD, padx=30, pady=30)
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        self.preview_text.configure(state='disabled')
        
        # Configure Preview Tags
        self.preview_text.tag_configure('h1', font=('Helvetica', 24, 'bold'), spacing3=10)
        self.preview_text.tag_configure('h2', font=('Helvetica', 20, 'bold'), spacing3=8)
        self.preview_text.tag_configure('bold', font=('Helvetica', 13, 'bold'))
        self.preview_text.tag_configure('italic', font=('Helvetica', 13, 'italic'))
        self.preview_text.tag_configure('code', font=('Consolas', 12), background='#f0f0f0', foreground='#d63384')
        self.preview_text.tag_configure('link', font=('Helvetica', 13, 'underline'), foreground=ModernStyle.ACCENT_COLOR)

    def on_tab_change(self, event):
        # If user switches to Preview tab, render the content
        selected_tab = self.notebook.index(self.notebook.select())
        if selected_tab == 1: # 1 is the index of the second tab (Preview)
            self.render_preview()

    def render_preview(self):
        """ Parses Markdown and displays it visually in the Preview tab """
        raw = self.content_text.get(1.0, tk.END)
        lines = raw.split('\n')
        
        self.preview_text.configure(state='normal')
        self.preview_text.delete(1.0, tk.END)
        
        for line in lines:
            line = line.strip()
            if not line: 
                self.preview_text.insert(tk.END, "\n")
                continue

            # Headers
            if line.startswith("# "):
                self.preview_text.insert(tk.END, line[2:] + "\n", 'h1')
            elif line.startswith("## "):
                self.preview_text.insert(tk.END, line[3:] + "\n", 'h2')
            elif line.startswith("### "):
                self.preview_text.insert(tk.END, line[4:] + "\n", 'h1') # Simplify to H1
            # Bold
            else:
                # Simple regex replacement for bold/italic for display
                formatted_line = line.replace("**", "").replace("*", "")
                
                # Check for image
                if line.startswith("!["):
                     self.preview_text.insert(tk.END, f"[IMAGE: {line.split('(')[1].replace(')', '')}]\n", 'italic')
                # Check for link
                elif line.startswith("["):
                    try:
                        # Very basic link parser for display
                        text = line.split("]")[0][1:]
                        url = line.split("(")[1].replace(")", "")
                        self.preview_text.insert(tk.END, text + " (" + url + ")\n", 'link')
                    except:
                        self.preview_text.insert(tk.END, formatted_line + "\n")
                else:
                    self.preview_text.insert(tk.END, formatted_line + "\n")

        self.preview_text.configure(state='disabled')

    # --- Editor Logic ---
    def wrap_selection(self, before, after):
        try:
            sel_start = self.content_text.index("sel.first")
            sel_end = self.content_text.index("sel.last")
            selected_text = self.content_text.get(sel_start, sel_end)
            self.content_text.delete(sel_start, sel_end)
            self.content_text.insert(sel_start, f"{before}{selected_text}{after}")
        except:
            cursor_pos = self.content_text.index(tk.INSERT)
            self.content_text.insert(cursor_pos, f"{before}{after}")

    def insert_link(self):
        url = simpledialog.askstring("Insert Link", "Enter URL:")
        if url:
            text = simpledialog.askstring("Insert Link", "Enter Link Text:", initialvalue="Link")
            if text:
                self.wrap_selection(f"[{text}](", f"{url})")

    def pick_color(self):
        color = colorchooser.askcolor(title="Choose Text Color")[1]
        if color:
            self.wrap_selection(f'<span style="color:{color}">', '</span>')

    def insert_image_dialog(self):
        url = simpledialog.askstring("Insert Image", "Enter Image URL:")
        if url:
            self.wrap_selection(f"![Image](", f"{url})")

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")])
        if file_path:
            filename = f"img_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
            dest_path = os.path.join(self.images_dir, filename)
            
            try:
                img = Image.open(file_path)
                if img.mode in ("RGBA", "P"): img = img.convert("RGB")
                img.save(dest_path, "JPEG", quality=75, optimize=True)
                
                cursor_pos = self.content_text.index(tk.INSERT)
                self.content_text.insert(cursor_pos, f"\n![Image](blog/images/{filename})\n")
                self.status_var.set("Image uploaded and inserted.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    # --- Data Management ---
    def save_post_data(self):
        title = self.title_entry.get().strip()
        raw_markdown = self.content_text.get(1.0, tk.END).strip()
        
        if not title:
            messagebox.showwarning("Warning", "Title is required!")
            return

        html_content = markdown.markdown(raw_markdown, extensions=['fenced_code', 'tables', 'nl2br'])
        
        if self.current_id:
            post_id = self.current_id
        else:
            post_id = title.lower().replace(" ", "-") + "-" + datetime.now().strftime("%H%M%S")
        
        # Find first image for thumbnail
        img_match = re.search(r'!\[.*?\]\((.*?)\)', raw_markdown)
        thumbnail = img_match.group(1) if img_match else ""

        post = {
            "id": post_id, 
            "title": title, 
            "content": html_content, 
            "markdown": raw_markdown,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "image": thumbnail
        }
        
        updated = False
        for i, p in enumerate(self.posts):
            if p['id'] == post_id:
                self.posts[i] = post
                updated = True
                break
        
        if not updated:
            self.posts.insert(0, post)
            self.current_id = post_id

        self.save_posts_json()
        self.refresh_list()
        self.status_var.set("Saved successfully.")

    def load_selected(self, event):
        idx = self.listbox.curselection()
        if idx:
            p = self.posts[idx[0]]
            self.current_id = p['id']
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, p['title'])
            self.content_text.delete(1.0, tk.END)
            self.content_text.insert(1.0, p.get('markdown', p.get('content', '')))
            self.status_var.set(f"Loaded: {p['title']}")

    def refresh_list(self, *args):
        search = self.search_var.get().lower()
        self.listbox.delete(0, tk.END)
        for p in self.posts:
            if search in p['title'].lower():
                self.listbox.insert(tk.END, p['title'])

    def new_post(self):
        self.current_id = None
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, "")
        self.content_text.delete(1.0, tk.END)
        self.status_var.set("New post created.")

    def delete_post(self):
        idx = self.listbox.curselection()
        if not idx: return
        if messagebox.askyesno("Confirm", "Delete this post?"):
            self.posts.pop(idx[0])
            self.save_posts_json()
            self.new_post()
            self.refresh_list()

    # --- Git ---
    def set_remote(self):
        repo = self.repo_entry.get().strip()
        if not repo: return
        url = f"https://github.com/{self.github_username}/{repo}.git"
        try:
            if not os.path.exists(os.path.join(self.blog_dir, '.git')):
                subprocess.run(['git', 'init'], cwd=self.blog_dir, check=True)
            subprocess.run(['git', 'remote', 'remove', 'origin'], cwd=self.blog_dir, stderr=subprocess.DEVNULL)
            subprocess.run(['git', 'remote', 'add', 'origin', url], cwd=self.blog_dir, check=True)
            messagebox.showinfo("Success", f"Remote set to {repo}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def sync_github(self):
        self.save_post_data()
        try:
            self.status_var.set("Syncing...")
            self.root.update()
            subprocess.run(['git', 'add', '.'], cwd=self.blog_dir, check=True)
            subprocess.run(['git', 'commit', '-m', "Update CMS"], cwd=self.blog_dir, check=True)
            subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=self.blog_dir, check=True)
            messagebox.showinfo("Success", "Pushed to GitHub!")
            self.status_var.set("Sync Complete.")
        except subprocess.CalledProcessError as e:
             # Try pull if push fails
            try:
                subprocess.run(['git', 'pull', 'origin', 'main', '--rebase'], cwd=self.blog_dir, check=True)
                subprocess.run(['git', 'push', '-u', 'origin', 'main'], cwd=self.blog_dir, check=True)
                messagebox.showinfo("Success", "Pushed after rebase!")
                self.status_var.set("Sync Complete.")
            except:
                messagebox.showerror("Error", "Sync failed. Check connection.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogCMS(root)
    root.mainloop()
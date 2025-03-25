import os
import yt_dlp
import tkinter as tk
import browser_cookie3
import requests
import webbrowser
from tkinter import filedialog, messagebox, PhotoImage

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def extract_tiktok_cookies():
    cookies = browser_cookie3.chrome(domain_name="tiktok.com")
    with open("cookies.txt", "w") as f:
        f.write("\n".join([f"{c.name}={c.value}" for c in cookies]))

def open_folder(folder_path):
    if os.path.exists(folder_path):
        webbrowser.open(folder_path)

def clean_profile_url(url):
    if "?_" in url:
        url = url.split("?_", 1)[0]
    return url.strip()

def download_videos():
    url = url_entry.get()
    path = save_path.get()
    num_videos = int(video_count_entry.get())
    if not url or not path:
        messagebox.showerror("Error", "Please enter a valid URL and select a save location.")
        return
    folder = create_folder(path)
    ydl_opts = {
        'outtmpl': os.path.join(folder, '%(uploader)s_%(title)s.%(ext)s'),
        'format': 'best',
        'cookiefile': 'cookies.txt',
        'playlistend': num_videos
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        open_folder(folder)
        messagebox.showinfo("Download Complete", f"Downloaded {num_videos} videos successfully in:\n{folder}")
    except Exception as e:
        messagebox.showerror("Download Error", str(e))

def browse_folder():
    folder_selected = filedialog.askdirectory()
    save_path.set(folder_selected)

def paste_link():
    pasted_url = root.clipboard_get().strip()
    url_entry.delete(0, tk.END)
    url_entry.insert(0, clean_profile_url(pasted_url))

def toggle_background():
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "#121212" if dark_mode else "#FFFFFF"
    fg_color = "white" if dark_mode else "black"
    root.configure(bg=bg_color)
    for widget in root.winfo_children():
        try:
            widget.configure(bg=bg_color, fg=fg_color)
        except:
            pass

root = tk.Tk()
root.title("Tok Khemra - TikTok Video Downloader")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#121212")

dark_mode = True
save_path = tk.StringVar()

# Dark Mode Toggle (Top Right)
tk.Button(root, text="Dark Mode", command=toggle_background, bg="#333", fg="white", relief="flat").place(x=520, y=10)

# Banner Image
try:
    banner = PhotoImage(file="tok_khemra_banner.png")
    tk.Label(root, image=banner, bg="#121212").pack()
except:
    tk.Label(root, text="Tok Khemra", font=("Arial", 24, "bold"), fg="white", bg="#121212").pack(pady=10)

# Input TikTok Link
tk.Label(root, text="Enter TikTok Video/Profile Link:", fg="white", bg="#121212").pack(pady=5)
url_entry = tk.Entry(root, width=50, bg="#333", fg="white", insertbackground="white")
url_entry.pack(pady=5)

tk.Button(root, text="Paste Link", command=paste_link, bg="#0078D7", fg="white", relief="flat").pack(pady=5)

# Input Number of Videos to Download
tk.Label(root, text="Number of Videos to Download:", fg="white", bg="#121212").pack(pady=5)
video_count_entry = tk.Entry(root, width=10, bg="#333", fg="white", insertbackground="white")
video_count_entry.pack(pady=5)
video_count_entry.insert(0, "10")

# Select Save Folder
tk.Button(root, text="Select Save Folder", command=browse_folder, bg="#0078D7", fg="white", relief="flat").pack(pady=5)
tk.Entry(root, textvariable=save_path, width=50, bg="#333", fg="white", insertbackground="white").pack(pady=5)

# Download Button
tk.Button(root, text="Download", command=download_videos, bg="#28A745", fg="white", relief="flat", font=("Arial", 12, "bold")).pack(pady=10)

# Social Media Buttons (Below Download Button)
social_frame = tk.Frame(root, bg="#121212")
tk.Button(social_frame, text="TikTok", command=lambda: webbrowser.open("https://www.tiktok.com/@raatechofficial"), bg="#FF0050", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(social_frame, text="Telegram", command=lambda: webbrowser.open("https://t.me/hackisreal007"), bg="#0088CC", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(social_frame, text="GitHub", command=lambda: webbrowser.open("https://github.com/KevinnRaa/kevinnRaa.git"), bg="#333", fg="white").pack(side=tk.LEFT, padx=5)
social_frame.pack(pady=10)

# Created by Khemra Label
tk.Label(root, text="Created by Khemra", fg="gray", bg="#121212", font=("Arial", 10, "italic")).pack(pady=5)

root.mainloop()


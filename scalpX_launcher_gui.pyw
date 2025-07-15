# ==== scalpX_launcher_gui.pyw ====
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def run_bot():
    subprocess.Popen(["python", "scalpx_bot.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def run_dashboard():
    subprocess.Popen(["streamlit", "run", "scalpx_dashboard_streamlit.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def build_exe():
    subprocess.Popen(["pyinstaller", "--onefile", "scalpx_bot.py", "--name", "ScalpX_LiveBot"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def open_logs():
    os.system("start logs")

def git_pull():
    subprocess.Popen(["git", "pull"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def quit_app():
    window.destroy()

window = tk.Tk()
window.title("🧠 ScalpX Launcher")
window.geometry("400x320")
window.configure(bg="#111")

def make_button(label, action):
    return tk.Button(window, text=label, command=action, width=30, height=2, bg="#222", fg="lime", font=("Segoe UI", 10, "bold"))

make_button("🚀 Run ScalpX Bot", run_bot).pack(pady=5)
make_button("📊 Launch Dashboard", run_dashboard).pack(pady=5)
make_button("🛠️ Build .EXE", build_exe).pack(pady=5)
make_button("📁 Open Logs", open_logs).pack(pady=5)
make_button("🔄 Pull Latest Updates", git_pull).pack(pady=5)
make_button("❌ Quit", quit_app).pack(pady=5)

window.mainloop()

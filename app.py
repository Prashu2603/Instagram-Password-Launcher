import tkinter as tk
from tkinter import messagebox
import subprocess

PASSWORD = "1234"

def open_instagram():
    try:
        subprocess.Popen([
            "explorer.exe",
            "shell:AppsFolder\\Facebook.InstagramBeta_8xx8rvfyw5nnt!App"
        ])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def check_password():
    if entry.get() == PASSWORD:
        messagebox.showinfo("Success", "Welcome!")
        root.destroy()
        open_instagram()
    else:
        messagebox.showerror("Error", "Wrong Password")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("Instagram Lock")
root.geometry("350x180")
root.resizable(False, False)

label = tk.Label(root, text="Instagram Lock", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=25)
entry.pack()

button = tk.Button(root, text="Unlock", command=check_password)
button.pack(pady=20)

print("Application Started")   # <-- idi add cheyyi

root.mainloop()

print("Application Closed")
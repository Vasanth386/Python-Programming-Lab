import tkinter as tk
from tkinter import messagebox, filedialog
def show_message():
    messagebox.showinfo("Info", "Hello! This is a Message Box")
def open_file():
    file = filedialog.askopenfilename()
    result_label.config(text="Selected File: " + file)
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt")
    result_label.config(text="File Saved As: " + file)
root = tk.Tk()
root.title("Messagebox & File Dialog Example")
root.geometry("400x250")
tk.Button(root, text="Show Message", command=show_message).pack(pady=10)
tk.Button(root, text="Open File", command=open_file).pack(pady=10)
tk.Button(root, text="Save File", command=save_file).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=20)
root.mainloop()
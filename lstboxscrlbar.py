import tkinter as tk
def show_selected():
    selected = listbox.get(tk.ACTIVE)
    result_label.config(text="Selected: " + selected)
root = tk.Tk()
root.title("Listbox & Scrollbar Example")
root.geometry("300x250")
frame = tk.Frame(root)
frame.pack()
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=8)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)
items = ["Python", "Java", "C", "C++", "JavaScript", "HTML", "CSS", "SQL", "Django", "Flask"]
for item in items:
    listbox.insert(tk.END, item)
button = tk.Button(root, text="Show Selected", command=show_selected)
button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
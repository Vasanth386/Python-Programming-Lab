import tkinter as tk
def new_file():
    result_label.config(text="New File Selected")
def open_file():
    result_label.config(text="Open File Selected")
def exit_app():
    root.quit()
def option_selected(option):
    result_label.config(text="Selected: " + option)
root = tk.Tk()
root.title("Menu & Menubutton Example")
root.geometry("350x250")
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
mb = tk.Menubutton(root, text="Options", relief="raised")
mb.pack(pady=20)
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option 1", command=lambda: option_selected("Option 1"))
mb.menu.add_command(label="Option 2", command=lambda: option_selected("Option 2"))
mb.menu.add_command(label="Option 3", command=lambda: option_selected("Option 3"))
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
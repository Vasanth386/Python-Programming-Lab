import tkinter as tk
def show_selection():
    hobbies = []
    if var1.get() == 1:
        hobbies.append("Reading")
    if var2.get() == 1:
        hobbies.append("Sports")
    gender = gender_var.get()
    result_label.config(text="Hobbies: " + ", ".join(hobbies) + "\nGender: " + gender)
root = tk.Tk()
root.title("Checkbutton & Radiobutton")
root.geometry("300x250")
tk.Label(root, text="Select Hobbies:").pack()
var1 = tk.IntVar()
var2 = tk.IntVar()
tk.Checkbutton(root, text="Reading", variable=var1).pack()
tk.Checkbutton(root, text="Sports", variable=var2).pack()
tk.Label(root, text="Select Gender:").pack()
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()
tk.Button(root, text="Submit", command=show_selection).pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
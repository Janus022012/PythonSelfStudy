import tkinter as tk
from tkinter import ttk

root = tk.Tk()

user_name = tk.StringVar()

def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

frame1 = ttk.Frame(root).pack(side="left")
frame2 = ttk.Frame(root).pack(side="top")
name_rectangle = tk.Label(frame1, text="Name: ").pack(side="left")
name_entry = ttk.Entry(frame1, width=15, textvariable=user_name).pack(side="left")

greet_button = tk.Button(frame2, command=greet, text="greet").pack(side="left")
quit_button = tk.Button(frame2, command=root.destroy, text="quit").pack(side="right")



root.mainloop()
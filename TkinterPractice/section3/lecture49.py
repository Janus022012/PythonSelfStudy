import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

rectangle1 = tk.Label(main, text="Rectangle 1", bg="red", fg="white").pack(fill="both", expand=True, side="top")
rectangle2 = tk.Label(main, text="Rectangle 2", bg="red", fg="white").pack(fill="both", expand=True, side="top")
rectangle3 = tk.Label(root, text="Rectangle 3", bg="green", fg="white").pack(fill="both", expand=True, side="left")

root.mainloop()

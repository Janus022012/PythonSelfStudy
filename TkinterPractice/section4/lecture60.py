import tkinter as tk
from tkinter import ttk
try:
    # Windows10のみの拡張機能で高DPIの画面(4K画面など)に対応している。
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
# widgets here!

label1 = ttk.Label(root, text="Hello, world", padding=20).pack()

# fillをつけないと1ピクセルのみの線となる。
ttk.Separator(root, orient="horizontal").pack(fill="x")

label2 = ttk.Label(root, text="Hello, World!", padding=20).pack()

root.mainloop()
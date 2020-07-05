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

selected_option = tk.StringVar()

# widgets here!
check_button = ttk.Checkbutton(root, text="Check me!", variable=selected_option, onvalue="On", offvalue="Off")
check_button.pack()

root.mainloop()
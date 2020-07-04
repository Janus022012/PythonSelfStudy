import tkinter as tk
from tkinter import ttk


try:
    # Windows10のみの拡張機能で高DPIの画面(4K画面など)に対応している。
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Greeter")

#行 1行目の重み
root.columnconfigure(0, weight=10)
root.columnconfigure(1, weight=1)
#列 1列目の重み
root.rowconfigure(1, weight=10)


def greet():
    print(f"Hello, {user_name.get() or 'World'}!")

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
# 引数なしのgridはコンポーネントを自動的に配置する。
input_frame.grid()

name_label = ttk.Label(input_frame, text="Name: ")
name_label.grid(row=0, column=0, sticky="EW")
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.grid(row=0, column=1)
name_entry.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid()

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()
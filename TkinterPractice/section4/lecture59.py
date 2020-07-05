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
root.title("Example")

# これがないとScrollbarが動かなかった。
# TODO なぜか調べる。
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# widgets here!
text = tk.Text(root, height=8)
text.grid(row=0, column=0, sticky="ew")
text.insert("1.0", "Please enter a comment....")

# Scrollbar orient="vertical" or "horizontal" command=貼り付けるリンク
text_scroll = ttk.Scrollbar(root, orient="vertical", command=text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")
# テキストコンポーネントにもリンクを貼る必要がある。
text["yscrollcommand"] = text_scroll.set

root.mainloop()
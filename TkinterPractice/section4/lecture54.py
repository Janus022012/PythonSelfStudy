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
root.title("lesson54")

# widgets here!

label1 = ttk.Label(root, text="Hello, world!", padding=20)
# テキストの大きさとフォントを設定する。
label1.config(font=("Segoe UI", 20))
label1.pack()
# 画像を含める場合には、pillowをインストールする必要がある。
# image = Image.open("logo.png")
# photo = ImageTk.PhotoImage(image)
# label = ttk.Label(root, image=photo, padding=5).pack()
# 後で変更したい場合
# label["image"] = image2
# 文字と画像を使用したい場合(右に追加される。)
# label = ttk.Label(root, image=photo, padding=5, compount="right").pack()

root.mainloop()
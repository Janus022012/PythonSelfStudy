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

# widgets here!
# heightは何行のテキストを作成するかを示す。
text = tk.Text(root, height=8)
text.pack()

# "1.0"は行番号、キャラクタ番号
text.insert("1.0", "Plese enter a comment...")
text["state"] = "disabled" # normalが対になる。

text_content = text.get("1.0", "end") # 開始位置と終了位置を明示してその間のテキストを取得する事が可能である。
print(text_content)

root.mainloop()
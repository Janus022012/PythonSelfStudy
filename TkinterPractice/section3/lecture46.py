# Button

import tkinter as tk
# ウィジェットのコンポーネントなどがttkに含まれる。
from tkinter import ttk

def greet():
    print("Hello, world!")

root = tk.Tk()

# commnadは実行したい関数
greet_button = ttk.Button(root, text="Greet", command=greet)
# Packの特性として、前の要素や親要素の上位にくっ付く。
# 引数: side   どの方向に固定されるか
# 　　   fill   コンポーネントがどの方向に対してスペースを埋めるか
# 　　   expand ウィンドウの拡張とともに、拡大するか
greet_button.pack(side="left", fill="x")
#
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="y", expand=True)

root.mainloop()
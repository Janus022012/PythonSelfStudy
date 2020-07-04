import tkinter as tk
# ウィジェットのコンポーネントなどがttkに含まれる。
from tkinter import ttk

# アプリケーションのメインウィンドウ
root = tk.Tk()
# ウィンドウを固定サイズにする。xはエックス
# 300x150(横x縦)+100+300(横のパディング+縦のパディング)
root.geometry("600x400")

# Label: bg=背景色 fg=テキスト色 text=テキスト
rectangle1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
# ipadx・ipadyはインサイドパディング
# fillはコンポーネントが持っている幅を満たすのみである。
# expand=Trueは、出来る限りのスペースを確保する。
# epand=Trueが二つ以上存在する時は等分割する。
# sideはどの側面にアンカーするかを決定する。
# side="top" or "bottom"は水平方向にスペースを占領する。
# side="left" or "right"は垂直方向にスペースを占領する。
# 拡張に関しては、先に宣言されたsideと同じ方向にあるsideで分割する。
# side="left" fill="both" expand=True    左(垂直方向に拡張)へアンカー
# side="top" fill="both" expand=True
# side="left" fill="both" expand=True
rectangle1.pack(ipadx=10, ipady=10, fill="both", expand=True, side="left")

rectangle2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle2.pack(ipadx=10, ipady=10, expand=True)

root.mainloop()

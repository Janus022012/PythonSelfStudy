import tkinter as tk
# ウィジェットのコンポーネントなどがttkに含まれる。
from tkinter import ttk

# アプリケーションのメインウィンドウ
root = tk.Tk()
# ラベルコンポーネント; 全てのコンポーネントは、どれを親コンポーネントに持つかを引数に投入する必要がある。
# またpack()はレイアウト用の関数である。
ttk.Label(root, text="Hello, World!", padding=(50, 100)).pack()

# イベントループを開始する。
root.mainloop()
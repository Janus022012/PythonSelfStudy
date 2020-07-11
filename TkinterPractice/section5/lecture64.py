import tkinter as tk
from tkinter import ttk
try:
    # Windows10のみの拡張機能で高DPIの画面(4K画面など)に対応している。
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Distance Converter")

# 行0が全体を占めるようになる
root.columnconfigure(0, weight=1)
# 列1が全体を占めるようになる
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
# gridでは中にあるコンテンツによって幅・高さが決定する。
# 最も大きいコンテンツに幅・高さを各列・行は合わせる事になる。
main.grid()

metres_label = ttk.Label(main, text="Metres: ")
metres_input = ttk.Entry(main, width=10)
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, text="Feet shown here")
calc_button = ttk.Button(main, text="Calculate")

metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="W")
metres_label.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="W")

# stickyで伸ばす事によってコンテンツの幅が広がる。
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")
root.mainloop()
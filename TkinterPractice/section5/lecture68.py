import tkinter as tk
import tkinter.font as font
from tkinter import ttk
try:
    # Windows10のみの拡張機能で高DPIの画面(4K画面など)に対応している。
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=15)

METRES_CONVERT_CONST = 3.2808
metres_value = tk.StringVar()
feet_value = tk.StringVar()

def calculate_feet(*args):
    try:
        metres_tmp = metres_value.get()
        metres_float_tmp = float(metres_tmp)
        feet_int_tmp = metres_float_tmp * METRES_CONVERT_CONST
        feet_value.set(str(feet_int_tmp))
    except ValueError:
        feet_value.set(f"Can't convert {metres_value}")


# 行0が全体を占めるようになる
root.columnconfigure(0, weight=1)
# 列1が全体を占めるようになる
root.rowconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
# gridでは中にあるコンテンツによって幅・高さが決定する。
# 最も大きいコンテンツに幅・高さを各列・行は合わせる事になる。
main.grid()

metres_label = ttk.Label(main, text="Metres: ")
# グローバルでフォントを変更しても、コンポーネントでは変更できない事がある。
metres_input = ttk.Entry(main, width=10, textvariable=metres_value, font=("Segoe UI", 15))
feet_label = ttk.Label(main, text="Feet: ")
feet_display = ttk.Label(main, textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

metres_label.grid(column=0, row=0, sticky="W")
metres_input.grid(column=1, row=0, sticky="W")
metres_label.focus()

feet_label.grid(column=0, row=1, sticky="W")
feet_display.grid(column=1, row=1, sticky="W")

# stickyで伸ばす事によってコンテンツの幅が広がる。
calc_button.grid(column=0, row=2, columnspan=2, sticky="EW")


metres_input.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()
import tkinter as tk
# ボタンの配置を設定 --- (*1)
BUTTONS = [
  ['7', '8', '9', '/'],
  ['4', '5', '6', '*'],
  ['1', '2', '3', '-'],
  ['0', '.', '=', '+']]
# ボタンイベントの作成関数 --- (*2) 
def make_click(ch):
    def click(e):
        print(ch)
        if ch == '=': calc(0); 
        else: disp.insert(tk.END, ch)
    return click
# 計算式を計算 --- (*3)
def calc(e):
    label["text"] = '= ' + str(eval(disp.get()))
# ウィンドウを作成！パァン！ --- (*4)
win = tk.Tk()
# ウィンドウタイトルを設定
win.title("めちゃシンプルな電卓")
# ウィンドウサイズの設定
win.geometry("400x460")
# ディスプレイ部分 --- (*5)
disp = tk.Entry(win, font=('', 20), justify="center")
disp.pack(fill='x')
disp.bind('<Return>', calc)
label = tk.Label(win, font=('', 20), anchor="center")
label.pack(fill='x')
# 電卓のボタンを一括作成 --- (*6)
fr = tk.Frame(win)
fr.pack()
for y, cols in enumerate(BUTTONS):
    for x, n in enumerate(cols):
        btn = tk.Button(fr, text=n,
            font=('', 20), width=6, height=3)
        btn.grid(row=y+1, column=x+1)
        btn.bind('<1>', make_click(n))
# ウィンドウを動かす --- (*7)
win.mainloop()

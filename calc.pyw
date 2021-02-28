from tkinter import *
# 画面表示
def new_func():
    root = Tk()
    return root
root = new_func()
# 文字入力機能実装
def func(v):
    var1.set(var1.get() + v)
# Cの機能実装
def clear():
    var1.set("")
# ACの機能実装
def all_clear():
    var1.set("")
# =の機能実装
def result():
    try:
        var1.set(eval(var1.get()))
    except SyntaxError:
        var1.set("エラーが発生しました。計算不可能です！")
    except ZeroDivisionError:
        var1.set("数を0で割りました。演算が定義できません！")
    except NameError:
        var1.set("定義されていない変数を使用しています。")
var1 = StringVar()
label = Label(root, textvariable=var1, fg="#000000", bg="#FFFFFF", anchor=E, height=3)# 画面部分表示色指定
label.grid(row=0, column=0, columnspan=4, sticky="EW") 
root.title("電卓 Beta 2.0")# タイトル指定
# 1列目実装
btn_c = Button(root, text="C", command=clear, width=10, height=3)
btn_c.grid(row=1, column=0)
btn_ac = Button(root, text="AC", command=all_clear, width=10, height=3)
btn_ac.grid(row=1, column=1)
btn_p = Button(root, text="%", command=lambda: func("%"), width=10, height=3)
btn_p.grid(row=1, column=2)
btn_add = Button(root, text="+", command=lambda: func("+"), width=10, height=3)
btn_add.grid(row=1, column=3)
# 2列目実装
btn_7 = Button(root, text="7", command=lambda: func("7"), width=10, height=3)
btn_7.grid(row=2, column=0)
btn_8 = Button(root, text="8", command=lambda: func("8"), width=10, height=3)
btn_8.grid(row=2, column=1)
btn_9 = Button(root, text="9", command=lambda: func("9"), width=10, height=3)
btn_9.grid(row=2, column=2)
btn_div = Button(root, text="÷", command=lambda: func("/"), width=10, height=3)
btn_div.grid(row=2, column=3)
# 3列目実装
btn_4 = Button(root, text="4", command=lambda: func("4"), width=10, height=3)
btn_4.grid(row=3, column=0)
btn_5 = Button(root, text="5", command=lambda: func("5"), width=10, height=3)
btn_5.grid(row=3, column=1)
btn_6 = Button(root, text="6", command=lambda: func("6"), width=10, height=3)
btn_6.grid(row=3, column=2)
btn_mul = Button(root, text="×", command=lambda: func("*"), width=10, height=3)
btn_mul.grid(row=3, column=3)
# 4列目実装
btn_1 = Button(root, text="1", command=lambda: func("1"), width=10, height=3)
btn_1.grid(row=4, column=0)
btn_2 = Button(root, text="2", command=lambda: func("2"), width=10, height=3)
btn_2.grid(row=4, column=1)
btn_3 = Button(root, text="3", command=lambda: func("3"), width=10, height=3)
btn_3.grid(row=4, column=2)
btn_sub = Button(root, text="-", command=lambda: func("-"), width=10, height=3)
btn_sub.grid(row=4, column=3)
# 5列目実装
btn_0 = Button(root, text="0", command=lambda: func("0"), width=10, height=3)
btn_0.grid(row=5, column=0)
btn_pt = Button(root, text=".", command=lambda: func("."), width=10, height=3)
btn_pt.grid(row=5, column=2)
btn_eq = Button(root, text="=", command=result, width=10, height=3)
btn_eq.grid(row=5, column=3)
# ウィンドウを動かす
root.mainloop()


from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
root = Tk() # 初始化Tk()

root.title("hello tkinter")    # 设置窗口标题
root.geometry("800x600")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

lable = Label(root, text="姓名：新同学", bg="pink",bd=10, font=("Arial",12), width=28, height=3)
lable.pack(side=TOP)
lable1 = Label(root, text="学号：2020010108", bg="pink",bd=10, font=("Arial",12), width=28, height=3)
lable1.pack(side=TOP)
root.mainloop()

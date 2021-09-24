
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
root = Tk() # 初始化Tk()

root.title("hello tkinter")    # 设置窗口标题
root.geometry("800x500")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

def click():
    print("点击了一次")
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='新建...',command=click)
filemenu.add_command(label='打开...',command=click)
filemenu.add_command(label='保存',command=click)
filemenu.add_command(label='关闭填写',command=root.quit)


root.mainloop()

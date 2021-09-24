
from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框
root = Tk() # 初始化Tk()

root.title("hello tkinter")    # 设置窗口标题
root.geometry("800x600")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

lable = Label(root, text="label", bg="pink",bd=10, font=("Arial",12), width=8, height=3)
lable.pack(side=TOP)

def click():
    print("hello")
button=Button(root,text='QUIT',command=click,activeforeground="black",activebackground='blue',bg='red',fg='white')
button.pack(fill=X,expand=0,anchor=CENTER)


root.mainloop()

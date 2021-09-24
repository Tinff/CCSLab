# -*- coding: utf-8 -*-
# 递归画图
def drawstars(num):
    str = "*" * num
    print(str)
    if num > 0:
        drawstars(num-1)
drawstars(20)    
    

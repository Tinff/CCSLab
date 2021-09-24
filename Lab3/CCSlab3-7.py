# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:47:23 2020

@author: zhangyu
"""

def drawstars(num):
    str = "*" * num
    print(str)
    if num > 0:
        drawstars(num-1)
drawstars(20)    
    

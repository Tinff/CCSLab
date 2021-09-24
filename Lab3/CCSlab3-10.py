# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:44:55 2020

@author: zhangyu
"""

if __name__ == '__main__':  #如果是当前模块，则执行
    import time
    start = time.time()
    for i in range(3000):
        print(i)
    end = time.time()
 
    print (end - start)



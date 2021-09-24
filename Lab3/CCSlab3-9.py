# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:43:05 2020

@author: zhangyu
"""

if __name__ == '__main__':
    import time
    print (time.ctime(time.time()))
    print (time.asctime(time.localtime(time.time())))
    print (time.asctime(time.gmtime(time.time())))



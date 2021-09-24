# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:39:16 2020

@author: zhangyu
"""


def factor(num):
    target=int(num)
    res=set()
    for i in range(1,num):
        if num%i==0:
            res.add(i)
            res.add(num/i)
    return res
for i in range(2,1001):
    if i==sum(factor(i))-i:
        print(i)



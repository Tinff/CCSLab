# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:56:35 2020

@author: zhangyu
"""


import copy
a = [1,2,3,4,['a','b']]
print('a=',a)
print('id(a):',id(a))

b = a	
print('b=',b)				# 赋值
print('id(b):',id(b))

c = a[:]				# 浅拷贝
print('c=',c)
print('id(c):',id(c))

d = copy.copy(a)		# 浅拷贝
print('d=',d)
print('id(d):',id(d))

e = copy.deepcopy(a)	# 深拷贝
print('e=',e)
print('id(e):',id(e))

a.append(5)
a[4].append('c')
print('a=',a)
print('id(a):',id(a))
print('b=',b)	
print('id(b):',id(b))





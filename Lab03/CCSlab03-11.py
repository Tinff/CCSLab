# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 10:49:59 2020

@author: zhangyu
"""


import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day=day.replace(year=day.year+22)
print(day)



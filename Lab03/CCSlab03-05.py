# -*- coding: utf-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天

def isLeapYear(y):
    return (y%400==0 or (y%4==0 and y%100!=0))

DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
res=0
year=2020
month=5
day=26
if isLeapYear(year):
    DofM[2]+=1
for i in range(month):
    res+=DofM[i]
print(res+day)

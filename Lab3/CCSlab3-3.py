#coding=gbk
a=10

#　　为一个变量赋值
print(a)
a=b=10
print(a)
print(b)
#　　同时为多个变量赋值

a,b,c='abc'
print(a)
print(b)
print(c)
#　　拆解序列，要一一对应

a,*b='abc'
print(a)
print(b)
#　　*b自动为变量b创建列表

a,b='abc',[1,2,3]
print(a)
print(b)
#　　各自赋值
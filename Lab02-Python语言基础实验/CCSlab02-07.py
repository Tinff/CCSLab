#coding=utf-8
#练习


# 数字组合
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：遍历全部可能，把有重复的剃掉。
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                print(i,j,k)
                total+=1
print(total)

# 简便方法 用itertools中的permutations即可。
import itertools
sum2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(i)
    sum2+=1
print(sum2)


# 九九乘法表
# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()


 
#打破循环
# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

while True:
    try:
        n=float(input('输入一个数字：'))
    except:
        print('输入错误')
        continue
    dn=n**2
    print('其平方为：',dn)
    if dn<50:
        print('平方小于50，退出')
        break

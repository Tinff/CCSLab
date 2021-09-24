#coding=utf-8
# gbk 
# 用id()函数输出变量地址的示例程序
str1 = "这是一个变量";
print("变量str1的值是："+str1);  
print("变量str1的地址是：%d" %(id(str1))); 
str2 = str1;
print("变量str2的值是："+str2);  
print("变量str2的地址是：%d" %(id(str2))); 
str1 = "这是另一个变量";
print("变量str1的值是："+str1);  
print("变量str1的地址是：%d" %(id(str1)));   
print("变量str2的值是："+str2);  
print("变量str2的地址是：%d" %(id(str2)));

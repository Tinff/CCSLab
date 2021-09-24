# coding=utf-8
import math

#G(s)=400/(s^2+50s)
class ControlledObjectOne:
    __Uk_1 = 0.0
    __Uk_2 = 0.0
    __Yk = 0.0
    __Yk_1 = 0.0
    __Yk_2 = 0.0
    __Uk = 0.0

    #从控制器获取控制量
    def InputCv(self,Uk):
        self.__Uk = Uk
        return

    #控制对象输出的过程值
    def OutputPv(self,):
        #self.__Yk = 1.9512 * self.__Yk_1 - 0.9512 * self.__Yk_2 + 1.9671 * math.pow(10, -4) * self.__Uk_1 + 1.9346 * math.pow(10, -4) * self.__Uk_2
        self.__Yk = 1.9512 * self.__Yk_1 - 0.9512 * self.__Yk_2 + 0.00019671 * self.__Uk_1 + 0.00019346 * self.__Uk_2
        self.__Uk_2 = self.__Uk_1
        self.__Uk_1 = self.__Uk
        self.__Yk_2 = self.__Yk_1
        self.__Yk_1 = self.__Yk

        return self.__Yk

#	增量型数字PID控制算法
class PIDcontroller:
    #__PV = 0.0.001
    #__SV = 0.0.001
    __TC = 1 #周期，ms
    __Delta = 0.0
    __Ti = 0.0
    __Td = 0.0
    __Kp = 0.0
    __Ki = 0.0
    __Kd = 0.0   #PID参数
    __error = 0.0
    __error_1 = 0.0
    __error_2 = 0.0  #误差
    __Uk = 0.0
    __Uk_1 = 0.0  #PID当前周期输出，前一周期输出
    __dUk = 0.0  #增量输出

    #输入采样周期和PID三个参数
    def __init__(self,TC,Delta,Ti,Td):
        self.__TC = TC
        self.__Delta = Delta
        self.__Ti = Ti
        self.__Td = Td
        self.__CalPidParameters()
        return

    #计算PID参数
    def __CalPidParameters(self,): #私有方法
        self.__Kp = 1 / self.__Delta
        self.__Ki = self.__Kp * self.__TC / self.__Ti
        self.__Kd = self.__Kp * self.__Td / self.__TC
        return

    #输入设定值SV和采样值PV，控制器计算输出CV值
    def Exec(self,SV,PV):
        #计算偏差
        self.__error = SV - PV
        #PID增量计算
        self.__dUk = self.__Kp * (self.__error - self.__error_1) + self.__Ki * self.__error + self.__Kd * (self.__error - 2 * self.__error_1 + self.__error_2)
        #全量输出
        self.__Uk = self.__Uk_1 + self.__dUk
        #历史数据
        self.__error_2 = self.__error_1
        self.__error_1 = self.__error
        self.__Uk_1 = self.__Uk

        return self.__Uk

pid1 = PIDcontroller(1,0.2,800,0.01)
co1 = ControlledObjectOne()
SvList = []
PvList = []
for i in range(0,15000,1):
    sv = 10
    pv = co1.OutputPv()  #从被控对象采样
    cv = pid1.Exec(sv,pv) #计算控制输出值
    co1.InputCv(cv)#控制量送给被控对象
    SvList.append(sv)
    PvList.append(pv)


import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(SvList,color='r', linestyle='-')
plt.plot(PvList,color='b', linestyle='-') 
plt.xlabel('Time')
plt.ylabel('PV')

plt.show()
# -*- coding: utf-8 -*-
import time
import serial #导入模块
import threading

print('pySerial verison is: %s' % serial.VERSION)
exitFlag = 0
class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("start thread：" + self.name)
        inputChar = ''
        while (inputChar.lower() != 'q'):
            inputChar = input("application is running, input q to quit.\n")
            print('your input is %s' % inputChar)
            time.sleep(1)
        global exitFlag 
        exitFlag = 1
        print("exit thread：" + self.name)

thread1 = myThread(1, "thread1")
thread1.start()
thread1.join(1)

#端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx = "COM3"
bps = 115200 #波特率
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex = 5
# 打开串口，并得到串口对象
ser = serial.Serial(portx,bps,timeout=timex)

data = ''
while 1 :
    len = ser.in_waiting

    if len > 0:
        data = ser.read(len)
        msgStr = data.decode()
        msgStr = msgStr.upper()
        print('received message from %s: %s' % (portx,msgStr))
        #处理收到的信息，并准备response
        msgStr = msgStr.replace(' ','') 
        

        deviceId = msgStr[0:2]
        if deviceId == 'FF':
            cmd = msgStr[2:4]
            if cmd == '03':
                # 写数据
                responseData = 'FF 03 02 1C 17 D9 4A'
                result = ser.write(responseData.encode())

    time.sleep(1)

    if exitFlag:
        break

 



ser.close()#关闭串口


try:
    x = 1
except Exception as e:
    print("---异常---：",e)

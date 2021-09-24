# -*- coding: utf-8 -*-
import time
import serial #导入模块
import threading
import sqlite3

print("主站程序")

print('pySerial verison is: %s' % serial.VERSION)
exitFlag = False

#端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
portx = "COM4"
bps = 115200 #波特率
#超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
timex = 5
# 打开串口，并得到串口对象
ser = serial.Serial(portx,bps,timeout=timex)



class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print("start thread：" + self.name)
        inputStr = ''
        while (inputStr.lower() != 'q'):
            print('input device ID, or input q to quit.')
            inputStr = input('input:\n')
            print('your input is %s' % inputStr)
            if inputStr != 'q':
                global ser
                cmdData = inputStr #' 03 00 00 00 01 91 D4' #03 02 1C 17 D9 4A
                result = ser.write(cmdData.encode())

            time.sleep(1)
        global exitFlag 
        exitFlag = True
        print("exit thread：" + self.name)

thread1 = myThread(1, "thread1")
thread1.start()
thread1.join(1)

data = ''
while not exitFlag :
    len = ser.in_waiting

    if len > 0:
        data = ser.read(len)
        msgStr = data.decode()
        print('received message from %s: %s' % (portx,msgStr))
        #处理收到的信息，并准备response
        msgStr = msgStr.replace(' ','') 

        #save to database------------------------------------------
        
        # 连接数据库(如果不存在则创建)
        conn = sqlite3.connect('ProcessData.db')
        # 创建游标
        cursor = conn.cursor()
        # 写入数据表
        sql = "INSERT INTO PDATA(p_data) VALUES(\'%s\')" % (msgStr)
        #sql = "INSERT INTO PDATA(p_data) VALUES('S9DA06783C56E7')"
        cursor.execute(sql)
        # 提交事务
        conn.commit()
        print("INSERT INTO PDATA successfully")

        # 关闭游标
        cursor.close()
        # 提交事务
        conn.commit()
        # 关闭连接
        conn.close()

        #---------------------------------------------show
        deviceId = msgStr[0:2]
        dataLen = msgStr[4:6]
        dataTemp = msgStr[6:10]
        temp = int(dataTemp,16) / 100 - 40
        print('The temperature is %0.2f ℃' % temp)
        #保存到数据库



    time.sleep(1)


ser.close()#关闭串口


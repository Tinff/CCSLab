# -*- coding: utf-8 -*-
import serial #导入模块
try:
  #端口，GNU / Linux上的/ dev / ttyUSB0 等 或 Windows上的 COM3 等
  portx = "COM3"
  bps = 115200 #波特率
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
  timex = 5
  # 打开串口，并得到串口对象
  ser = serial.Serial(portx,bps,timeout=timex)
  # 写数据
  result = ser.write("ABC".encode())
  result = ser.write("---".encode("gbk"))
  datastr = b'45678'  #
  result = ser.write(datastr)
  result = ser.write("通信结束---".encode("gbk"))

  ser.close()#关闭串口
except Exception as e:
    print("---异常---：",e)

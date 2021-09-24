import control
import control.matlab
import math

#unit s
Ts = 1 
#s = control.matlab.tf('s')
#sys = (math.exp(-80 * s)) / (60 * s + 1)

num1,den1 = control.matlab.pade(80,3)
sys1 = control.matlab.tf(num1,den1)
sys2 = control.matlab.tf(1,[60,1])
sys3 = control.matlab.series(sys1,sys2)

dsys = control.matlab.c2d(sys3,Ts,method='zoh')
(num,den) = control.tfdata(dsys)
print("numerator = %s" % ("".join(str(lst) for lst in num)))
print("denominator = %s" % ("".join(str(lst) for lst in den)))

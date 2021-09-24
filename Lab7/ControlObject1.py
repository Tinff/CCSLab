import control
import control.matlab

#unit s
Ts = 0.01 
sys = control.TransferFunction(523500,[1,87.35,10470,0])
dsys = control.matlab.c2d(sys,Ts,method='zoh')
(num,den) = control.tfdata(dsys)
print("numerator = %s" % ("".join(str(lst) for lst in num)))
print("denominator = %s" % ("".join(str(lst) for lst in den)))

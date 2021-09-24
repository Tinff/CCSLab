import control
import control.matlab

#unit s
Ts = 0.001 
s = control.matlab.tf('s')
sys  = (400)/(s**2 + 50*s + 0)

dsys = control.matlab.c2d(sys,Ts,method='zoh')
(num,den) = control.tfdata(dsys)
print("numerator = %s" % ("".join(str(lst) for lst in num)))
print("denominator = %s" % ("".join(str(lst) for lst in den)))

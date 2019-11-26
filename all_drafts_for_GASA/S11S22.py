import random
import math


Zg = 33.85-5.015j
Zd = 46.925-6.83j

Zin_1 = -3.669-68.703j
Zout_1 = 27.672-147.113j
Zin_2 = 2.847-61.3j
Zout_2 = 51.998-144.629j
Zin_3 = 1.878-59.295j
Zout_3 = 55.698-127.429j
Zin_4 = -0.969-61.703j
Zout_4 = 65.14-141.421j
'''
Zin_1 = 1.96-60.7j
Zout_1 = 27.975-149j
Zin_2 = 0.8936-60.95j
Zout_2 = 31.075-147.4j
Zin_3 = 0.324-61.45j
Zout_3 = 25.715-147.5j
Zin_4 = 0.8185-61.8j
Zout_4 = 23.62-148.5j
'''
Rx = 229958
Zls = 2 * 3.1415 * 0.01 * 20030j
#Zc = 0.085855-1.5735j
Zc20 = -0.7957981855801j
gm = 0.05508


x=   [550, 850, 800, 700, 500, 1300, 900, 710, 600, 100]








Zl5 = 2 * 3.1415 * 0.01j * x[0]#400 #650#400j
Zl4 = 2 * 3.1415 * 0.01j * x[1]#850 #600#600j
Zl3 = 2 * 3.1415 * 0.01j * x[2]#550 #850#600j
Zl2 = 2 * 3.1415 * 0.01j * x[3]#500 #550#700j
Zl1 = 2 * 3.1415 * 0.01j * x[4]#300 #600#500j

zl1 = 2 * 3.1415 * 0.01j * x[5]#900 #1450#1200j
zl2 = 2 * 3.1415 * 0.01j * x[6]#700 #750#1000j
zl3 = 2 * 3.1415 * 0.01j * x[7]#760 #360#510j
zl4 = 2 * 3.1415 * 0.01j * x[8]#600 #400#350j
zl5 = 2 * 3.1415 * 0.01j * x[9]#200 #50#50j

Zin1 = Zg + Zl1
Zin2 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin1)
Zin3 = Zin2 + Zl2
Zin4 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin3)
Zin5 = Zin4 + Zl3
Zin6 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin5)
Zin7 = Zin6 + Zl4
Zin8 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rx)
Zin9 = Zin8 + Zl5

Zout1 = Zd + zl1
Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
Zout3 = Zout2 + zl2
Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)
Zout5 = Zout4 + zl3
Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5 )
Zout7 = Zout6 + zl4
Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
Zout9 = Zout8 + zl5

print(" Zin1: ",Zin1,'\n',"Zin2: ",Zin2,'\n',"Zin3: ",Zin3,'\n',"Zin4: ", Zin4, '\n', "Zin5: ", Zin5,'\n', "Zin6: ", Zin6, '\n', "Zin7: ", Zin7, '\n', "Zin8: ", Zin8, '\n', "Zin9: ", Zin9, '\n')
print(" Zout1: ", Zout1,'\n', "Zout2: ",Zout2,'\n',"Zout3: ", Zout3,'\n',"Zout4: ", Zout4,'\n',"Zout5: ", Zout5,'\n', "Zout6: ",Zout6,'\n',"Zout7: ", Zout7,'\n',"Zout8: ", Zout8,'\n',"Zout9: ", Zout9,'\n')


S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)
print("S11,S22:", S11, S22)

'''
I1 = (Zin_1 + Rx) / (Zin_1 + Zin7 + Rx)
I2 = (Zin_2 / (Zin_2 + Zin5)) * I1
I3 = (Zin_3 / (Zin_3 + Zin3)) * I2
I4 = (Zin_4 / (Zin_4 + Zin1)) * I3

Izin1_gc = (Zin7 + Rx) / (Zin_1 + Zin7 + Rx)
Izin2_gc = I1 * Zin5 / (Zin_2 + Zin5)
Izin3_gc = I2 * Zin3 / (Zin_3 + Zin3)
Izin4_gc = I3 * Zin1 / (Zin_4 + Zin1)


Iout4 = gm * Zout1 * Zin_1 * Izin1_gc / Zout1      #i=g*u(电压控制电流)
Izout4_gc = gm * Zin_4 * Izin4_gc
Izout3_gc = gm * Zin_3 * Izin3_gc
Izout2_gc = gm * Zin_2 * Izin2_gc
Izout1_gc = gm * Zin_1 * Izin1_gc

Iout = Izout1_gc + Izout2_gc + Izout3_gc + Izout4_gc + Iout4
Vout = ( zl5+ Zc20 ) * Iout + Izout4_gc * Zout_4
Vin = Izin1_gc * Zin_1 + Zl5 + Zc20
'''
#function_value = 10 * math.log(abs((0.5 * Zg / Zout9) * (Vout * Vout) / (Vin * Vin)), 10)
function_value = 20*math.log(2.0 * abs(1.0 / (1.0 / (Zout9+Zd) + 1.0 / (Zin9+Zg)))* gm, 10)
print("增益：", function_value, end="\n")
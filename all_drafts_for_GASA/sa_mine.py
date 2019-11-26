import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
#from random import sample,randint,random
from random import *
def function(genetic_population):
    Zg = 33.85 - 5.015j
    Zd = 46.925 - 6.83j
    Zin_1 = -3.669 - 68.703j
    Zout_1 = 27.672 - 147.113j
    Zin_2 = 2.847 - 61.3j
    Zout_2 = 51.998 - 144.629j
    Zin_3 = 1.878 - 59.295j
    Zout_3 = 55.698 - 127.429j
    Zin_4 = -0.969 - 61.703j
    Zout_4 = 65.14 - 141.421j

    Rx = 229958
    Zls = 2 * 3.1415 * 0.01 * 20030j
    Zc20 = -0.7957981855801j
    gm = 0.05508

    Zl5 = 2 * 3.1415 * 0.01j * genetic_population[0]
    Zl4 = 2 * 3.1415 * 0.01j * genetic_population[1]
    Zl3 = 2 * 3.1415 * 0.01j * genetic_population[2]
    Zl2 = 2 * 3.1415 * 0.01j * genetic_population[3]
    Zl1 = 2 * 3.1415 * 0.01j * genetic_population[4]
    zl1 = 2 * 3.1415 * 0.01j * genetic_population[5]
    zl2 = 2 * 3.1415 * 0.01j * genetic_population[6]
    zl3 = 2 * 3.1415 * 0.01j * genetic_population[7]
    zl4 = 2 * 3.1415 * 0.01j * genetic_population[8]
    zl5 = 2 * 3.1415 * 0.01j * genetic_population[9]

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
    Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5)
    Zout7 = Zout6 + zl4
    Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
    Zout9 = Zout8 + zl5

    S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
    S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)

    I1 = (Zin_1 + Rx) / (Zin_1 + Zin7 + Rx)
    I2 = (Zin_2 / (Zin_2 + Zin5)) * I1
    I3 = (Zin_3 / (Zin_3 + Zin3)) * I2
    I4 = (Zin_4 / (Zin_4 + Zin1)) * I3

    Izin1_gc = (Zin7 + Rx) / (Zin_1 + Zin7 + Rx)
    Izin2_gc = I1 * Zin5 / (Zin_2 + Zin5)
    Izin3_gc = I2 * Zin3 / (Zin_3 + Zin3)
    Izin4_gc = I3 * Zin1 / (Zin_4 + Zin1)

    Iout4 = gm * Zout1 * Zin_1 * Izin1_gc / Zout1
    Izout4_gc = gm * Zin_4 * Izin4_gc
    Izout3_gc = gm * Zin_3 * Izin3_gc
    Izout2_gc = gm * Zin_2 * Izin2_gc
    Izout1_gc = gm * Zin_1 * Izin1_gc

    Iout = Izout1_gc + Izout2_gc + Izout3_gc + Izout4_gc + Iout4
    # Vout = (zl5 + Zc20) * Iout + Izout4_gc * Zout_4
    # Vin = Izin1_gc * Zin_1 + Zl5 + Zc20
    function_value = 20 * math.log(2.0 * abs(1.0 / (1.0 / (Zout9 + Zd) + 1.0 / (Zin9 + Zg))) * gm, 10)
    return function_value,S11,S22
# 初始function_value为15.516754


initT = 100000
minT = 0.000000000000001
iterL = 1000
eta = 0.95
k = 1
#x0 = 1.5       #init solution
genetic_population_initial = [400, 850, 850, 550, 550, 950, 950, 760, 600, 200]
genetic_population_new=[]
chrom_length = 10
x_new =[]
t = initT
x_old = genetic_population_initial
flag = True

while t > minT:
    for i in range(iterL):
        value_old = function(x_old)[0]
        #value_new_maybe,S11,S22 = function(x_old)  #x_new
        S11 = function(x_old)[1]
        S22 = function(x_old)[2]
        print(S11,S22)
        while flag:
            #genetic_population_new=[]
            genetic_population_new = sample([randint(-1, 1) for _ in range(10)], 10)
            for i in range(chrom_length):
                genetic_population_new[i] =50*genetic_population_new[i]
                #genetic_population_new.append(50 * random.randint(-1, 1))
            #genetic_population_new = np.array(genetic_population_new) + np.array(x_old)
            for i in range(chrom_length):
                genetic_population_new[i] = genetic_population_new[i] + x_old[i]

            if 0 in genetic_population_new:
                #print(genetic_population_new)
                flag=True
            else:
                S11 = function(genetic_population_new)[1]
                S22 = function(genetic_population_new)[2]
                #print(S11,S22)
                if S11 <= -15 and S22 <= -15:
                    x_new = genetic_population_new     # x_old #需要变化，赋给新列表
                    print(x_new)
                    flag = False
                else:
                    #print(genetic_population_new)
                    flag = True

        value_new = function(x_new)[0]
        res = value_new - value_old      #1y_new>y_old;2math.exp(-(y_old-y_new)/T)>random.random()
        if res > 0 or math.exp(res / (k * t)) > randint(0,1):
            x_old = x_new
            t = t*eta

print("最优解: ",x_old,"最优值：",function(x_old)[0])
#plt.plot(x_old,function(x_old),'or')
#plt.show()


import random
import math
import numpy as np
import matplotlib.pyplot as plt

population_size = 1  # 种群数量
                # 变异概率

genetic_population = []  # 种群的基因编码
fitness = []             # 适应度
fitness_mean = []        # 平均适应度
optimum_solution = []    # 每次迭代的所获得的最优解

def calculate_fitness():
    sum = 0.0
    Zg = 33.85-5.015j#34.6 - 2j  # 46.90985-5.25600j #58.0789             #41.5#48.47 - 2.084j
    Zd = 46.925-6.83j#46.84 - 7.116j  # 48.45 - 2.7975j #33.81985-3.26500j#41.4849               #58#34.62 - 2.003j

    Zin_1 = -3.669-68.703j#1.96-60.7j#2.005-61.2j#1.291 - 61.1j  # 5.175-43.165j  #-5.1-43.255j    #40.35-173.8j
    Zout_1 = 27.975-149j#27.975-149j#28.83-142.7j#26.545-150.5j#27.975-147.5j#57.121 - 137.751j  # 27-147j#56.4 - 142.25j#56.4-142.25j#36.2-142.3j#26.05-133j
    Zin_2 = 2.847-61.3j#0.8936-60.95j#1.175 - 61.05j  # 5.175-43.165j   #39.85-176j
    Zout_2 = 42.21-132.1j#31.075-147.4j#56.3-141.85j#38.78-153.9j#38.78-153.9j##34.3-140.55j#43.1305-135.259j###29.52-149j#31.075-147.4j#56.65-147.4j#56.65-142.5j#27.975-149j#31.075-147.4j#56.65-142.5j#57.121 - 137.751j  # 53-147j
    Zin_3 = 1.878-59.295j#0.324-61.45j#0.8185-61.8j#11655.011655-61.47j#0.324-61.45j#1.18 - 61j  # 5.175-43.165j    #39.85-176j
    Zout_3 = 58.463-146.2955j#.715-147.5j#20.2-157.2j#24.425-150.5j#25.715-149j#56.55-142.25j#57.121 - 137.751j  # 57.5-126.5j#56.55 - 142.25j#56.55-142.25j#36.18-142.15j
    Zin_4 = -0.969-61.703j#0.8185-61.8j#1.175 - 61.1j  # 5.175-43.165j   #39.85-176j
    Zout_4 = 53.94-153.721j#23.62-148.5j#22.3-150j#23.62-148.5j#56.55-142.3j#57.121 - 137.751j  # 67-140.5j#56.55 - 142.3j#56.55-142.3j#36.29-142.55j

    #Zout_1 =Zout_2 =Zout_3 =Zout_4 =27.975 - 147.5j

    Rx = 229958
    Zls = 2 * 3.1415 * 0.01 * 20030j
    Zc = 0.085855-1.5735j    #0.09015-1.6j #1.0 / (2 * 3.1415 * 0.01 * 4.43j)
    Zc20 = -0.7957981855801j #1.0 / (2 * 3.1415 * 0.01 * 20j)
    gm = 0.05508
    for i in range(population_size):
        Zl5 = 2 * 3.1415 * 0.01 * 400j
        Zl4 = 2 * 3.1415 * 0.01 * 600j
        Zl3 = 2 * 3.1415 * 0.01 * 600j
        Zl2 = 2 * 3.1415 * 0.01 * 700j
        Zl1 = 2 * 3.1415 * 0.01 * 500j

        zl1 = 2 * 3.1415 * 0.01 * 1200j
        zl2 = 2 * 3.1415 * 0.01 * 1000j
        zl3 = 2 * 3.1415 * 0.01 * 510j
        zl4 = 2 * 3.1415 * 0.01 * 350j
        zl5 = 2 * 3.1415 * 0.01 * 50j

        Zin1 = Zg + Zl1          #+ Zc        #考虑Zc
        Zin2 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin1)
        Zin3 = Zin2 + Zl2
        Zin4 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin3)
        Zin5 = Zin4 + Zl3
        Zin6 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin5)
        Zin7 = Zin6 + Zl4
        Zin8 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rx)
        Zin9 = Zin8 + Zl5       #+ Zc20    #考虑Zc20


        Zout1 = Zd + zl1        #不考虑Zc，注意Zd是否包括Zc
        Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
        Zout3 = Zout2 + zl2
        Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)
        Zout5 = Zout4 + zl3
        Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5 )  #  + 1.0/168141
        Zout7 = Zout6 + zl4
        Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
        Zout9 = Zout8 + zl5     #+Zc20      #考虑Zc20

        print(" Zin1: ",Zin1,'\n',"Zin2: ",Zin2,'\n',"Zin3: ",Zin3,'\n',"Zin4: ", Zin4, '\n', "Zin5: ", Zin5,'\n', "Zin6: ", Zin6, '\n', "Zin7: ", Zin7, '\n', "Zin8: ", Zin8, '\n', "Zin9: ", Zin9, '\n')
        print(" Zout1: ", Zout1,'\n', "Zout2: ",Zout2,'\n',"Zout3: ", Zout3,'\n',"Zout4: ", Zout4,'\n',"Zout5: ", Zout5,'\n', "Zout6: ",Zout6,'\n',"Zout7: ", Zout7,'\n',"Zout8: ", Zout8,'\n',"Zout9: ", Zout9,'\n')

        S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
        S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)
        print("S11,S22:", S11, S22)

        I1 = (Zin_1 + Rx) / (Zin_1 + Zin7 + Rx)
        I2 = (Zin_2 / (Zin_2 + Zin5)) * I1
        I3 = (Zin_3 / (Zin_3 + Zin3)) * I2
        I4 = (Zin_4 / (Zin_4 + Zin1)) * I3

        Izin1_gc = (Zin7 + Rx) / (Zin_1 + Zin7 + Rx)
        Izin2_gc = I1 * Zin5 / (Zin_2 + Zin5)
        Izin3_gc = I2 * Zin3 / (Zin_3 + Zin3)
        Izin4_gc = I3 * Zin1 / (Zin_4 + Zin1)

        Iout4 = gm * Zout1 * Zin_1 * Izin1_gc / Zout1  # i=g*u(电压控制电流)
        Izout4_gc = gm * Zin_4 * Izin4_gc
        Izout3_gc = gm * Zin_3 * Izin3_gc
        Izout2_gc = gm * Zin_2 * Izin2_gc
        Izout1_gc = gm * Zin_1 * Izin1_gc

        Iout = Izout1_gc + Izout2_gc + Izout3_gc + Izout4_gc + Iout4
        Vout = (zl5 + Zc20) * Iout + Izout4_gc * Zout_4
        Vin = Izin1_gc * Zin_1 + Zl5 + Zc20

        function_value = 10 * math.log(abs((0.5 * Zg / Zout_4) * (Vout * Vout) / (Vin * Vin)), 10)
        print("function_value", function_value, end="\n")


        '''
        I1 = (Zin_1 + Rx) / (Zin_1 + Zin1 + Rx)
        I2 = (Zin_2 / (Zin_2 + Zin9)) * I1
        I3 = (Zin_3 / (Zin_3 + Zin7)) * I2
        I4 = (Zin_4 / (Zin_4 + Zin5)) * I3
        I5 = (Zin_5 / (Zin_5 + Zin3)) * I4
        I6 = (Zin_6 / (Zin_6 + Zin1)) * I5
        Izin1_gc = (Zin11 + Rx) / (Zin_1 + Zin11 + Rx)
        Izin2_gc = I1 * Zin9 / (Zin_2 + Zin9)
        Izin3_gc = I2 * Zin7 / (Zin_3 + Zin7)
        Izin4_gc = I3 * Zin5 / (Zin_4 + Zl5)
        Izin5_gc = I4 * Zin3 / (Zin_5 + Zl3)
        Izin6_gc = I5 * Zin1 / (Zin_6 + Zl1)

        Iout6 = gm * (Izin1_gc * Zin_1) * Zout_1 / Zout1     #i=g*u(电压控制电流)
        Izout6_gc = gm * Zin_6 * Izin6_gc
        Izout5_gc = gm * Zin_5 * Izin5_gc
        Izout4_gc = gm * Zin_4 * Izin4_gc
        Izout3_gc = gm * Zin_3 * Izin3_gc
        Izout2_gc = gm * Zin_2 * Izin2_gc
        Izout1_gc = gm * Zin_1 * Izin1_gc

        Iout = Izout1_gc + Izout2_gc + Izout3_gc + Izout4_gc + Izout5_gc + Izout6_gc + Iout6
        Vout = ( zl7+ Zc20 ) * Iout + Izout6_gc * Zout_6
        Vin = Izin1_gc * Zin_1 + Zl7 + Zc20

        function_value = 10 * math.log(abs((0.5 * Zg / Zout13) * (Vout * Vout) / (Vin * Vin)), 10)
        #print("function_value", function_value, end="\n")

        if S11 < -12  and S11 > -14 and S22 < -12 and S22 > -14 and function_value > 0.0:#and S11 > -12.5
            sum += function_value
            fitness.append(function_value)
            print("function_value", function_value, end="\n")
        else:
            fitness.append(0.0)
        #print(fitness, end="\n")       #"this is fitness[]:",
        '''
    return sum / population_size


calculate_fitness()

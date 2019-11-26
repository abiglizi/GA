import random
import math
import numpy as np
import matplotlib.pyplot as plt


population_size = 1     # 种群数量


def calculate_fitness():
    sum = 0.0
    Zg = 34.6 - 2j #46.90985-5.25600j #58.0789             #41.5#48.47 - 2.084j
    Zd = 46.84 - 7.116j#48.45 - 2.7975j #33.81985-3.26500j#41.4849               #58#34.62 - 2.003j

    Zin_1 = 1.291-61.5j#5.175-43.165j  #-5.1-43.255j    #40.35-173.8j
    Zout_1 = 57.121-137.751j#27-147j#56.4 - 142.25j#56.4-142.25j#36.2-142.3j#26.05-133j    #25.96-133j   #33.5-132.2j
    Zin_2 = 1.175-61.05j#5.175-43.165j   #39.85-176j
    Zout_2 = 57.121-137.751j#53-147j#56.65 - 142.5j#56.65-142.5j#36.13-141.9j#26.05-133j   #33.53-132.2j
    Zin_3 = 1.18-61j#5.175-43.165j    #39.85-176j
    Zout_3 = 57.121-137.751j#57.5-126.5j#56.55 - 142.25j#56.55-142.25j#36.18-142.15j#26.05-133j   #33.53-132.2j
    Zin_4 = 1.175-61.1j#5.175-43.165j   #39.85-176j
    Zout_4 = 57.121-137.751j#67-140.5j#56.55 - 142.3j#56.55-142.3j#36.29-142.55j#26.05-133j  #33.53-132.2j

    #Zin = Zin_1 = Zin_2 = Zin_3 = Zin_4 = 1.175 - 61.1j
    #Zout = Zout_1 = Zout_2 = Zout_3 = Zout_4 = 56.55 - 142.3j
                                                 #gm = 0.0550
    Rx = 229958                                #RL的阻抗
    Zls = round((2 * 3.1415 * 0.01 * 20030j).imag,8)*1j            #Ls的阻抗
    Zc = 0.085855-1.5735j    #0.09015-1.6j #1.0 / (2 * 3.1415 * 0.01 * 4.43j)         #电容的阻抗
    Zc20 = -0.7957981855801j #1.0 / (2 * 3.1415 * 0.01 * 20j)      #电容的阻抗
    gm = 0.05508

    for i in range(population_size):
        Zl8 = round((2 * 3.1415 * 0.01 * 400j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][0]
        Zl7 = round((2 * 3.1415 * 0.01 * 300j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][1]
        Zl6 = round((2 * 3.1415 * 0.01 * 300j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][2]
        Zl5 = round((2 * 3.1415 * 0.01 * 300j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][3]
        Zl4 = round((2 * 3.1415 * 0.01 * 300j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][4]
        Zl3 = round((2 * 3.1415 * 0.01 * 300j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][5]
        Zl2 = round((2 * 3.1415 * 0.01 * 400j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][6]
        Zl1 = round((2 * 3.1415 * 0.01 * 500j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][7]

        zl1 = round((2 * 3.1415 * 0.01 * 1200j).imag,8)*1j     #(0.105 + 2.93j) * genetic_population[i][8]
        zl2 = round((2 * 3.1415 * 0.01 * 500j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][9]
        zl3 = round((2 * 3.1415 * 0.01 * 500j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][10]
        zl4 = round((2 * 3.1415 * 0.01 * 310j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][11]
        zl5 = round((2 * 3.1415 * 0.01 * 200j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][12]
        zl6 = round((2 * 3.1415 * 0.01 * 200j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][13]
        zl7 = round((2 * 3.1415 * 0.01 * 150j).imag,8)*1j      #(0.105 + 2.93j) * genetic_population[i][14]
        zl8 = round((2 * 3.1415 * 0.01 * 50j).imag,8)*1j       #(0.105 + 2.93j) * genetic_population[i][15]


        Zin1 = round((Zg + Zc +Zl1).real,8) + round((Zg + Zc +Zl1).imag,8)*1j
        Zin2 = round((1.0 / (1.0 / Zin_4 + 1.0 / Zin1)).real,8) + round((1.0 / (1.0 / Zin_4 + 1.0 / Zin1)).imag,8)*1j
        Zin3 = round((Zin2 + Zl2 + Zl3).real,8) + round((Zin2 + Zl2 + Zl3).imag,8)*1j
        Zin4 = round((1.0 / (1.0 / Zin_3 + 1.0 / Zin3)).real,8) + round((1.0 / (1.0 / Zin_3 + 1.0 / Zin3)).imag,8)*1j
        Zin5 = round((Zin4 + Zl4 + Zl5).real,8) + round((Zin4 + Zl4 + Zl5).imag,8)*1j
        Zin6 = round((1.0 / (1.0 / Zin_2 + 1.0 / Zin5)).real,8) + round((1.0 / (1.0 / Zin_2 + 1.0 / Zin5)).imag,8)*1j
        Zin7 = round((Zin6 + Zl6 + Zl7).real,8) + round((Zin6 + Zl6 + Zl7).imag,8)*1j
        Zin8 = round((1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rx)).real,8) + round((1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rx)).imag,8)*1j
        Zin9 = round((Zin8 + Zl8 + Zc20).real,8) + round((Zin8 + Zl8 + Zc20).imag,8)*1j

        Zout1 = round((Zd + zl1).real,8) + round((Zd + zl1).imag,8)*1j
        Zout2 = round((1.0 / (1.0 / Zout_1 + 1.0 / Zout1)).real,8) + round((1.0 / (1.0 / Zout_1 + 1.0 / Zout1)).imag,8)*1j
        Zout3 = round((Zout2 + zl2 + zl3).real,8) + round((Zout2 + zl2 + zl3).imag,8)*1j
        Zout4 = round((1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)).real,8) + round((1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)).imag,8)*1j
        Zout5 = round((Zout4 + zl4 + zl5).real,8) + round((Zout4 + zl4 + zl5).imag,8)*1j
        Zout6 = round((1.0 / (1.0 / Zout_3 + 1.0 / Zout5)).real,8) + round((1.0 / (1.0 / Zout_3 + 1.0 / Zout5)).imag,8)*1j
        Zout7 = round((Zout6 + zl6 + zl7).real,8) + round((Zout6 + zl6 + zl7).imag,8)*1j
        Zout8 = round((1.0 / (1.0 / Zout_4 + 1.0 / Zout7)).real,8) + round((1.0 / (1.0 / Zout_4 + 1.0 / Zout7)).imag,8)*1j
        Zout9 = round((Zout8 + Zc20 + zl8).real,8) + round((Zout8 + Zc20 + zl8).imag,8)*1j

        print("Zin1_9: ", Zin1, Zin2, Zin3, Zin4,Zin5, Zin6, Zin7, Zin8, Zin9)
        print("Zout1_9: ", Zout1, Zout2, Zout3, Zout4,Zout5, Zout6, Zout7, Zout8, Zout9)

        #haaa_in = (Zin9 - 50) / (Zin9 + 50)    #(abs(Zin9) - 50) / (abs(Zin9) + 50)#abs((Zin9 - 50) / (Zin9 + 50))
        #haaa_out = (50 - Zout9) / (Zout9 + 50)  #(50 - abs(Zout9)) / (abs(Zout9) + 50)#abs((50 - Zout9) / (Zout9 + 50))
        #print("haaa_in,haaa_out", haaa_in, haaa_out)

        RL1 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
        RL2 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)
        print("RL1,RL2:", RL1, RL2)

        '''
        I1 = Zin / (Zin + Zin7)
        I2 = (Zin / (Zin + Zin5)) * I1
        I3 = (Zin / (Zin + Zin3)) * I2

        Izin1_gc = Zin7 / (Zin + Zin7 + Rx)
        Izin2_gc = I1 * Zin5 / (Zin + Zin5)
        Izin3_gc = I2 * Zin3 / (Zin + Zin3)
        Izin4_gc = I3 * Zl1 / (Zin + Zl1)

        Iout4 = gm * Zout * Zin * Izin1_gc / (Zd + zl1)
        Izout3_gc = gm * Zin * Izin3_gc
        Izout2_gc = gm * Zin * Izin2_gc
        Izout1_gc = gm * Zin * Izin1_gc

        Iout = Izout1_gc + Izout2_gc + Izout3_gc + Iout4
        Vout = zl8 * Iout + gm * Izin4_gc * Zin * Zout
        Vin = Izin1_gc * Zin + Zl8

        function_value = 10 * math.log(abs((0.5 * Zg / Zout_4) * (Vout * Vout) / (Vin * Vin)), 10)
        print("function_value", function_value, end="\n")
        
        '''
        '''
        Pout = 0.5 *Zout9*Iout*Iout
        vin = 0.001
        Pin = vin*vin/Zg
        PAE = (Pin - Pout)/76.27*1000
        print("Pout,Pin,PAE",Pout,Pin,PAE,end="\n")
        '''

        I1 = Zin_1 / (Zin_1 + Zin7)
        I2 = (Zin_2 / (Zin_2 + Zin5)) * I1
        I3 = (Zin_3 / (Zin_3 + Zin3)) * I2

        Izin1_gc = Zin7 / (Zin_1 + Zin7 + Rx)
        Izin2_gc = I1 * Zin5 / (Zin_2 + Zin5)
        Izin3_gc = I2 * Zin3 / (Zin_3 + Zin3)
        Izin4_gc = I3 * Zin1 / (Zin_4 + Zin1)

        Iout4 = gm * Zout_1 * Zin_1 * Izin1_gc / (Zd + zl1)
        Izout3_gc = gm * Zin_3 * Izin3_gc
        Izout2_gc = gm * Zin_2 * Izin2_gc
        Izout1_gc = gm * Zin_1 * Izin1_gc

        Iout = Izout1_gc + Izout2_gc + Izout3_gc + Iout4
        Vout = zl8 * Iout + gm * Izin4_gc * Zin_4 * Zout_4
        Vin = Izin1_gc * Zin_1 + Zl8

        function_value = 10 * math.log(abs((0.5 * Zg / Zout9) * (Vout * Vout) / (Vin * Vin)), 10)
        print("function_value",function_value, end="\n")


    return sum / population_size


calculate_fitness()

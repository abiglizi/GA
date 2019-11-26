"""
import random
import math
import numpy as np
import matplotlib.pyplot as plt

'''
population_size = 1#800    # 种群数量
generations =400        # 迭代次数
chrom_length = 16        # 染色体长度
pc = 0.60                # 交配概率
pm = 0.05                # 变异概率

genetic_population = []  # 种群的基因编码
fitness = []             # 适应度
fitness_mean = []        # 平均适应度
optimum_solution = []    # 每次迭代的所获得的最优解



def calculate_fitness():
    sum = 0.0
    Zg = 41.5
    Zd = 58
    Zin = 6864 - 62.5j
    Zout = 1.643 - 2.04j
    gm = 0.05508
    for i in range(population_size):
        Zl8 = 2 * 3.1415 * 0.01 * 400j      #(0.105 + 2.93j) * genetic_population[i][0]
        Zl7 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][1]
        Zl6 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][2]
        Zl5 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][3]
        Zl4 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][4]
        Zl3 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][5]
        Zl2 = 2 * 3.1415 * 0.01 * 400j      #(0.105 + 2.93j) * genetic_population[i][6]
        Zl1 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][7]
        zl1 = 2 * 3.1415 * 0.01 * 1200j     #(0.105 + 2.93j) * genetic_population[i][8]
        zl2 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][9]
        zl3 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][10]
        zl4 = 2 * 3.1415 * 0.01 * 310j      #(0.105 + 2.93j) * genetic_population[i][11]
        zl5 = 2 * 3.1415 * 0.01 * 200j      #(0.105 + 2.93j) * genetic_population[i][12]
        zl6 = 2 * 3.1415 * 0.01 * 200j      #(0.105 + 2.93j) * genetic_population[i][13]
        zl7 = 2 * 3.1415 * 0.01 * 150j      #(0.105 + 2.93j) * genetic_population[i][14]
        zl8 = 2 * 3.1415 * 0.01 * 50j       #(0.105 + 2.93j) * genetic_population[i][15]


        Zin1 = Zl2 + 1.0 / (1.0 / Zin + 1.0 / (Zl1 + Zg))
        Zout1 = zl2 + 1.0 / (1.0 / Zout + 1.0 / (zl1 + Zd))
        Zin2 = Zl4 + 1.0 / (1.0 / Zin + 1.0 / (Zl3 + Zin1))
        Zout2 = zl4 + 1.0 / (1.0 / Zout + 1.0 / (zl3 + Zout1))
        Zin3 = Zl6 + 1.0 / (1.0 / Zin + 1.0 / (Zl5 + Zin2))
        Zout3 = zl6 + 1.0 / (1.0 / Zout + 1.0 / (zl5 + Zout2))
        Zin4 = Zl8 + 1.0 / (1.0 / Zin + 1.0 / (Zl7 + Zin3))
        Zout4 = zl8 + 1.0 / (1.0 / Zout + 1.0 / (zl7 + Zout3))
        #print("zin4,zout4:" ,abs(Zin4),abs(Zout4),end="\n")
'''
'''
        I1 = Zin / (Zin + Zl7 + Zin3)
        I2 = (Zin / (Zin + Zl5 + Zin2)) * I1
        I3 = (Zin / (Zin + Zl3 + Zin1)) * I2

        Izin1_gc = (Zl7 + Zin3) / (Zin + Zl7 + Zin3)
        Izin2_gc = I1 * (Zl5 + Zin2) / (Zin + Zl5 + Zin2)
        Izin3_gc = I2 * (Zl3 + Zin1) / (Zin + Zl3 + Zin1)
        Izin4_gc = I3 * Zl1 / (Zin + Zl1)

        Iout4 = gm * Zout * Zin * Izin1_gc / (Zd + zl1)
        Izout3_gc = gm * Zin * Izin3_gc
        Izout2_gc = gm * Zin * Izin2_gc
        Izout1_gc = gm * Zin * Izin1_gc

        Iout = Izout1_gc + Izout2_gc + Izout3_gc + Iout4


        Zvc1_left = Zl8
        Zvc1_right = Zin3 +Zl7
        print("Zvc1_left,Zvc1_right", abs(Zvc1_left), abs(Zvc1_right),end="\n")

        Zvc2_left = Zin4 - Zin3 + Zl6
        Zvc2_left_x = Zl7 + Zl6 + 1.0/(1.0/Zl8 + 1.0/Zin)
        Zvc2_right = Zin2 + Zl5
        print("Zvc2_left,Zvc2_right,Zvc2_left_x", abs(Zvc2_left), abs(Zvc2_right), abs(Zvc2_left_x) ,end="\n")

        Zvc3_left = Zin4 - Zin2 + Zl4
        Zvc3_left_x = Zl5 + Zl4 + 1.0 / (1.0/Zvc2_left_x + 1.0/Zin)
        Zvc3_right = Zin1 + Zl3
        print("Zvc3_left,Zvc3_right,Zvc3_left_x", abs(Zvc3_left), abs(Zvc3_right), abs(Zvc3_left_x) ,end="\n")

        Zvc4_left = Zin4 - Zin1 + Zl2
        Zvc4_left_x = Zl2 + Zl3 + 1.0 / (1.0 / Zvc3_left_x + 1.0 / Zin)
        Zvc4_right = Zl4 + Zg
        print("Zvc4_left,Zvc4_right,Zvc4_left_x", abs(Zvc4_left), abs(Zvc4_right), abs(Zvc4_left_x), end="\n")


        zvc4_right = zl8
        zvc4_left = Zout3 + zl7
        print("zvc4_left,zvc4_right", abs(zvc4_left), abs(zvc4_right),end="\n")

        zvc3_right = Zout4 - Zout3 + zl6
        zvc3_right_x = zl7 + zl6 + 1.0 / (1.0 / zl8 + 1.0 / Zout)
        zvc3_left = Zout2 + zl5
        print("zvc3_left,zvc3_right,zvc3_right_x", abs(zvc3_left), abs(zvc3_right), abs(zvc3_right_x) ,end="\n")

        zvc2_right = Zout4 - Zout2 + zl4
        zvc2_right_x = zl5 + zl4 + 1.0 / (1.0/zvc3_right_x + 1.0/Zout)
        zvc2_left = Zout1 + zl3
        print("zvc3_left,zvc3_right,zvc2_right_x", abs(zvc2_left), abs(zvc2_right), abs(zvc2_right_x), end="\n")

        zvc1_right = Zout4 - Zout1 + zl2
        zvc1_right_x = zl2 + zl3 + 1.0 / (1.0 / zvc2_right_x + 1.0 / Zout)
        zvc1_left = zl1
        print("zvc3_left,zvc3_right,zvc1_right_x", abs(zvc1_left), abs(zvc1_right), abs(zvc1_right_x), end="\n")

        haaa_in = abs((Zg - Zin4) / (Zin4 + Zg))
        haaa_out = abs((Zd - Zout4) / (Zout4 + Zd))
        RL1 = 20 * math.log(haaa_in, 10)
        RL2 = 20 * math.log(haaa_out, 10)
        print("RL1,RL2",RL1,RL2)

    return sum / population_size



calculate_fitness()




这里Zout是Zout4吗？
function_value = 10 * math.log(abs((0.5 * Zg / Zout) * (Vout * Vout) / (Vin * Vin)), 10)
Vin = Izin1_gc * Zin + Zl8
Vout = Iout * zl8 + Zout * Izout

vc1 = Izin1_gc * Zin 
vc2 = Izin1_gc * Zin 
vc3 = Izin1_gc * Zin 
vc4 = Izin1_gc * Zin 
Izout = Zout/(Zout + zl8 + (Zout3 + zl7)) * gm*vc4 + zvc3_right/(Zout + zvc3_right + (Zout2 + zl5)) * gm*vc3 * [Zout/(Zout + zl8)] 
        + zvc2_right/(Zout + zvc2_right + (Zout1 + zl3)) * gm*vc2 * [zvc3_right/(Zout + zvc3_right)] * [Zout/(Zout + zl8)]
         + zvc1_right/(Zout + zvc1_right + zl1 + Zd(！！！zd是否需要！！！)) * gm*vc1 * [zvc2_right/(Zout + zvc2_right)] * [zvc3_right/(Zout + zvc3_right)] * [Zout/(Zout + zl8)]
Iout = zl8/(Zout + zl8 + (Zout3 + zl7)) * gm*vc4 + zvc3_right/(Zout + zvc3_right + (Zout2 + zl5)) * gm*vc3 * [zl8/(Zout + zl8)] 
        + zvc2_right/(Zout + zvc2_right + (Zout1 + zl3)) * gm*vc2 * [zvc3_right/(Zout + zvc3_right)] * [zl8/(Zout + zl8)]
         + zvc1_right/(Zout + zvc1_right + zl1 + Zd(！！！zd是否需要！！！)) * gm*vc1 * [zvc2_right/(Zout + zvc2_right)] * [zvc3_right/(Zout + zvc3_right)] * [zl8/(Zout + zl8)]

'''



population_size = 1#800    # 种群数量
generations =400        # 迭代次数
chrom_length = 16        # 染色体长度
pc = 0.60                # 交配概率
pm = 0.05                # 变异概率

genetic_population = []  # 种群的基因编码
fitness = []             # 适应度
fitness_mean = []        # 平均适应度
optimum_solution = []    # 每次迭代的所获得的最优解



def calculate_fitness():
    sum = 0.0
    Zg = 41.5
    Zd = 58
    Zin = 6864 - 62.5j
    Zout = 1.643 - 2.04j
    gm = 0.05508
    Rx = 229958
    for i in range(population_size):
        Zl8 = 2 * 3.1415 * 0.01 * 400j      #(0.105 + 2.93j) * genetic_population[i][0]
        Zl7 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][1]
        Zl6 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][2]
        Zl5 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][3]
        Zl4 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][4]
        Zl3 = 2 * 3.1415 * 0.01 * 300j      #(0.105 + 2.93j) * genetic_population[i][5]
        Zl2 = 2 * 3.1415 * 0.01 * 400j      #(0.105 + 2.93j) * genetic_population[i][6]
        Zl1 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][7]
        zl1 = 2 * 3.1415 * 0.01 * 1200j     #(0.105 + 2.93j) * genetic_population[i][8]
        zl2 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][9]
        zl3 = 2 * 3.1415 * 0.01 * 500j      #(0.105 + 2.93j) * genetic_population[i][10]
        zl4 = 2 * 3.1415 * 0.01 * 310j      #(0.105 + 2.93j) * genetic_population[i][11]
        zl5 = 2 * 3.1415 * 0.01 * 200j      #(0.105 + 2.93j) * genetic_population[i][12]
        zl6 = 2 * 3.1415 * 0.01 * 200j      #(0.105 + 2.93j) * genetic_population[i][13]
        zl7 = 2 * 3.1415 * 0.01 * 150j      #(0.105 + 2.93j) * genetic_population[i][14]
        zl8 = 2 * 3.1415 * 0.01 * 500j       #(0.105 + 2.93j) * genetic_population[i][15]
        Zls = 2 * 3.1415 * 0.01 * 20030j
        Zc = 0.0019228 - 0.08621j    #1F = 10**12 pF ; 1H = 10**12 pH
        Zc20 = 1.0 / (2 * 3.1415 * 0.01 * 20j)

        Zin1 = Zl2 + 1.0 / (1.0 / Zin + 1.0 / (Zl1 + Zg + Zc))
        Zin2 = Zl4 + 1.0 / (1.0 / Zin + 1.0 / (Zl3 + Zin1))
        Zin3 = Zl6 + 1.0 / (1.0 / Zin + 1.0 / (Zl5 + Zin2))
        Zin4 = Zc20 + Zl8 + 1.0 / (1.0 / Zin + 1.0 / (Zl7 + Zin3) + 1.0/Rx)

        Zout1 = Zd + zl1 + Zc
        Zout2 = 1.0 / (1.0 / Zout + 1.0 / Zout1)
        Zout3 = Zout2 + zl2 + zl3
        Zout4 = 1.0 / (1.0 / Zout + 1.0 / Zout3 + 1.0 / Zls)
        Zout5 = Zout4 + zl4 + zl5
        Zout6 = 1.0 / (1.0 / Zout + 1.0 / Zout5)
        Zout7 = Zout6 + zl6 + zl7
        Zout8 = 1.0 / (1.0 / Zout + 1.0 / Zout7)
        Zout9 = Zout8 + zl8 + Zc20

        #print("Zin1_9", abs(Zin1), abs(Zin2), abs(Zin3), abs(Zin4), abs(Zin5), abs(Zin6), abs(Zin7), abs(Zin8), abs(Zin9))
        #print("Zout1_9", abs(Zout1), abs(Zout2), abs(Zout3), abs(Zout4), abs(Zout5), abs(Zout6), abs(Zout7), abs(Zout8), abs(Zout9))

        haaa_in = abs((Zin4 - 50) / (Zin4 + 50))
        haaa_out = abs((50 - Zout9) / (Zout9 + 50))
        RL1 = 20 * math.log(haaa_in, 10)
        RL2 = 20 * math.log(haaa_out, 10)
        print("RL1,RL2", RL1, RL2)

        '''
        Zin1 = Zl2 + 1.0 / (1.0 / Zin + 1.0 / (Zl1 + Zg))
        Zin2 = Zl4 + 1.0 / (1.0 / Zin + 1.0 / (Zl3 + Zin1))
        Zin3 = Zl6 + 1.0 / (1.0 / Zin + 1.0 / (Zl5 + Zin2))
        Zin4 = Zl8 + 1.0 / (1.0 / Zin + 1.0 / (Zl7 + Zin3))
        
        
        Zout1 = zl2 + 1.0 / (1.0 / Zout + 1.0 / (zl1 + Zd))
        Zout2 = zl4 + 1.0 / (1.0 / Zout + 1.0 / (zl3 + Zout1))
        Zout3 = zl6 + 1.0 / (1.0 / Zout + 1.0 / (zl5 + Zout2))
        Zout4 = zl8 + 1.0 / (1.0 / Zout + 1.0 / (zl7 + Zout3))
        #print("zin4,zout4:" ,abs(Zin4),abs(Zout4),end="\n")

        #Zvc1_left = Zl8
        #Zvc1_right = Zl7 +Zl6
        #print("Zvc1_left,Zvc1_right", abs(Zvc1_left), abs(Zvc1_right),end="\n")
        
        Zvc2_left = Zin4 - Zin3 + Zl6
        Zvc2_left_x = Zl7 + Zl6 + 1.0/(1.0/Zl8 + 1.0/Zin)
        Zvc2_right = Zin2 + Zl5
        print("Zvc2_left,Zvc2_right,Zvc2_left_x", abs(Zvc2_left), abs(Zvc2_right), abs(Zvc2_left_x) ,end="\n")

        Zvc3_left = Zin4 - Zin2 + Zl4
        Zvc3_left_x = Zl5 + Zl4 + 1.0 / (1.0/Zvc2_left_x + 1.0/Zin)
        Zvc3_right = Zin1 + Zl3
        print("Zvc3_left,Zvc3_right,Zvc3_left_x", abs(Zvc3_left), abs(Zvc3_right), abs(Zvc3_left_x) ,end="\n")

        Zvc4_left = Zin4 - Zin1 + Zl2
        Zvc4_left_x = Zl2 + Zl3 + 1.0 / (1.0 / Zvc3_left_x + 1.0 / Zin)
        Zvc4_right = Zl4
        print("Zvc4_left,Zvc4_right,Zvc4_left_x", abs(Zvc4_left), abs(Zvc4_right), abs(Zvc4_left_x), end="\n")


        zvc4_right = zl8
        zvc4_left = Zout3 + zl7
        print("zvc4_left,zvc4_right", abs(zvc4_left), abs(zvc4_right),end="\n")

        zvc3_right = Zout4 - Zout3 + zl6
        zvc3_right_x = zl7 + zl6 + 1.0 / (1.0 / zl8 + 1.0 / Zout)
        zvc3_left = Zout2 + zl5
        print("zvc3_left,zvc3_right,zvc3_left_x", abs(zvc3_left), abs(zvc3_right), abs(zvc3_right_x) ,end="\n")

        zvc2_right = Zout4 - Zout2 + zl4
        zvc2_right_x = zl5 + zl4 + 1.0 / (1.0/zvc3_right_x + 1.0/Zout)
        zvc2_left = Zout1 + zl3
        print("zvc3_left,zvc3_right,zvc3_left_x", abs(zvc2_left), abs(zvc2_right), abs(zvc2_right_x), end="\n")
        '''

    return sum / population_size


calculate_fitness()

"""



import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
population_size = 100
generations =100
chrom_length = 14
pc = 0.60     # 交配概率
pm = 0.05     # 变异概率

genetic_population = []
fitness = []
fitness_mean = []
optimum_solution = []


# 为染色体进行编码，生成初始种群
def chrom_encoding():
    aaaaa = 0
    for i in range(population_size):
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        A = 0
        B = 0
        C = 0
        D = 0
        E = 0
        F = 0
        G = 0
        while(a==0 or b==0 or c==0 or d==0 or e==0 or f==0 or g==0 or A==0 or B==0 or C==0 or D==0 or E==0 or F==0 or G==0):
            a = random.randint(0, 50)
            b = random.randint(0, 50 - a)
            c = random.randint(0, 50 - a - b)
            d = random.randint(0, 50 - a - b - c)
            e = random.randint(0, 50 - a - b - c - d)
            f = random.randint(0, 50 - a - b - c - d - e)
            g = 50 - a - b - c - d - e - f
            A = random.randint(0, 60)
            B = random.randint(0, 60 - A)
            C = random.randint(0, 60 - A - B)
            D = random.randint(0, 60 - A - B - C)
            E = random.randint(0, 60 - A - B - C - D)
            F = random.randint(0, 60 - A - B - C - D - E)
            G = 60 - A - B - C - D - E - F
        population_1 = [a, b, c, d, e, f, g, A, B, C, D, E, F, G]
        genetic_population.append(population_1)
        #population_2 = [A, B, C, D, E, F, G, H]
        #print(population_2, end="@@@@@@@@@\n")
        # genetic_population.append(population_2)
    for i in genetic_population:
        print(i)
    for i in range(100):
        for j in range(14):
            aaaaa = aaaaa+genetic_population[i][j]
        if aaaaa !=110:
            print(aaaaa)
        aaaaa=0

chrom_encoding()


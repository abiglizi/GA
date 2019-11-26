import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
population_size = 1200
generations =500
chrom_length = 14
pc = 0.60     # 交配概率
pm = 0.05     # 变异概率

genetic_population = []
fitness = []
fitness_mean = []
optimum_solution = []


# 为染色体进行编码，生成初始种群
def chrom_encoding():
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
            a = random.randint(0, 80)
            b = random.randint(0, 80 - a)
            c = random.randint(0, 80 - a - b)
            d = random.randint(0, 80 - a - b - c)
            e = random.randint(0, 80 - a - b - c - d)
            f = random.randint(0, 80 - a - b - c - d - e)
            g = 80 - a - b - c - d - e - f
            A = random.randint(0, 85)
            B = random.randint(0, 85 - A)
            C = random.randint(0, 85 - A - B)
            D = random.randint(0, 85 - A - B - C)
            E = random.randint(0, 85 - A - B - C - D)
            F = random.randint(0, 85 - A - B - C - D - E)
            G = 85 - A - B - C - D - E - F
        population_1 = [a, b, c, d, e, f, g, A, B, C, D, E, F, G]
        genetic_population.append(population_1)
        #population_2 = [A, B, C, D, E, F, G, H]
        #print(population_2, end="@@@@@@@@@\n")
        # genetic_population.append(population_2)
    #for i in genetic_population:
    #    print(i)

#计算每个染色体的适应度
def calculate_fitness():
    fitness.clear()
    sum = 0.0
    Zg = 50 #34.6 - 2j  # 46.90985-5.25600j #58.0789             #41.5#48.47 - 2.084j
    Zd = 50 #46.84 - 7.116j  # 48.45 - 2.7975j #33.81985-3.26500j#41.4849               #58#34.62 - 2.003j

    Zin_1 = 78.235-373.45j #69.465-369.65j
    Zout_1 = 126.8-284.95j #126.8-284.95j
    Zin_2 = 45.035-197j #38.915-192j
    Zout_2 =  78.87-127.2j #78.87-127.2j
    Zin_3 = 75.465-383.25 #66.4-377.3j
    Zout_3 = 102.65-314.35j #102.65-314.35j
    Zin_4 = 45.035-197j #39.035-192j
    Zout_4 =  58.15-158.6j #58.15-158.6j
    Zin_5 = 45.035-197j #39.055-192j
    Zout_5 = 58.15-158.6j #58.15-158.6j
    Zin_6 = 75.465-383.25j  #92.755-686j
    Zout_6 = 78.87-127.2j #200.5-653j


    Rx = 229958
    Zls = 2 * 3.1415 * 0.01 * 20030j
    Zc = 0.085855-1.5735j    #0.09015-1.6j #1.0 / (2 * 3.1415 * 0.01 * 4.43j)
    Zc20 = -0.7957981855801j #1.0 / (2 * 3.1415 * 0.01 * 20j)
    gm = 0.05508
    for i in range(population_size):
        Zl7 = 3.1415j * genetic_population[i][0]
        Zl6 = 3.1415j * genetic_population[i][1]
        Zl5 = 3.1415j * genetic_population[i][2]
        Zl4 = 3.1415j * genetic_population[i][3]
        Zl3 = 3.1415j * genetic_population[i][4]
        Zl2 = 3.1415j * genetic_population[i][5]
        Zl1 = 3.1415j * genetic_population[i][6]

        zl1 = 3.1415j * genetic_population[i][7]
        zl2 = 3.1415j * genetic_population[i][8]
        zl3 = 3.1415j * genetic_population[i][9]
        zl4 = 3.1415j * genetic_population[i][10]
        zl5 = 3.1415j * genetic_population[i][11]
        zl6 = 3.1415j * genetic_population[i][12]
        zl7 = 3.1415j * genetic_population[i][13]


        Zin1 = Zg + Zc + Zl1
        Zin2 = 1.0 / (1.0 / Zin_6 + 1.0 / Zin1)
        Zin3 = Zin2 + Zl2
        Zin4 = 1.0 / (1.0 / Zin_5 + 1.0 / Zin3)
        Zin5 = Zin4 + Zl3
        Zin6 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin5)
        Zin7 = Zin6 + Zl4
        Zin8 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin7)
        Zin9 = Zin8 + Zl5
        Zin10 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin9)
        Zin11 = Zin10 + Zl6
        Zin12 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin11 + 1.0 / Rx)
        Zin13 = Zin12 + Zl7 + Zc20

        Zout1 = Zd + zl1 + Zc
        Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
        Zout3 = Zout2 + zl2
        Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)
        Zout5 = Zout4 + zl3
        Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5)
        Zout7 = Zout6 + zl4
        Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
        Zout9 = Zout8 + zl5
        Zout10 = 1.0 / (1.0 / Zout_5 + 1.0 / Zout9)
        Zout11 = Zout10 + zl6
        Zout12 = 1.0 / (1.0 / Zout_6 + 1.0 / Zout11)
        Zout13 = Zout12 + zl7 + Zc20

        #print("Zin1_13: ", Zin1, Zin2, Zin3, Zin4, Zin5, Zin6, Zin7, Zin8, Zin9)
        #print("Zout1_13: ", Zout1, Zout2, Zout3, Zout4, Zout5, Zout6, Zout7, Zout8, Zout9)

        S11 = 20 * math.log(abs((Zin13 - 50) / (Zin13 + 50)), 10)
        S22 = 20 * math.log(abs((50 - Zout13) / (Zout13 + 50)), 10)
        print("S11,S22:", S11, S22)

        I1 = (Zin_1 + Rx) / (Zin_1 + Zin11 + Rx)
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
    return sum / population_size


def best_value():
    max_fitness = fitness[0]
    max_chrom = 0
    for x in range(population_size):
        if fitness[x] > max_fitness:
            max_fitness = fitness[x]
            max_chrom = x
    return max_chrom, max_fitness


def selection():
    new_genetic_population = []
    global genetic_population
    for i in range(population_size):
        x = random.randint(0, population_size - 1)
        y = random.randint(0, population_size - 1)
        if fitness[x] > fitness[y]:
            new_genetic_population.append(genetic_population[x])
        else:
            new_genetic_population.append(genetic_population[y])
    genetic_population = new_genetic_population


#进行交配过程
def crossover():
    for i in range(0, population_size - 1, 2):
        if random.random() < pc:
            change_point = 7  #random.randint(0, chrom_length - 1)
            #change_point = random.randint(0, chrom_length - 1)
            temp1 = []
            temp2 = []
            temp1.extend(genetic_population[i][0: change_point])
            temp1.extend(genetic_population[i + 1][change_point:])
            temp2.extend(genetic_population[i + 1][0: change_point])
            temp2.extend(genetic_population[i][change_point:])
            genetic_population[i] = temp1
            genetic_population[i + 1] = temp2

#进行基因的变异
def mutation():
    for i in range(population_size):
        if random.random() < pm:
            mutation_point_1 = random.randint(0, chrom_length - 1)
            mutation_point_2 = random.randint(0, chrom_length - 1)
            number_x = random.randint(1, 13)
            genetic_population[i][mutation_point_1] += number_x
            if (mutation_point_1 in range(8)):
                while (mutation_point_2 == mutation_point_1 or genetic_population[i][mutation_point_2] <= number_x or mutation_point_2>=8):
                    mutation_point_2 = random.randint(0, 7)
                else:
                    genetic_population[i][mutation_point_2] -= number_x
                    break
            elif (mutation_point_1 in range(8, 16)):
                while(mutation_point_2 == mutation_point_1 or genetic_population[i][mutation_point_2] <= number_x or mutation_point_2<=7):
                    mutation_point_2 = random.randint(8, 15)
                else:
                    genetic_population[i][mutation_point_2] -= number_x
                    break
'''
            while (1):
                if (mutation_point_1 in range(8)):
                    if (mutation_point_2 == mutation_point_1 or genetic_population[i][mutation_point_2] <= number_x or mutation_point_2>=8):
                        mutation_point_2 = random.randint(0, 7)
                    else:
                        genetic_population[i][mutation_point_2] -= number_x
                        break
                else:
                    if (mutation_point_2 == mutation_point_1 or genetic_population[i][mutation_point_2] <= number_x or mutation_point_2<=7):
                        mutation_point_2 = random.randint(8, 15)
                    else:
                        genetic_population[i][mutation_point_2] -= number_x
                        break

'''


start=time.clock()
chrom_encoding()
for step in range(generations):
    fit_mean = calculate_fitness()
    best_id, best_fitness = best_value()
    optimum_solution.append(best_fitness)
    fitness_mean.append(fit_mean)
    selection()
    crossover()
    #mutation()
#    if (fitness[0]> 15 and fitness[0] < 25):
#       print("XXX", genetic_population[1], end="\n")
end=time.clock()

new =[]
new2=[]
for i in range(20):
    for j in range(14):
        new.append(genetic_population[i][j]*50)
for i in range(0, len(new), 14):
    new2.append(new[i:i+14])
for i in new2:
    print(i)
for i in genetic_population:
    print(i)


print("final time =", end - start)

# 最优解随迭代次数的变化
fig1 = plt.figure(1)
plt.plot(range(1, generations + 1), optimum_solution)
plt.xlabel('迭代次数', fontproperties='SimHei')
plt.ylabel('最优解', fontproperties='SimHei')

# 平均适应度随迭代次数的变化
fig2 = plt.figure(2)
plt.plot(range(1, generations + 1), fitness_mean)
plt.xlabel('迭代次数', fontproperties='SimHei')
plt.ylabel('平均适应度', fontproperties='SimHei')
plt.show()

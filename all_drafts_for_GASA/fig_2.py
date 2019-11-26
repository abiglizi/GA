# -*- coding: utf-8 -*-
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import time
#random.seed( 100 )
population_size = 500
generations =100
chrom_length = 10
#pc = 0.60
#pm = 0.05

genetic_population = []
fitness = []
fitness_mean = []
optimum_solution = []


# 为染色体进行编码，生成初始种群
def chrom_encoding():
    for i in range(population_size):
        a = random.randint(-3, 4)
        b = random.randint(-4, 5)
        c = random.randint(-4, 5)
        d = random.randint(-4, 6)
        e = random.randint(-3, 5)
        A = random.randint(-6, 6)
        B = random.randint(-6, 6)
        C = random.randint(-3, 5)
        D = random.randint(-2, 3)
        E = random.randint(0, 3)
		
        population_1 = [a, b, c, d, e, A, B, C, D, E]
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
    Zg = 33.85-5.015j
    Zd = 46.925-6.83j

    Zin_1 = -3.669-68.703j
    Zout_1 = 27.672-147.113j#27.975-149j
    Zin_2 = 2.847-61.3j
    Zout_2 = 51.998-144.629j#42.21-132.1j
    Zin_3 = 1.878-59.295j
    Zout_3 = 55.698-127.429j#58.463-146.2955j
    Zin_4 = -0.969-61.703j
    Zout_4 = 65.14-141.421j#53.94-153.721j

    Rx = 229958
    Zls = 2 * 3.1415 * 0.01 * 20030j
    #Zc = 0.085855-1.5735j    #0.09015-1.6j #1.0 / (2 * 3.1415 * 0.01 * 4.43j)
    Zc20 = -0.7957981855801j #1.0 / (2 * 3.1415 * 0.01 * 20j)
    gm = 0.05508
    for i in range(population_size):
        Zl5 = 2 * 3.1415 * 0.01j * (400+genetic_population[i][0]*50)
        Zl4 = 2 * 3.1415 * 0.01j * (600+genetic_population[i][1]*50)
        Zl3 = 2 * 3.1415 * 0.01j * (600+genetic_population[i][2]*50)
        Zl2 = 2 * 3.1415 * 0.01j * (700+genetic_population[i][3]*50)
        Zl1 = 2 * 3.1415 * 0.01j * (500+genetic_population[i][4]*50)
        zl1 = 2 * 3.1415 * 0.01j * (1200+genetic_population[i][5]*50)
        zl2 = 2 * 3.1415 * 0.01j * (1000+genetic_population[i][6]*50)
        zl3 = 2 * 3.1415 * 0.01j * (510+genetic_population[i][7]*50)
        zl4 = 2 * 3.1415 * 0.01j * (350+genetic_population[i][8]*50)
        zl5 = 2 * 3.1415 * 0.01j * (50+genetic_population[i][9]*50)

        Zin1 = Zg + Zl1  # + Zc        #考虑Zc
        Zin2 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin1)
        Zin3 = Zin2 + Zl2
        Zin4 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin3)
        Zin5 = Zin4 + Zl3
        Zin6 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin5)
        Zin7 = Zin6 + Zl4
        Zin8 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rx)
        Zin9 = Zin8 + Zl5  # + Zc20    #考虑Zc20

        Zout1 = Zd + zl1  # 不考虑Zc，注意Zd是否包括Zc
        Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
        Zout3 = Zout2 + zl2
        Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Zls)
        Zout5 = Zout4 + zl3
        Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5)  # + 1.0/168141
        Zout7 = Zout6 + zl4
        Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
        Zout9 = Zout8 + zl5    # +Zc20      #考虑Zc20
        #print("Zin1_9: ", Zin1, Zin2, Zin3, Zin4, Zin5, Zin6, Zin7, Zin8, Zin9)
        #print("Zout1_9: ", Zout1, Zout2, Zout3, Zout4, Zout5, Zout6, Zout7, Zout8, Zout9)

        S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
        S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)
        #print("S11,S22:", S11, S22)

        #function_value = 10 * math.log(abs((0.5 * Zg / Zout9) * (Vout * Vout) / (Vin * Vin)), 10)
        function_value = 20 * math.log(2.0 * abs(1.0 / (1.0 / (Zout9+Zd) + 1.0 / (Zin9+Zg))) * gm, 10)
        #print("function_value:", function_value, end="\n")

        if S11 < -15 and S22 < -15 and function_value > 1:
        #if S11 < -10 and S11 > -13 and S22 < -10 and S22 > -13 and function_value > 10 and function_value < 15:
            sum += function_value
            fitness.append(function_value)
            #print("function_value", function_value, end="\n")
        else:
            fitness.append(0.0)
            #print(fitness, end="\n")
    return sum / population_size

def best_value():
    max_fitness = fitness[0]
    max_chrom = 0
    for x in range(population_size):
        if fitness[x] > max_fitness:
            max_fitness = fitness[x]
            max_chrom = x
    return max_chrom, max_fitness
'''
#进行选择过程(1.轮盘赌,2.锦标赛)
def selection():
    fitness_proportion = []
    fitness_sum = 0
    for i in range(population_size):
        fitness_sum += fitness[i]
    for i in range(population_size):
        fitness_proportion.append(fitness[i] / fitness_sum)
    pie_fitness = []
    cumsum = 0.0
    for i in range(population_size):
        pie_fitness.append(cumsum + fitness_proportion[i])
        cumsum += fitness_proportion[i]
    pie_fitness[-1] = 1
    random_selection = []
    for i in range(population_size):
        random_selection.append(random.random())
    random_selection.sort()        #排序
    new_genetic_population = []    # 选择新种群
    random_selection_id = 0
    global genetic_population
    for i in range(population_size):
        while random_selection_id < population_size and random_selection[random_selection_id] < pie_fitness[i]:
            new_genetic_population.append(genetic_population[i])
            random_selection_id += 1
    genetic_population = new_genetic_population

'''
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
#'''

#进行交叉过程
def crossover():
    pc1=0.9
    pc2=0.6
    for i in range(0, population_size - 1, 2):
        if fitness[i] > fitness[i + 1]:
            count = i
        else:
            count = i + 1
        if fitness[count] > fit_mean:
            pc = pc1- (pc1 - pc2) * (fitness[count] - fit_mean) / (best_fitness - fit_mean)
        else:
            pc = pc1
        if random.random() < pc:
            #'''
            change_point = random.randint(0, chrom_length - 1)
            temp1 = []
            temp2 = []
            temp1.extend(genetic_population[i][0: change_point])
            temp1.extend(genetic_population[i + 1][change_point:])
            temp2.extend(genetic_population[i + 1][0: change_point])
            temp2.extend(genetic_population[i][change_point:])
            '''
            change_point_1 = 3
            change_point_2 = 6
            temp1 = []
            temp2 = []
            temp1.extend(genetic_population[i + 1][0: change_point_1])
            temp1.extend(genetic_population[i][change_point_1:change_point_2])
            temp1.extend(genetic_population[i + 1][change_point_2:])
            temp2.extend(genetic_population[i][0: change_point_1])
            temp2.extend(genetic_population[i + 1][change_point_1:change_point_2])
            temp2.extend(genetic_population[i][change_point_2:])
            '''
            genetic_population[i] = temp1
            genetic_population[i + 1] = temp2

#进行基因的变异
def mutation():
    pm1=0.1
    pm2=0.02
    for i in range(population_size):
        if fitness[i] > fit_mean:
            pm = pm1 - ( pm1 - pm2) * (fitness[i] - fit_mean) / (best_fitness - fit_mean)
        else:
            pm = pm1
        if random.random() < pm:
            mutation_point = random.randint(0, chrom_length - 1)
            genetic_population[i][mutation_point]=random.randint(0,5)



start=time.clock()
chrom_encoding()
for step in range(generations):
    fit_mean = calculate_fitness()
    best_id, best_fitness = best_value()
    optimum_solution.append(best_fitness)
    fitness_mean.append(fit_mean)
    selection()
    crossover()
    mutation()
#    if (fitness[0]> 15 and fitness[0] < 25):
#       print("XXX", genetic_population[1], end="\n")
end=time.clock()
fact= [[0 for j in range(chrom_length)] for i in range(population_size)]
genetic_population=[[genetic_population[i][j]*50 for j in range(chrom_length)] for i in range(population_size)]
for i in range(population_size):
    fact[i][0] = genetic_population[i][0] + 400
    fact[i][1] = genetic_population[i][1] + 600
    fact[i][2] = genetic_population[i][2] + 600
    fact[i][3] = genetic_population[i][3] + 700
    fact[i][4] = genetic_population[i][4] + 500
    fact[i][5] = genetic_population[i][5] + 1200
    fact[i][6] = genetic_population[i][6] + 1000
    fact[i][7] = genetic_population[i][7] + 510
    fact[i][8] = genetic_population[i][8] + 350
    fact[i][9] = genetic_population[i][9] + 50
#for i in genetic_population:
#    print(i)
#for i in fact:
#    print(i)
#print("final time =", end - start)


# 设置X,Y轴的字体样式
my_font = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc", size=18)
# 设置输出的图片大小
figure,ax = plt.subplots(figsize=(8,6))
# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=14)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
#绘图 最优解随迭代次数的变化
fig = plt.figure(1)

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

lns1 = ax.plot(range(1, generations + 1), optimum_solution, ':k', label = '最优解')
ax2 = ax.twinx()
lns2 = ax2.plot(range(1, generations + 1), fitness_mean, '-k', label = '平均适应度')

plt.tick_params(labelsize=14)
labels = ax2.get_xticklabels() + ax2.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
# 坐标轴名称
ax.set_xlabel('迭代次数',fontproperties=my_font)
ax.set_ylabel('最优解',fontproperties=my_font)
ax2.set_ylabel('平均适应度', fontproperties=my_font)
# 合并图例
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
plt.show()



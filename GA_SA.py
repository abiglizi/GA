import random
import math
import matplotlib.pyplot as plt
import numpy as np
import time

start=time.clock()          # 监测时间

population_size = 500       # 种群数目
generations = 200           # 种群代数
chrom_length = 10           # 编码长度
genetic_population = []     # 种群个体
fitness = []                # 适应度
fitness_mean = []           # 平均适应度
optimum_solution = []

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

Rl = 229958
Ls = 2 * 3.1415 * 0.01 * 20030j
gm = 0.05508

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

# 计算每个染色体的适应度
def calculate_fitness():
    fitness.clear()
    sum = 0.0
    for i in range(population_size):
        Zl5 = 2 * 3.1415 * 0.01j * (400 + genetic_population[i][0] * 50)
        Zl4 = 2 * 3.1415 * 0.01j * (600 + genetic_population[i][1] * 50)
        Zl3 = 2 * 3.1415 * 0.01j * (600 + genetic_population[i][2] * 50)
        Zl2 = 2 * 3.1415 * 0.01j * (700 + genetic_population[i][3] * 50)
        Zl1 = 2 * 3.1415 * 0.01j * (500 + genetic_population[i][4] * 50)
        zl1 = 2 * 3.1415 * 0.01j * (1200 + genetic_population[i][5] * 50)
        zl2 = 2 * 3.1415 * 0.01j * (1000 + genetic_population[i][6] * 50)
        zl3 = 2 * 3.1415 * 0.01j * (510 + genetic_population[i][7] * 50)
        zl4 = 2 * 3.1415 * 0.01j * (350 + genetic_population[i][8] * 50)
        zl5 = 2 * 3.1415 * 0.01j * (50 + genetic_population[i][9] * 50)

        Zin1 = Zg + Zl1
        Zin2 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin1)
        Zin3 = Zin2 + Zl2
        Zin4 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin3)
        Zin5 = Zin4 + Zl3
        Zin6 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin5)
        Zin7 = Zin6 + Zl4
        Zin8 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rl)
        Zin9 = Zin8 + Zl5

        Zout1 = Zd + zl1
        Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
        Zout3 = Zout2 + zl2
        Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Ls)
        Zout5 = Zout4 + zl3
        Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5)
        Zout7 = Zout6 + zl4
        Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
        Zout9 = Zout8 + zl5

        S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
        S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)

        function_value = 20 * math.log(2.0 * abs(1.0 / (1.0 / (Zout9 + Zd) + 1.0 / (Zin9 + Zg))) * gm, 10)

        if S11 < -15 and S22 < -15 and function_value >= 8:
            sum += function_value
            fitness.append(function_value)
        else:
            fitness.append(0.0)
    return sum / population_size

# 确定适应度最好的个体
def best_value():
    max_fitness = fitness[0]
    max_chrom = 0
    for x in range(population_size):
        if fitness[x] > max_fitness:
            max_fitness = fitness[x]
            max_chrom = x
    return max_chrom, max_fitness

# 进行选择过程(锦标赛)
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

# 进行交叉过程
def crossover():
    pc1 = 0.9
    pc2 = 0.6
    for i in range(0, population_size - 1, 2):
        if fitness[i] > fitness[i + 1]:
            count = i
        else:
            count = i + 1
        if fitness[count] >= fit_mean:
            pc = pc1 - (pc1 - pc2) * (fitness[count] - fit_mean) / (best_fitness - fit_mean)
        else:
            pc = pc1
        if random.random() < pc:
            change_point = random.randint(0, chrom_length - 1)
            temp1 = []
            temp2 = []
            temp1.extend(genetic_population[i][0: change_point])
            temp1.extend(genetic_population[i + 1][change_point:])
            temp2.extend(genetic_population[i + 1][0: change_point])
            temp2.extend(genetic_population[i][change_point:])
            genetic_population[i] = temp1
            genetic_population[i + 1] = temp2

# 进行基因的变异
def mutation():
    pm1 = 0.1
    pm2 = 0.02
    for i in range(population_size):
        if fitness[i] >= fit_mean:
            pm = pm1 - (pm1 - pm2) * (fitness[i] - fit_mean) / (best_fitness - fit_mean)
        else:
            pm = pm1
        if random.random() < pm:
            mutation_point = random.randint(0, chrom_length - 1)
            genetic_population[i][mutation_point] = random.randint(0, 5)

# GA的主函数
chrom_encoding()
for step in range(generations):
    fit_mean = calculate_fitness()
    best_id, best_fitness = best_value()
    optimum_solution.append(best_fitness)
    fitness_mean.append(fit_mean)
    selection()
    crossover()
    mutation()


fact = [[0 for j in range(chrom_length)] for i in range(population_size)]
genetic_population = [[genetic_population[i][j] * 50 for j in range(chrom_length)] for i in range(population_size)]
# 类似解码，还原个体，每个x50放大
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



# ---------------------这是分割线-----------------------------



#计算增益，S11，S22
def function(list):
    Zl5 = 2 * 3.1415 * 0.01j * list[0]
    Zl4 = 2 * 3.1415 * 0.01j * list[1]
    Zl3 = 2 * 3.1415 * 0.01j * list[2]
    Zl2 = 2 * 3.1415 * 0.01j * list[3]
    Zl1 = 2 * 3.1415 * 0.01j * list[4]
    zl1 = 2 * 3.1415 * 0.01j * list[5]
    zl2 = 2 * 3.1415 * 0.01j * list[6]
    zl3 = 2 * 3.1415 * 0.01j * list[7]
    zl4 = 2 * 3.1415 * 0.01j * list[8]
    zl5 = 2 * 3.1415 * 0.01j * list[9]

    Zin1 = Zg + Zl1
    Zin2 = 1.0 / (1.0 / Zin_4 + 1.0 / Zin1)
    Zin3 = Zin2 + Zl2
    Zin4 = 1.0 / (1.0 / Zin_3 + 1.0 / Zin3)
    Zin5 = Zin4 + Zl3
    Zin6 = 1.0 / (1.0 / Zin_2 + 1.0 / Zin5)
    Zin7 = Zin6 + Zl4
    Zin8 = 1.0 / (1.0 / Zin_1 + 1.0 / Zin7 + 1.0 / Rl)
    Zin9 = Zin8 + Zl5

    Zout1 = Zd + zl1
    Zout2 = 1.0 / (1.0 / Zout_1 + 1.0 / Zout1)
    Zout3 = Zout2 + zl2
    Zout4 = 1.0 / (1.0 / Zout_2 + 1.0 / Zout3 + 1.0 / Ls)
    Zout5 = Zout4 + zl3
    Zout6 = 1.0 / (1.0 / Zout_3 + 1.0 / Zout5)
    Zout7 = Zout6 + zl4
    Zout8 = 1.0 / (1.0 / Zout_4 + 1.0 / Zout7)
    Zout9 = Zout8 + zl5

    S11 = 20 * math.log(abs((Zin9 - 50) / (Zin9 + 50)), 10)
    S22 = 20 * math.log(abs((50 - Zout9) / (Zout9 + 50)), 10)
    function_value = 20 * math.log(2.0 * abs(1.0 / (1.0 / (Zout9 + Zd) + 1.0 / (Zin9 + Zg))) * gm, 10)
    return function_value,S11,S22


initT = 10000           # 初始温度
minT = 0.001            # 终止温度
iterL = 80              # 内循环次数
eta = 0.99              # 降温系数
x_new =[]               # 存放产生的新的数组
GAIN=[]                 # 增益
OUTCOME=[]              # 输出的结果

x_old =fact[population_size-1]
genetic_population_new = []
genetic_population_temp = []
t = initT
count=0                 # 用来绘图，确定迭代次数

print("初始增益：",function(x_old)[0],"初始S11:",function(x_old)[1],"初始S22:",function(x_old)[2],"\n")
while t > minT:
    for i in range(iterL):
        value_old = function(x_old)[0]
        flag = True
        while flag:
            genetic_population_temp = [(50 * random.randint(-1, 1)) for i in range(chrom_length)]
            genetic_population_new=np.array(genetic_population_temp)+np.array(x_old)
            genetic_population_temp.clear()
            if max(genetic_population_new) >1000 or min(genetic_population_new)<=0:
                flag=True
            else:
                S11 = function(genetic_population_new)[1]
                S22 = function(genetic_population_new)[2]
                if S11 < -15.3 and S22 < -15.3:
                    x_new = genetic_population_new     # x_old #需要变化，赋给新列表
                    flag = False
                else:
                    flag = True

        value_new = function(x_new)[0]
        res = value_new - value_old      #1y_new>y_old;2math.exp(-(y_old-y_new)/T)>random.random()
        if res > 0:
            x_old = x_new
            GAIN.append(value_new)
            OUTCOME.append(x_new)
            count+=1
        elif math.exp(res / t) > random.random():
            x_old = x_new
    t = t*eta


print("SA最大增益：",max(GAIN))
print("SA结果：",OUTCOME[GAIN.index(max(GAIN))])
print(function(OUTCOME[GAIN.index(max(GAIN))]),"\n")

end=time.clock()
print(end-start)


# GA最优解随迭代次数的变化
fig1 = plt.figure(1)
plt.plot(range(1, generations + 1), optimum_solution)
plt.xlabel('GA迭代次数', fontproperties='SimHei')
plt.ylabel('GA最优解', fontproperties='SimHei')

# GA平均适应度随迭代次数的变化
fig2 = plt.figure(2)
plt.plot(range(1, generations + 1), fitness_mean)
plt.xlabel('GA迭代次数', fontproperties='SimHei')
plt.ylabel('GA平均适应度', fontproperties='SimHei')
plt.show()

# SA最优解随迭代次数的变化
fig3 = plt.figure(3)
plt.plot(range(1, count + 1), GAIN)
plt.xlabel('SA迭代次数', fontproperties='SimHei')
plt.ylabel('SA增益值', fontproperties='SimHei')
plt.show()
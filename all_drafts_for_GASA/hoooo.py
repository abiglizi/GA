import random
import math
import numpy as np
import matplotlib.pyplot as plt

population_size = 500  # 种群数量
generations = 500  # 迭代次数
chrom_length = 16  # 染色体长度
pc = 0.65  # 交配概率
pm = 0.01  # 变异概率

genetic_population = []  # 种群的基因编码
fitness = []  # 适应度
fitness_mean = []  # 平均适应度
optimum_solution = []  # 每次迭代的所获得的最优解


# 为染色体进行编码，生成初始种群
def chrom_encoding():
    for i in range(population_size):
        a = random.randint(1, 49)
        b = random.randint(1, 56 - a )
        c = random.randint(1, 56 - a - b )
        d = random.randint(1, 56 - a - b - c)
        e = random.randint(1, 56 - a - b - c - d)
        f = random.randint(1, 56 - a - b - c - d - e)
        g = random.randint(1, 56 - a - b - c - d - e - f)
        h = 56 - a - b - c - d - e - f - g
        A = random.randint(1, 62)
        B = random.randint(1, 62 - A)
        C = random.randint(1, 62 - A - B)
        D = random.randint(1, 62 - A - B - C)
        E = random.randint(1, 62 - A - B - C - D)
        F = random.randint(1, 62 - A - B - C - D - E)
        G = random.randint(1, 62 - A - B - C - D - E - F)
        H = 62 - A - B - C - D - E - F - G
        population_1 = [a, b, c, d, e, f, g, h, A, B, C, D, E, F, G, H]

        # population_2 = [A,B,C,D,E,F,G,H]
        genetic_population.append(population_1)  # 这种正确
        # genetic_population.append(population_2)	#采用这种不正确，追加后称为二维数组
    for i in genetic_population:
        print(i)

# 计算每个染色体的适应度
def calculate_fitness():
    fitness.clear()
    sum = 0.0
    Zg = 41.5
    Zd = 58
    Zin = 6864 - 62.5j
    Zout = 1.643 - 2.04j
    gm = 0.05508
    for i in range(population_size):
        Lin8 = 50 * genetic_population[i][0] * (10 ** -12)
        Lin7 = 50 * genetic_population[i][1] * (10 ** -12)
        Lin6 = 50 * genetic_population[i][2] * (10 ** -12)
        Lin5 = 50 * genetic_population[i][3] * (10 ** -12)
        Lin4 = 50 * genetic_population[i][4] * (10 ** -12)
        Lin3 = 50 * genetic_population[i][5] * (10 ** -12)
        Lin2 = 50 * genetic_population[i][6] * (10 ** -12)
        Lin1 = 50 * genetic_population[i][7] * (10 ** -12)
        Lout1 = 50 * genetic_population[i][8] * (10 ** -12)
        Lout2 = 50 * genetic_population[i][9] * (10 ** -12)
        Lout3 = 50 * genetic_population[i][10] * (10 ** -12)
        Lout4 = 50 * genetic_population[i][11] * (10 ** -12)
        Lout5 = 50 * genetic_population[i][12] * (10 ** -12)
        Lout6 = 50 * genetic_population[i][13] * (10 ** -12)
        Lout7 = 50 * genetic_population[i][14] * (10 ** -12)
        Lout8 = 50 * genetic_population[i][15] * (10 ** -12)
        Zl8 = 2j * 3.14 * 10 ** 10 * Lin8  # 大写的Z表示输入方向
        Zl7 = 2j * 3.14 * 10 ** 10 * Lin7
        Zl6 = 2j * 3.14 * 10 ** 10 * Lin6
        Zl5 = 2j * 3.14 * 10 ** 10 * Lin5
        Zl4 = 2j * 3.14 * 10 ** 10 * Lin4
        Zl3 = 2j * 3.14 * 10 ** 10 * Lin3
        Zl2 = 2j * 3.14 * 10 ** 10 * Lin2
        Zl1 = 2j * 3.14 * 10 ** 10 * Lin1
        zl1 = 2j * 3.14 * 10 ** 10 * Lout1  # 小写的z表示输出方向
        zl2 = 2j * 3.14 * 10 ** 10 * Lout2
        zl3 = 2j * 3.14 * 10 ** 10 * Lout3
        zl4 = 2j * 3.14 * 10 ** 10 * Lout4
        zl5 = 2j * 3.14 * 10 ** 10 * Lout5
        zl6 = 2j * 3.14 * 10 ** 10 * Lout6
        zl7 = 2j * 3.14 * 10 ** 10 * Lout7
        zl8 = 2j * 3.14 * 10 ** 10 * Lout8

        Zin1 = Zl2 + 1.0 / (1 / Zin + 1 / (Zl1 + Zg))
        Zout1 = zl2 + 1.0 / (1 / Zout + 1 / (zl1 + Zd))
        Zin2 = Zl4 + 1.0 / (1 / Zin + 1 / (Zl3 + Zin1))
        Zout2 = zl4 + 1.0 / (1 / Zout + 1 / (zl3 + Zout1))
        Zin3 = Zl6 + 1.0 / (1 / Zin + 1 / (Zl5 + Zin2))
        Zout3 = zl6 + 1.0 / (1 / Zout + 1 / (zl5 + Zout2))
        Zin4 = Zl8 + 1.0 / (1 / Zin + 1 / (Zl7 + Zin3))
        Zout4 = zl8 + 1.0 / (1 / Zout + 1 / (zl7 + Zout3))

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
        Vout = zl8 * Iout + gm * Izin4_gc * Zin
        Vin = Izin1_gc * Zin + Zl8
        function_value = 10 * math.log(abs((0.5 * Zg / Zout) * (Vout * Vout) / (Vin * Vin)), 10)

        # print(function_value,end="!!!!!\n")
        haaa_in = abs((Zin4 - Zg) / (Zin4 + Zg))
        haaa_out = abs((Zout4 - Zd) / (Zin4 + Zd))
        # print(haaa_in,haaa_out,end="#####\n")
        RL1 = 20 * math.log(haaa_in, 10)
        RL2 = 20 * math.log(haaa_out, 10)
        # print(RL1, RL2,end="&&&&&\n")
        if function_value > 0.0 and RL2 < -10 and RL1 < -1:  # and RL1 < -10 and RL2 < -10:
            sum += function_value
            fitness.append(function_value)
        else:
            fitness.append(0.0)
        print(fitness)
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


# 进行交配过程
def crossover():
    for i in range(0, population_size - 1, 2):
        if random.random() < pc:
            # 随机选择交叉点
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
    for i in range(population_size):
        if random.random() < pm:
            mutation_point = random.randint(0, chrom_length - 1)
            genetic_population[i][mutation_point] += random.randint(0, 5)


for step in range(generations):
    chrom_encoding()
    fit_mean = calculate_fitness()
    best_id, best_fitness = best_value()
    optimum_solution.append(best_fitness)
    fitness_mean.append(fit_mean)
    selection()
    crossover()
    mutation()

for i in genetic_population:
    print(i)

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

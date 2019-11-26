import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import math
import random
import time
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

    Rl = 229958
    Ls = 2 * 3.1415 * 0.01 * 20030j
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

start=time.clock()

initT = 10000
minT = 0.001
iterL = 80
eta = 0.99
chrom_length = 10
x_new =[]
t = initT
x_old =[250, 850, 550, 500, 400, 900, 700, 760, 600, 200]
genetic_population_new = []
genetic_population_x = []
fitness=[]
fitness_x=[]
print("初始：",function(x_old),"\n")
count=0


while t > minT:
    for i in range(iterL):
        value_old = function(x_old)[0]
        flag = True
        while flag:
            genetic_population_x = [(50 * random.randint(-1, 1)) for i in range(chrom_length)]
            genetic_population_new=np.array(genetic_population_x)+np.array(x_old)
            genetic_population_x.clear()
            if max(genetic_population_new) >1200 or min(genetic_population_new)<=0:
                flag=True
            else:
                value=function(genetic_population_new)[0]
                S11 = function(genetic_population_new)[1]
                S22 = function(genetic_population_new)[2]
                if S11 < -10 and S22 < -10 and value >1:
                    x_new = genetic_population_new     # x_old #需要变化，赋给新列表
                    flag = False
                else:
                    flag = True

        value_new = function(x_new)[0]
        res = value_new - value_old      #1y_new>y_old;2math.exp(-(y_old-y_new)/T)>random.random()
        if res > 0:
            x_old = x_new
            fitness.append(value_new)
            fitness_x.append(x_new)
            count+=1
        elif math.exp(res / t) > random.random():
            x_old = x_new
    t = t*eta


end=time.clock()
print("最大增益：",max(fitness))
print("结果：",fitness_x[fitness.index(max(fitness))])
print(function(fitness_x[fitness.index(max(fitness))]),"\n")
print("final time:",end - start)


my_font = fm.FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc", size=18)
figsize = 8,6
figure, ax = plt.subplots(figsize=figsize)
# 设置坐标刻度值的大小以及刻度值的字体
plt.tick_params(labelsize=14)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

fig = plt.figure(1)
plt.plot(range(1, count + 1), fitness)
plt.xlabel('迭代次数', fontproperties=my_font)
plt.ylabel('增益值', fontproperties=my_font)
plt.show()
import random
import numpy as np
genetic_population_new=[]
x_old = [400, 850, 700, 500, 450, 900, 700, 760, 600, 200]
genetic_population_x=[]
'''
for x in range(20):
    genetic_population_new = []
    for i in range(10):
        genetic_population_new.append(50 * random.randint(-1, 1))
        genetic_population_new[i] = genetic_population_new[i] + x_old[i]
    print(x,genetic_population_new)
'''

genetic_population_x = [(50 * random.randint(-1, 1)) for i in range(10)]
genetic_population_new = np.array(genetic_population_x)+np.array(x_old)
print(genetic_population_x)

genetic_population_x.clear()

print("haaa",genetic_population_new)
print("///",genetic_population_x)
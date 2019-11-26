"""
from scipy.optimize import fsolve

def f(x):
    x = float(x[0])
    y = float(x[1])
    return[
        (33.91 + 26.55j) * (x + y * 1j) / ((33.91 + x) + (26.55 + y) * 1j) - 43.51 + 19.64j,

    ]


result = fsolve(f , [ 1,1 ])

print(result)
#print(f(result))
"""


from sympy import *
import math
import numpy as np

x = Symbol('x', real=True)  #, real=True
y = Symbol('y', real=True)  #, real=True

print(solve(1.0/(x-148.5j) +1.0/(88.74295+106.41740j) -1.0/(143.6-24.81j) , x))
#print(solve(  [-1j*y + 1.53937299277285 - 43.5515064024815j - x, 1j*x - 43.5515064024815 - 1.53937299277285j-y] , [x,y]))
#(33.91 + 26.55j)*(x +y*1j)  (33.91 + x)*(26.55 + y)*1j      43.51-19.64j

#print( solve( (47 + 68.54j)*(x +y*1j) / ( (47 + x)+(68.54 + y)*1j ) -104.1 - 44.51j, x) )
#print( solve( (47 + 68.54j)*(x +y*1j) / ( (47 + x)+(68.54 + y)*1j ) -104.1 - 44.51j, y) )

#print(solve(  [-1j*y + 30.3678042469029 - 148.813409175953j - x, 1j*x - 148.813409175953 - 30.3678042469029j-y] , [x,y]))
#(47 + 68.54j)*(x +y*1j)  (47 + x)+(68.54 + y)*1j       104.1-44.51j

#print( solve( (47 + 68.54j)*(x +y*1j) / ( (47 + x)+(68.54 + y)*1j ) -104.1 - 44.51j, [x,y]) )


#(90.28 - 15.54j)*(30.37 - 128.81j)  (90.28-15.54j+30.37-148.81j)       104.1-44.51j
#(43.51 + 24.36j)*(1.54-43.55j)  (45.05-19.19j)




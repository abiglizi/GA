import matplotlib.pyplot as plt
import numpy as np
#import multipolyfit as mpf#.multipolyfit





'''
data = [[1,1],[4,3],[8,3],[11,4],[10,7],[15,11],[16,12]]
x, y = zip(*data)
plt.plot(x, y, 'kx')

stacked_x = numpy.array([x,x+1,x-1])
coeffs = mpf(stacked_x, y, deg)
x2 = numpy.arange(min(x)-1, max(x)+1, .01) #use more points for a smoother plot
y2 = numpy.polyval(coeffs, x2) #Evaluates the polynomial for each x2 value
plt.plot(x2, y2, label="deg=3")
'''

#x = [[1,2,3,4,5], [2,2,4,4,5], [2,2,4,4,1]]
#y = [1,2,3,4,5]


# 定义x、y散点坐标
x = [10, 20, 30, 40, 50, 60, 70, 80]   #[[1,2,3,4,5], [2,2,4,4,5], [2,2,4,4,1]]
x = np.array(x)
print('x is :\n', x)
y = [174, 236, 305, 334, 349, 351, 342, 323]  #[1,2,3,4,5]
y = np.array(y)
print('y is :\n', y)

# 用3次多项式拟合
f1 = np.polyfit(x, y, 1)
print('f1 is :\n', f1)


p1 = np.poly1d(f1)
print('p1 is :\n', p1)

# 也可使用yvals=np.polyval(f1, x)
yvals = p1(x)  # 拟合y值
print('yvals is :\n', yvals)

# 绘图
plot1 = plt.plot(x, y, 's', label='original values')
plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=4)  # 指定legend的位置右下角
plt.title('polyfitting')
plt.show()








'''
x = np.arange(1, 17, 1)
y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
z1 = np.polyfit(x, y, 3) # 用3次多项式拟合
p1 = np.poly1d(z1)
print(p1) # 在屏幕上打印拟合多项式
yvals=p1(x) # 也可以使用yvals=np.polyval(z1,x)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4) # 指定legend的位置,读者可以自己help它的用法
plt.title('polyfitting')
plt.show()
'''
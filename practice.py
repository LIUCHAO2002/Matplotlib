from multiprocessing import Condition
import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import axes3d
from numpy import linspace
fig = plt.figure()  
ax3 = plt.axes(projection='3d')
def mainformula(x,y):
    z = np.zeros_like(x)
    condition1 = np.logical_and(x >= 0,x<100)
    #z[condition1] = -0.0004*np.square(x[condition1]) - 0.000256*np.square(y[condition1]-50)+1
    z[condition1]=pow((math.e)*(1/np.sqrt(2*math.pi)),-((x[condition1])**2+(y[condition1]-50)**2)/100)*5
    # now do it in the range where subformula 2 is valid
    #condition2 = np.logical_and(x>=90, x<110)
    #z[condition2] = -0.011670231880692712*x[condition2]+1.1670231880692712
    condition3 = np.logical_and(x >= 100, x<=200)
    z[condition3]=-pow((math.e)*(1/np.sqrt(2*math.pi)),-((x[condition3]-200)**2+(y[condition3]-50)**2)/100)*5
    return z
#定义三维数据
x=linspace(0,200,200)
y=linspace(0,100,100)
X, Y = np.meshgrid(x, y)
Z=mainformula(X,Y)
#作图
ax3.plot_surface(X,Y,Z,rstride = 1, cstride = 1,cmap='rainbow')
ax3.contour(X,Y,Z,offset=-4.8, cmap = 'rainbow')#绘制等高线
plt.show()

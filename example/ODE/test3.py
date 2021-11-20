# -*- codeing = utf-8 -*-
# @Time : 2021/3/13 14:32
# @Author : lzf
# @File : test3.py
# @Software :PyCharm
from scipy.integrate import odeint
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
def lorenz(w,t): #定义微分方程组
	sigma=10;rho=28;beta=8/3
	x,y,z=w
	return np.array([sigma*(y-x),rho*x-y-x*z,x*y-beta*z])
t=np.arange(0,50,0.01) #建立自变量序列（也就是时间点）
sol1=odeint(lorenz, [0.0,1.0,0.0],t) #第一个初值问题求解
sol2=odeint(lorenz,[0.0,1.001,0.0],t) #第二个初值问题求解
#画图代码 （可忽略）
plt.rc('font',size=16); plt.rc('text',usetex=False)
#第一个图的各轴的定义
ax1=plt.subplot(121,projection='3d')
ax1.plot(sol1[:,0],sol1[:,1],sol1[:,2],'r')
ax1.set_xlabel('$x$');ax1.set_ylabel('$y$');ax1.set_zlabel('$z$')
ax2=plt.subplot(122,projection='3d')
ax2.plot(sol1[:,0]-sol2[:,0],sol1[:,1]-sol2[:,1],
		 sol1[:,2]-sol2[:,2],'g')
ax2.set_xlabel('$x$');ax2.set_ylabel('$y$');ax2.set_zlabel('$z$')
plt.show()
print("sol1=",sol1,'\n\n',"sol1-sol2=",sol1-sol2)

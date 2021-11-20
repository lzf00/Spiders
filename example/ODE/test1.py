# -*- codeing = utf-8 -*-
# @Time : 2021/3/13 13:48
# @Author : lzf
# @File : test1.py
# @Software :PyCharm
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import arange
dy=lambda y,x: -2*y+x**2+2*x #lambda匿名函数
x=arange(1,10.1,0.1)
sol=odeint(dy,2,x)  #函数名，y0数列，初始x
print("x={}\n对应的数值解y={}".format(x,sol.T))   #.format()
print('x={}\n 对应的数值解y={}'.format(x,sol.T),1)
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.plot(x,sol,color="green", linewidth=1.0, linestyle="-")
plt.show()


# import numpy as np
# mat= np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# print('mat=',mat)
# print('删除第0行：',np.delete(mat,0,axis=0))
# print('删除第0列：',np.delete(mat,0,axis=1))


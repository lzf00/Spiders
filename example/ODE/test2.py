# -*- codeing = utf-8 -*-
# @Time : 2021/3/13 14:02
# @Author : lzf
# @File : test2.py
# @Software :PyCharm
from scipy.integrate import odeint
from sympy.abc import t
import numpy as np
import matplotlib.pyplot as plt
#https://blog.csdn.net/weixin_45870904/article/details/113080181?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.baidujs&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.baidujs
#定义一个方程组（微分方程组）
def pfun(y,x):
	y1,y2=y; #让'y'成为一个[y1',y2']的向量 所以将等式左边都化为1阶微分是很重要的
	return np.array([y2,-2*y1-2*y2]) #返回的是等式右边的值
x=np.arange(0,10,0.1) #创建自变量序列
soli=odeint(pfun,[0.0,1.0],x) #求数值解
plt.rc('font',size=16,family='SimHei')#; plt.rc('font',family='SimHei')
plt.plot(x,soli[:,0],'r*',label="数值解")
plt.plot(x,np.exp(-x)*np.sin(x),'g',label="符号解曲线")
plt.legend(['red','green'])  #给图像加上图例
plt.show()

# b = np.arange(5)
# plt.plot(b,b*1.0,'g.-',b,b*1.5,'rx',b,b*2.0, 'b-')  #三种画图格式
# plt.show()


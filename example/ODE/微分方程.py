# -*- codeing = utf-8 -*-
# @Time : 2021/3/11 21:15
# @Author : lzf
# @File : 微分方程.py
# @Software :PyCharm
# https://www.bilibili.com/video/BV1tb411G72z
#小球摆动模型
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
g=9.8
L=2
mu=0.1

theta0=np.pi/3  #  初始θ=60 degrees
theta_dot0=0  #initial  角速度 θ‘ =0
#definition of ODE常微分方程
def get_theta_double_dot(theta,theta_dot):  #θ的二阶导
    return -mu*theta_dot-(g/L)*np.sin(theta)

#Solution to the differential equation
t1=[]
t2=[]
def theta(t):
    #Initialize changing values
    theta=theta0
    theta_dot=theta_dot0
    delta_t=0.01  #some time step
    for time in np.arange(0,t,delta_t):
        theta_double_dot=get_theta_double_dot(theta,theta_dot)

        theta+=theta_dot*delta_t
        theta_dot+=theta_double_dot*delta_t
        t1.append(theta)
        t2.append(theta_dot)

    return theta

print(theta(10))
t=np.arange(0,10,0.01)
plt.plot(t, t1, color='red')  #时间t和角度θ

plt.plot(t1, t2, color='orange')  #角度θ和角速度θ’
my_x_ticks = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2,  0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
xticklabes = ['-2π', '-3π/2', '-π', '-π/2', 0, 'π/2', 'π', '3π/2', '2π' ]
my_y_ticks = np.arange(-3, 3, 1)
plt.xticks(my_x_ticks, xticklabes, size=14, color='grey')
plt.yticks(my_y_ticks)
plt.grid()
plt.show()





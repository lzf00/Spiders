# -*- codeing = utf-8 -*-
# @Time : 2021/3/17 22:01
# @Author : lzf
# @File : num_time.py
# @Software :PyCharm
import csv
import pandas as pd
import time, hashlib
from selenium import webdriver
import time
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
d = pd.read_csv('C:/Users\Lzf\Desktop/all_微博\weibo1\weibo_No5511008040_2.csv', usecols=['time'])#pandas读文件某一列
#print(d)
num0=[]
num1=[]
num2=[]
num3=[]
for x in d['time']:
    #print(x)
    #num.append ( x )
    if (x[0:4]=='1月4日'):
        num1.append(x)
        #print(x)
    if (x[0:4]=='1月5日'):
        num2.append(x)
        #print(x)
    if (x[0:4]=='1月6日'):
        num3.append(x)
        #print(x)
print('num1,2,3:::',len(num1),len(num2),len(num3))
#n0,n1,n2,n3,n4,n5,n6,n7,n8=[0,0,0,0,0,0,0,0,0]
N=[0 for x in range(0,24)]
print(N)
print(len(N))
a=12
for x in range(0,48,2):  #步长为2
    for i in num1:
    # print('时钟：：：',i[-5:-3])
    # print('分钟：：：',i[-2:])
        if ((int ( i[-5:-3] ) == a) and (int ( i[-2:] ) < 31)):  # 从12：00到12：31
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N[x] = N[x] + 1
        if ((int(i[-5:-3])==a) and (30<int(i[-2:])<60)):  #从12：31到13：00
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N[x+1] = N[x+1] + 1
    a=a+1
print(N)
print(sum(N))

N1=[0 for x in range(0,48)]
print(N1)
print(len(N1))
a1=0
for x in range(0,48,2):  #步长为2
    for i in num2:

        if ((int ( i[-5:-3] ) == a1) and (int ( i[-2:] ) < 31)):  # 从12：00到12：31
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N1[x] = N1[x] + 1
        if ((int(i[-5:-3])==a1) and (30<int(i[-2:])<60)):  #从12：31到13：00
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N1[x+1] = N1[x+1] + 1
    a1=a1+1
print(N1)
print(sum(N1))

N2=[0 for x in range(0,48)]
print(N2)
print(len(N2))
a2=0
for x in range(0,48,2):  #步长为2
    for i in num3:

        if ((int ( i[-5:-3] ) == a2) and (int ( i[-2:] ) < 31)):  # 从12：00到12：31
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N2[x] = N2[x] + 1
        if ((int(i[-5:-3])==a2) and (30<int(i[-2:])<60)):  #从12：31到13：00
            #print ( '时钟：：：', i[-5:-3],'分钟：：：', i[-2:]  )
            N2[x+1] = N2[x+1] + 1
    a2=a2+1
print(N2)
print(sum(N2))

for i in range(1,25):
   num0.append(sum(N[0:i]))
print(num0)
print('num0:::',len(num0))

for i in range(1,49):
   num0.append(sum(N1[0:i]))
for i in range(24,72):
    num0[i]+=689
print(num0)
print('num0:::',len(num0))

for i in range(1,49):
   num0.append(sum(N2[0:i]))
for i in range(72,120):
    num0[i]+=758
print(num0)
print('num0:::',len(num0))

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.title('显示中文标题')
plt.xlabel("横坐标")
plt.ylabel("纵坐标")
t=np.arange(0,60,1)
plt.plot(t, num0[0:120:2], color='red',label='1h',marker='o',markersize=4)  #切片，只取偶数位置的值,即间隔一个小时
t=np.arange(0,120,1)
plt.plot(t, num0[0:120:1], color='blue',label='0.5h',marker = "x",markersize=4)  #所有值，间隔半个小时
#plt.legend(["red","Blue"])  #给图像加图例
plt.grid()#添加网格
plt.show()


#X_1, X_0 = X_train[y_train == 1], X_train[y_train == -1]
# plt.plot(X_1[:, 0], X_1[:, 1], "ro")
# plt.plot(X_0[:, 0], X_0[:, 1], "bo")
# plt.show()
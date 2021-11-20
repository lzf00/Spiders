# -*- codeing = utf-8 -*-
# @Time : 2020/9/30 19:59
# @Author : lzf
# @File : rls.py
# @Software :PyCharm
import matplotlib.pyplot as plt
import math
from pylab import *
import numpy as np
import pandas as pd
import csv

filename = 'Network.csv'
with open ( filename, encoding='utf-8' ) as f:
    reader = csv.reader ( f )
    header_row = next ( reader )

    net = []
    for row in reader:
        idnet = float ( row[0] )
        num = row[1]
        a = float ( row[2] )
        rls = a   #rls第二层与第一层之比
        h = float ( row[3] )
        Authenticity = str ( row[4] )
        distance = float ( row[5] )    #节点对的距离？？？
        new = {'net_id': idnet, 'num': num, 'rls': rls, 'h': h, 'Authenticity': Authenticity, 'p': 0, 'Distance': distance}
        net.append ( new )

    data = pd.read_csv ( r'Network.csv' )
    data1 = data['rls']  # 获取名字为flow列的数据
    data_list = data1.values.tolist ()  # 将csv文件中flow列中的数据保存到列表中
    #print ( data_list )

    a = pd.Series ( data_list )
    b = a.value_counts ()
    x = list ( b.index )
    y=[0 for i in range(0,len(x)-2) ]
    for i in x:
        if 0<i<0.1:
          y[0]=y[0]+1
        elif i<0.2:
          y[1]=y[1]+1
        elif i < 0.3:
          y[2] = y[2] + 1
        elif i < 0.4:
          y[3] = y[3] + 1
        elif i < 0.5:
          y[4] = y[4] + 1
        elif i < 0.6:
          y[5] = y[5] + 1
        elif i < 0.7:
          y[6] = y[6] + 1
        elif i < 0.8:
          y[7] = y[7] + 1
        elif i<0.9:
          y[8] = y[9]+1
        elif i<1.0:
          y[9] = y[9]+1
        elif i<1.1:
          y[10]=y[10]+1
        elif i < 1.2:
          y[11] = y[11] + 1
        # elif i < 1.3:
        #   y[12] = y[12] + 1
    #x1 = [0.05,0.15,0.25,0.35,0.45,0.55,0.65,0.75,0.85,0.95,1.05,1.15,1.25]
    x1=[0 for i in range(0,12) ]
    for i in range(0,12):
        x1[i]=0.05+i*0.1
    # x1= [log10(c0) for c0 in x]
    print ( x1 )

    y1 = [c / len(x) for c in y]
    print ( y1 )

    rls1 = np.array ( x1 )
    p1 = np.array ( y1 )

 #------------------------------------------------------------------

    data3 = pd.read_csv( r'Network1.csv' )
    data4 = data3['rls']  # 获取名字为rls列的数据
    data_list1 = data4.values.tolist ()  # 将csv文件中rls列中的数据保存到列表中
    # print ( data_list )

    e = pd.Series ( data_list1 )
    f = e.value_counts ()
    l = list ( f.index )
    m = [0 for i in range ( 0, 12)]
    for i in l:
        if 0<i < 0.1:
            m[0] = m[0] + 1
        elif i < 0.2:
            m[1] = m[1] + 1
        elif i < 0.3:
            m[2] = m[2] + 1
        elif i < 0.4:
            m[3] = m[3] + 1
        elif i < 0.5:
            m[4] = m[4] + 1
        elif i < 0.6:
            m[5] = m[5] + 1
        elif i < 0.7:
            m[6] = m[6] + 1
        elif i < 0.8:
            m[7] = m[7] + 1
        elif i < 0.9:
            m[8] = m[9] + 1
        elif i < 1.0:
            m[9] = m[9] + 1
        elif i < 1.1:
            m[10] = m[10] + 1
        elif i < 1.2:
            m[11] = m[11] + 1
        # elif i < 1.3:
        #     m[12] = m[12] + 1

    l1 = [0 for i in range ( 0, 12 )]
    for i in range ( 0, 12 ):
        l1[i] = 0.05 + i * 0.1

    #l1 = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95, 1.05, 1.15, 1.25,1.35]
    print ( l1 )

    m1 = [c1 / len(l) for c1 in m]
    print ( m1 )

    rls11 = np.array ( l1 )
    p11 = np.array ( m1 )

plt.plot ( rls1, y1, color='red',marker='o' )
plt.plot ( rls11, p11, color='green',marker='o')
plt.xlabel('Ratio of layer sizes')
plt.ylabel('Probability')
plt.title('RLSP')
plt.show()

'''
# x轴用来绘图的真实数据点
x_values = [0,100,200,300]
# y轴用来绘图的真实数据点，同时，它们也是给人看的数字
y_values =[12,33,10,1000]
# x轴给人看的数字,第0个元素0是纯粹用来占位的，我只是随便选了个0，你写什么都可以
x_values_for_show = [0,8,64,512,998]
# 这一步的设置的第一个参数是x轴真实数据点，第二个参数是x轴给人看的数据点，
# 这样设置之后它们俩就存在一个一一对应的关系了
# 我们看到的不均匀的8,64,512背后是均匀的0,100,200，其实不过是一个障眼法
plt.xticks(x_values,x_values_for_show)
# 绘制数据点
plt.plot(x_values,y_values,c='green')
'''

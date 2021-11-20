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

filename1 = 'Network1.csv'

with open ( filename1, encoding='utf-8' ) as f1:
    reader1 = csv.reader ( f1 )
    header_row1 = next ( reader1 )

    net = []
    for row in reader1:
        idnet = float ( row[0] )
        num = row[1]
        a = float ( row[2] )
        rls = a   #rls第二层与第一层之比
        h = float ( row[3] )
        Authenticity = str ( row[4] )
        distance = float ( row[5] )    #节点对的距离？？？
        new = {'net_id': idnet, 'num': num, 'rls': rls, 'h': h, 'Authenticity': Authenticity, 'p': 0, 'Distance': distance}
        net.append ( new )

    #alt = array ( f[['net_id', 'num', 'rls', 'H', 'Authenticity','distance']] )

    data = pd.read_csv ( r'Network1.csv' )
    data1 = data['rls']  # 获取名字为flow列的数据
    data_list = data1.values.tolist ()  # 将csv文件中flow列中的数据保存到列表中
    #print ( data_list )

    a = pd.Series ( data_list )
    b = a.value_counts ()
    x = list ( b.index )
    y = []
    x1 = [c0 for c0 in x]
    # x1= [log10(c0) for c0 in x]
    print ( x1 )

    #print ( b )
    for i in x:
        y.append ( b[i] )

    y1 = [c/13 for c in y]
    print ( y1 )

    # x = np.array ( x )
    # y = np.array ( y )
    rls1 = np.array ( x1 )
    p1 = np.array ( y1 )

 #------------------------------------------------------------------

#x_values_for_show = [0.001,0.01,0.1,1,10]
#plt.xticks(rls1,x_values_for_show)
    # filename1 = 'Network1.csv'
    #
    # with open ( filename1, encoding='utf-8' ) as f1:
    #     reader1= csv.reader ( f1 )
    #     header_row1 = next ( reader1 )
    #
    # data3 = pd.read_csv ( r'Network1.csv' )
    # data4 = data['rls']  # 获取名字为rls列的数据
    # data_list1 = data3.values.tolist ()  # 将csv文件中rls列中的数据保存到列表中
    # # print ( data_list )
    #
    # e = pd.Series ( data_list1 )
    # f = e.value_counts ()
    # l = list ( f.index )
    # m = []
    # l1 = [c2 for c2 in l]
    # # x1= [log10(c0) for c0 in x]
    # print ( l1 )
    #
    # # print ( b )
    # for j in l:
    #     m.append ( f[j] )
    #
    # m1 = [c1 / 15 for c1 in m]
    # print ( m1 )
    #
    # l = np.array ( l )
    # m = np.array ( m )
    # rls11 = np.array ( l1 )
    # p11 = np.array ( m1 )

    plt.scatter ( rls1, p1, color='green' )
    # plt.scatter ( rls11, p11, color='green' )


    # for row in net[0:]:
    #   if row['Authenticity'] == 0:
    #    plt.scatter ( rls1, p1, color='red' )


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

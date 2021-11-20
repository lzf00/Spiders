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
#978个数据，前10个小时，857条数据
for ii in range(1,13):
    name='fn'+str(ii)
    #name='normal'+str(ii)
    file_path = 'D:\All_Script\ODES/'+name+'.csv'
    f = open(file_path, 'w', encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['key','S', 'Ic', 'dI/dt','R','Z', 'E','I','SAIRa','SAIRi','Ac','Ic1'])

    d = pd.read_csv('C:\\Users\\Lzf\\Desktop\\动力学模型\\result\\12+12/'+name+'.csv', usecols=['t'])#pandas读文件某一列
    d1 = pd.read_csv('C:\\Users\\Lzf\\Desktop\\动力学模型\\result\\12+12/'+name+'.csv', usecols=['followers_count'])#pandas读文件某一列
    d2 = pd.read_csv('C:\\Users\\Lzf\\Desktop\\动力学模型\\result\\12+12/'+name+'.csv', usecols=['verified'])#pandas读文件某一列

    num0=[]
    num1=[]
    numAI=[]
    i=0
    for x in d['t']:
        num0.append(x)
        i=i+1
        #print(i,':::',x)

    for x in d1['followers_count']:
        num1.append(x)
        # i=i+1
        # print(i,':::',x)
    print(num1)

    for x in d2['verified']:
        numAI.append(x)

        # print(i,':::',x)
    for i in range(1,300):
       numAI.append ( 'none' )
    print('numAI_true or false',numAI)

    print(type(numAI[0]))
    N=[0 for x in range(0,300)]
    N1=[0 for x in range(0,300)]
    N2=[0 for x in range(0,300)]
    NT1=[0 for x in range(0,300)]
    NF1=[0 for x in range(0,300)]
    Sc=[]
    B=[]
    Z=[]
    E=[]
    # print(N)
    # print(len(N))
    t0=num0[0]
    #print(t0)
    tx=60*2
    NT=[0 for x in range(0,300)]  #SAIR感染数A
    NF=[0 for x in range(0,300)]  #SAIR感染数I
    for x in range(1,301):  #步长为2分钟
        for i in num0:
            if  t0+x*tx>i>t0+(x-1)*tx-1:  #每2分钟的计数
                #print(x,':::',i)
                N1[x-1]=N1[x-1]+1
                if ((numAI[x - 1] == 1)  ):  #True为bool型变量
                    NT[x - 1] = NT[x - 1] + 1  # SAIR感染数A(验证用户)
                else:
                    NF[x - 1] = NF[x - 1] + 1  # SAIR感染数I(非验证用户)

            if  t0+x*tx>i>t0-1:   #总数
                #print(x,':::',i)
                N[x-1]=N[x-1]+1

    print ( '每两分钟SAIR的A', NT )
    print ( '每两分钟SAIR的I', NF )

    NI=sum(N1)#总感染数
    NN=sum(num1[0:NI])+1 #总粉丝数+1
    print('总粉丝数：：：',NN)
    print('总感染数：：：',NI)

    writer.writerow ( [0,NN,1,0,0,0,0,1,1,0,1,0 ] )
    for x1 in range ( 1, 301 ):
        N2[x1-1]=sum(num1[0:N[x1-1]])  #0到每个时间的总粉丝数S
        NT1[x1-1]=sum(NT[0:(x1-1)])  #0到每个时间的A  SAIR
        NF1[x1-1]=sum(NF[0:(x1-1)])  #0到每个时间的i
    NT1[0]=1
    print ( 'SAIR的A', NT1 )
    print ( 'SAIR的I', NF1 )

    #取间隔时间的I
    tc=30
    Nc=[0 for x in range(0,300)]
    vi=[0 for x in range(0,300)]
    R=[0 for x in range(0,300)]
    Ac = [0 for x in range ( 0, 300 )]
    Ic1 = [0 for x in range ( 0, 300 )]

    for x1 in range ( 1, 301 ):
        if(x1>tc):
            Nc[x1-1]=N[x1-1]-N[x1-1-tc]
            Ac[x1-1]=NT1[x1-1]-NT1[x1-1-tc]
            Ic1[x1-1]=NF1[x1-1]-NF1[x1-1-tc]

        else:
            Nc[x1-1] = N[x1-1]
            Ac[x1-1] = NT1[x1-1]
            Ic1[x1-1] = NF1[x1-1]
    print('SAIC-Ac',Ac)
    print('SAIC-Ic1',Ic1)

    #转发过期人数R
    for x1 in range ( 1, 301 ):
        if (x1<tc):
            R[x1-1]=0
        else:
            R[x1-1]=N[x1-tc]

    #i的速率
    for x1 in range ( 1, 300 ):
        vi[x1-1]=Nc[x1]-Nc[x1-1]

    key=1
    for x1 in range ( 1, 301 ):
        #N2[x1-1]=sum(num1[0:N[x1-1]])  #0到每个时间的总粉丝数S

        s=NN-N2[x1-1]  #易感数S
        Sc.append ( s )
        b=N[x1-1]/N2[x1-1]
        #print(b)   #感染数/总粉丝数
        B.append(b)  #
        e=NI-N[x1-1]
        E.append(e)  # E暴露者
        z = N2[x1-1]-N[x1-1]
        Z.append ( z )  # Z怀疑者
        writer.writerow ( [key,s,Nc[x1-1],vi[x1-1],R[x1-1],z,e,N[x1-1] ,NT1[x1-1],NF1[x1-1],Ac[x1-1],Ic1[x1-1]] )
        key=key+1

    # print(sum(num1[0:9]))
    # print(sum(num1[0:21]))

    print(B)
    print('Z:::',Z)
    print('E:::',E)
    print('beta*p:::',sum(B)/len(B))   #平均数

    print('I:::',N)  #感染数I（转推人数）
    print("每2分钟感染的人数：：：",N1)
    print('每个时间的总粉丝S:::',N2)  #总粉丝数S


    #print((1583066225-1582954615)/3600) #总时间 ：111610s,31个小时
    print(Nc)
    print(Sc)
    print('i的变化速率',vi)
    print('过期转发',R)
    print('总粉丝数：：：',NN)
    #print(len(R))
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.title('显示中文标题')
    plt.xlabel("横坐标")
    plt.ylabel("纵坐标")
    t=np.arange(0,600,2)
    plt.figure(1)
    ax1=plt.subplot(2,2,1)
    ax2=plt.subplot(2,2,2)
    ax3 = plt.subplot ( 2, 2, 3 )
    ax4 = plt.subplot ( 2, 2, 4 )
    plt.sca(ax1)
    plt.plot(t, Ac[0:300:1], color='blue',label='Ac',marker = "x",markersize=4)  #所有值，间隔半个小时
    plt.legend ()  # 给图像加图例
    plt.sca(ax2)
    plt.plot(t, Ic1[0:300:1], color='red',label='Ic1',marker = "x",markersize=4)
    plt.legend ()  # 给图像加图例
    plt.sca ( ax3 )
    plt.plot ( t, Nc[0:300:1], color='green', label='Nc', marker="x", markersize=4 )  # 所有值，间隔半个小时
    plt.legend ()  # 给图像加图例
    plt.sca ( ax4 )
    plt.plot ( t, Sc[0:300:1], color='black', label='Sc', marker="x", markersize=4 )
    plt.legend (  )  # 给图像加图例
    plt.grid()#添加网格
    plt.show()

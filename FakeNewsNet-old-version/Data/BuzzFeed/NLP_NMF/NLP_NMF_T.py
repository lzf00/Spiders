# -*- codeing = utf-8 -*-
# @Time : 2021/1/31 16:01
# @Author : lzf
# @File : NLP_NMF_T.py
# @Software :PyCharm
import scipy.sparse as sp #稀疏矩阵
from pylab import *
from numpy import *
import random
import pandas as pd
import jieba
import csv
def load_data(file_path):
    f = open(file_path)
    V = []
    for line in f.readlines():
        line = eval ( line ) #字符串转列表（去除外面的引号）
        lines = line.strip().split("/t")
        data = []
        for x in lines:
            x= eval ( x ) #这里x为列表
            #data.append(x)
            print(x)
        V.append(x)
    return mat(V)
#V = load_data('T_NLP.csv')
#print(V)

def train(V, r, k, e):
    m, n = shape(V)
    print('-------------------',m,n)
    #先随机给定一个W、H，保证矩阵的大小
    # W=mat ( ones ( (m, r) ) )
    # H=mat (ones((r,n)))
    W=sp.rand ( m, r, density=1,dtype=float).todense ()
    H=sp.rand ( r, n, density=1, ).todense ()  #生成一个随机稀疏矩阵r*n，密度为0~1
    # W =  random.random ( 0,1,size=(74,5) )
    # H =  random.random ( 0,1,size=(5,15) )

#K为迭代次数
    for x in range(k):
        #error
        V_pre = W * H
        E = V - V_pre
        #print E
        err = 0.0
        for i in range(m):
            for j in range(n):
                err += E[i,j] * E[i,j]
        print(err)
        data.append(err)  #记录误差

        if err < e:
            break
#权值更新
        a = W.T * V
        b = W.T * W * H+1e-9
        #c = V * H.T
        #d = W * H * H.T
        for i_1 in range(r):
            for j_1 in range(n):
                if b[i_1,j_1] != 0:
                    H[i_1,j_1] = H[i_1,j_1] * a[i_1,j_1] / b[i_1,j_1]

        c = V * H.T
        d = W * H * H.T+1e-9
        for i_2 in range(m):
            for j_2 in range(r):
                if d[i_2, j_2] != 0:
                    W[i_2,j_2] = W[i_2,j_2] * c[i_2,j_2] / d[i_2, j_2]

    return W,H,data

if __name__ == "__main__":
    #file_path = "./data_nmf"
    # file_path = "./data1"
    data = []
    V = load_data('NLP_Real.csv')
    #V=[[5,3,2,1],[4,2,2,1,],[1,1,2,5],[1,2,2,4],[2,1,5,4]]
    W, H ,error= train(V, 10, 500, 1e-9) #原始矩阵V，特征数10，迭代次数50，误差1e-5=0.00001
    #print (V)
    print('W------------------------------------------------------------------------')
    print (W)
    print('H------------------------------------------------------------------------')
    print (H)
    print('W*H----------------------------------------------------------------------')
    print (W * H)
    np.savetxt ( 'True_mat_W.csv', W, delimiter=' ' ) #保存矩阵W，分隔符为空格，也可设为逗号
    np.savetxt ( 'True_mat_H.csv', H, delimiter=' ' ) #保存矩阵H

    n = len(error) #error为误差数组，迭代50次
    x = range(n)
    plot(x, error, color='r', linewidth=3)
    plt.title('Convergence curve')
    plt.xlabel('generation')
    plt.ylabel('loss')
    show()

with open ('True_mat_W.csv', 'ab') as f:
  f.write ( open ('Fake_mat_W.csv', 'rb').read ()) #将假新闻的W矩阵写入真新闻的W矩阵中

# path='T_mat_W.csv'
# df=pd.read_csv(path)
# #df.drop_duplicates('name', inplace=True)  #根据name这一列的元素值去重复
# df.insert(1,1,'1')  #（列位置，列名，列数据）插入一列：（有0列）在第一列后面加入一列，列名为1，出入数据为1
# df = df.to_csv(path,index=0,sep=' ')
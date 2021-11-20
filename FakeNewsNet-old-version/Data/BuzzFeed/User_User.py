# -*- codeing = utf-8 -*-
# @Time : 2021/2/5 17:39
# @Author : lzf
# @File : User_User.py
# @Software :PyCharm
#用户关系的邻接矩阵
from numpy import *
import numpy as np
#A = zeros ( (4, 4), dtype=float )  # 先创建一个全零方阵A，并且数据的类型设置为float浮点型
# f = open ( 'BuzzFeedNewsUser.txt' )
# m = f.todense()
# print(m)
#用户用户矩阵（15257，15257）
def getdata(filename):

    linedata = open("BuzzFeedUserUser.txt", 'r')    #读取txt文件
    cnt = 0
    res = []        #存读取后的数据，二元列表
    n = 15257
    matrix = np.zeros((n, n))
    for line in linedata:
        linelist = [int(s) for s in line.split( )] #每一行根据分割后的结果存入列表
        #print(linelist)
        # print(linelist[0])
        # print(linelist[1])
        matrix[linelist[0]-1][linelist[1]-1] = 1
        #print(linelist,matrix[linelist[0]-1][linelist[1]-1])
        cnt += 1
        print(cnt)
    print(matrix)
    print(matrix.shape)
    # print ( matrix[6165][15254] )
    # print ( matrix[6755][15254] )
    # print ( matrix[11491][15254] )
    return matrix
filename = 'BuzzFeedUserUser.txt'
data = getdata(filename)
print(data)
#print(data)
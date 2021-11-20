# -*- codeing = utf-8 -*-
# @Time : 2021/2/5 17:39
# @Author : lzf
# @File : User_User.py
# @Software :PyCharm
#新闻用户矩阵(182, 15257)
from numpy import *
import numpy as np
def getdata(filename):
    linedata = open("BuzzFeedNewsUser.txt", 'r')    #读取txt文件
    cnt = 0
    res = []        #存读取后的数据，二元列表

    matrix = np.zeros((182, 15257))
    for line in linedata:
        linelist = [int(s) for s in line.split( )] #每一行根据分割后的结果存入列表
        #print(linelist)
        # print(linelist[0])
        # print(linelist[1])
        matrix[linelist[0]-1][linelist[1]-1] = linelist[2]
        #print(linelist,matrix[linelist[0]-1][linelist[1]-1])
        cnt += 1
        print(cnt)
    #print(matrix)
    print(matrix.shape)
    print ( matrix[170][18] )
    # print ( matrix[6755][15254] )
    # print ( matrix[11491][15254] )
    return matrix
filename = 'BuzzFeedNewsUser.txt'
data = getdata(filename)
print(data)
#print(data)

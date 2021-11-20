# -*- codeing = utf-8 -*-
# @Time : 2021/2/5 12:55
# @Author : lzf
# @File : UserFeature_mat.py
# @Software :PyCharm
import scipy.io as scio
import scipy.sparse as sp
from scipy.io import loadmat
from pylab import *
import pandas
User_Feature = loadmat('UserFeature.mat')
scio.savemat('UF1.mat',{'X':User_Feature['X']})
print(User_Feature)
print(type(User_Feature))
print(type(User_Feature['X']))
#print(User_Feature['X'])  #列优先稀疏矩阵
print(User_Feature.keys())
m = User_Feature['X'].todense()   #将(元组)稀疏矩阵转换为numpy.matrix
print (type(m))
#print(m)
print(m.shape) #(15257, 109626)
#W=sp.rand ( 109626, 10, density=1,dtype=float).todense ()






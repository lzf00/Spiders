# -*- codeing = utf-8 -*-
# @Time : 2021/2/1 17:28
# @Author : lzf
# @File : NMF_SVM.py
# @Software :PyCharm
from typing import Dict, List
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import colors
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
# with open ('T_mat_W.csv', 'ab') as f:
#   f.write ( open ('F_mat_W.csv', 'rb').read ())  #在一个csv文件后面追加写入另一个文件

path='T_mat_W.csv'
data = np.loadtxt(path, dtype=float,delimiter=' ')
print('矩阵维度:::',data.shape)
#print(data)
y=np.ones((41,1)) #74行1列的‘1’矩阵
#print(y)
for i in range(41):
  y = np.append(y, [[0]], axis=0)   #直接在np数据后面添加元素，加入列表元素【0】，axis=0，1表示垂直，水平方向
#print(y)
#实验链接https://www.cnblogs.com/luyaoblog/p/6775342.html
x_train, x_test, y_train, y_test = train_test_split(data[0:,0:10] ,y,random_state=9,train_size=0.8) #stratify=y，按照y中的比例分配
clf = svm.SVC(C=1, kernel='rbf', gamma=3,decision_function_shape='ovo')   #kernel='rbf'时（default），为高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
#clf = svm.SVC(C=1, kernel='linear', decision_function_shape='ovo')  #kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）。
#特征数为5，使用线性核效果很差0.65，高斯核0.96左右，C=0.8，gamma=7~10最好（数据集为T，X）；数据集为（T，L）0.85,数据集为（T，P）0.839，gamma=4~7
#特征数为10，gamma=6~8，train_size=0.85，最高为0.875
#特征数为10，gamma=3，train_size=0.8，数据集为（T：41，F：41），十次随机平均为0.9470586
def show_accuracy(a, b, tip):
  acc = (a.ravel () == b.ravel ())
  print ( "%s Accuracy:%.6f" % (tip, np.mean ( acc )) )

clf.fit(x_train, y_train.ravel())
#print ('训练精度：',clf.score(x_train, y_train) ) # 精度
y_hat = clf.predict(x_train)
show_accuracy(y_hat, y_train, '训练集')
#print ('测试精度：',clf.score(x_test, y_test))
y_hat = clf.predict(x_test)
show_accuracy(y_hat, y_test, '测试集')
# print ('decision_function:\n', clf.decision_function(x_train))
# print ('\npredict:\n', clf.predict(x_train))

# x=data  #绘图
# def draw(model, x):
#   x1_min, x1_max = x[:, 0].min (), x[:, 0].max ()  # 第0列的范围  x[:, 0] "："表示所有行，0表示第1列
#   x2_min, x2_max = x[:, 1].min (), x[:, 1].max ()  # 第1列的范围  x[:, 0] "："表示所有行，1表示第2列
#   x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点（用meshgrid函数生成两个网格矩阵X1和X2）
#   grid_test = np.stack ( (x1.flat, x2.flat), axis=1 )  # 测试点，再通过stack()函数，axis=1，生成测试点
#   # .flat 将矩阵转变成一维数组 （与ravel()的区别：flatten：返回的是拷贝
#
#   grid_hat = model.predict ( grid_test )  # 预测分类值
#   grid_hat = grid_hat.reshape ( x1.shape )  # 使之与输入的形状相同
#
#   # # 2.指定默认字体
#   # mpl.rcParams['font.sans-serif'] = [u'SimHei']
#   # mpl.rcParams['axes.unicode_minus'] = False
#
#   # 3.绘制
#   cm_light = mpl.colors.ListedColormap ( ['#A0FFA0', '#FFA0A0', '#A0A0FF'] )
#   cm_dark = mpl.colors.ListedColormap ( ['g', 'r', 'b'] )
#
#   # alpha = 0.5
#   plt.pcolormesh ( x1, x2, grid_hat, cmap=cm_light )  # 预测值的显示
#   # plt.plot(x[:, 0], x[:, 1], 'o', alpha=alpha, color='blue', markeredgecolor='k')
#   plt.scatter ( x[:, 0], x[:, 1], c=np.squeeze ( y ), edgecolor='k', s=50, cmap=cm_dark )  # 圈中测试集样本
#   plt.scatter ( x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10 )  # 圈中测试集样本
#   plt.xlabel ( 'sepal length', fontsize=13 )
#   plt.ylabel ( 'sepal width', fontsize=13 )
#   plt.xlim ( x1_min, x1_max )
#   plt.ylim ( x2_min, x2_max )
#   plt.title ( 'SVM feature', fontsize=15 )
#   # plt.grid()
#   plt.show ()
# draw(clf, data)


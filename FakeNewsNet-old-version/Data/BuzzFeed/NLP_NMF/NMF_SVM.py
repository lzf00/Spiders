# -*- codeing = utf-8 -*-
# @Time : 2021/2/1 17:28
# @Author : lzf
# @File : NMF_SVM.py
# @Software :PyCharm
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
# with open ('T_mat_W.csv', 'ab') as f:
#   f.write ( open ('F_mat_W.csv', 'rb').read ())  #在一个csv文件后面追加写入另一个文件

path='True_mat_W.csv'
data = np.loadtxt(path, dtype=float,delimiter=' ')
print('矩阵维度:::',data.shape)
#print(data)
y=np.ones((90,1)) #74行1列的‘1’矩阵
#print(y)
for i in range(81):
  y = np.append(y, [[0]], axis=0)   #直接在np数据后面添加元素，加入列表元素【0】，axis=0，1表示垂直，水平方向
#print(y)
#实验链接https://www.cnblogs.com/luyaoblog/p/6775342.html
x_train, x_test, y_train, y_test = train_test_split(data[:,0:10], y, random_state=0, train_size=0.8) #stratify=y，按照y中的比例分配
clf = svm.SVC(C=1, kernel='rbf', gamma=3,decision_function_shape='ovo')   #kernel='rbf'时（default），为高斯核，gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
#clf = svm.SVC(C=1, kernel='linear', decision_function_shape='ovo')  #kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）。
#特征数为5，使用线性核效果很差0.65，高斯核0.96左右，C=0.8，gamma=7~10最好（数据集为T：74，X：52）；数据集为（T，L：29）0.85,数据集为（T，P：81）0.839，gamma=4~7
#特征数为10，数据集为（T：74，P：81），gamma=6~8，train_size=0.85，最高为0.875
#特征是为10，数据集为BuzzFeed（T:90,F:81）,gamma=3，random=0，最高为0.942857
def show_accuracy(a, b, tip):
  acc = (a.ravel () == b.ravel ())  #ravel扁平化数据
  print ( "%s Accuracy:%.6f" % (tip, np.mean ( acc )) )

clf.fit(x_train, y_train.ravel())
#print ('训练精度：',clf.score(x_train, y_train) ) # 精度
print ('decision_function:\n', clf.decision_function(x_train))
print ('\npredict:\n', clf.predict(x_train))
y_hat = clf.predict(x_train)
show_accuracy(y_hat, y_train, '训练集')
#print ('测试精度：',clf.score(x_test, y_test))
y_hat1 = clf.predict(x_test)
show_accuracy(y_hat1, y_test, '测试集')



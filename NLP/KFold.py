# -*- codeing = utf-8 -*-
# @Time : 2021/2/8 17:35
# @Author : lzf
# @File : KFold.py
# @Software :PyCharm
# MLP for Pima Indians Dataset with 10-fold cross validation
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import StratifiedKFold  #简单的神经网络框架
import numpy as np
# fix random seed for reproducibility
seed = 100
np.random.seed(seed)
# load pima indians dataset
dataset = np.loadtxt("T_mat_W.csv",dtype=float, delimiter=" ")
# split into input (X) and output (Y) variables
X = dataset[:,0:10]
Y=np.ones((41,1)) #74行1列的‘1’矩阵
#print(y)
for i in range(41):
  Y = np.append(Y, [[0]], axis=0)
# define 10-fold crossY validation test harness
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
cvscores = []
for train, test in kfold.split(X, Y):
  # create model
    model = Sequential()
    model.add(Dense(12, input_dim=10, activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X[train], Y[train], epochs=150, batch_size=10, verbose=0)
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
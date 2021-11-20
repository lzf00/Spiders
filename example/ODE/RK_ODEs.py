# -*- codeing = utf-8 -*-
# @Time : 2021/3/27 21:17
# @Author : lzf
# @File : RK_ODEs.py
# @Software :PyCharm
import sys
"""对于自己编写的模块可以通过sys.path.append()把对应路径加入python搜索模块路径"""
#sys.path.append(r"package mcmutils所在路径名")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from example.ODE import RKSEIR  #根目录下的文件夹example.ODE

data = pd.read_csv(r"./china.csv")
# data.head()
N = 140005e4
N=float(N)
I = np.array(data.existing)
R = np.array(data.recovered[:-6])
E = np.array(I[6:] - I[:-6])
I = I[:-6]
S = N*np.ones_like(E) - E - I - R
y = np.array([S, E, I, R])
# 注意numpy的索引是多维数组风格
st = np.argmax(y[2,:])
# st = np.argmax(np.diff(y[2,:]))
# # st = 0
y = np.transpose(y[:,st:])

def seir(t, y, arg, N):
    (beta, lamda, sigma, mu, alpha) =(arg[0], arg[1], arg[2], arg[3], arg[4])
    dS = -beta*lamda*(y[1]+y[2])*y[0]/N
    dE = beta*lamda*(y[1]+y[2])*y[0]/N - y[1]/sigma
    dI = y[1]/sigma - (mu+alpha)*y[2]
    dR = (mu+alpha)*y[2]
    # 按照MATLAB风格 返回导数值的列向量
    return np.array([dS, dE, dI, dR]).T

# 残差函数
def rfun(args, ydata, N):
    len = ydata.shape[0]
    y0 = ydata[0,:]
#     print(y0, len)

    _, yval = RKSEIR.rks4(lambda t,y: seir(t,y, args, N), 1, len, y0, len-1)
#     print(yval.shape)
#     return np.log(np.sum((yval[:,1:] - ydata)**2))
    weights = np.array([0.1,0.1,0.6,0.4])
    return np.sum(np.abs(yval - ydata)*weights, axis=1)

# print(y.shape)
# rfun(np.random.rand(5,1), y)
from scipy.optimize import least_squares
arg0 = np.array([0.1, 3, 7, 0.1, 1e-3])
optiargs = least_squares(lambda arg: rfun(arg, y, N), arg0)
print(optiargs)
len = y.shape[0]
y0 = y[0,:]
# print(y0)
tval, yval = RKSEIR.rks4(lambda t,y: seir(t,y, optiargs.x, N), 1, len, y0, len -1)

sns.set()
fig, ax = plt.subplots()
plt.plot(tval, yval[:,2], 'r--', linewidth=1.5, label='Fit')
plt.plot(tval, y[:,2], 'k--', linewidth=1.5, label='True')
plt.legend(loc='best')
plt.xlabel('days')
plt.ylabel('cases')
plt.title('SEIR model fitting')
err = np.std(yval[:,2]- y[:,2])/np.mean(y[:,2])*100
ax.text(0.4, 0.9, f'Relative error:\n{err:.{3}}%', transform=ax.transAxes)
plt.show()

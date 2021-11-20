# -*- codeing = utf-8 -*-
# @Time : 2021/2/26 14:54
# @Author : lzf
# @File : test1.py
# @Software :PyCharm
import numpy as np
a = np.array([[1], [2]])  #2*1
b = np.array([[3], [4]])
x=np.kron(a, b)  #K积
y=np.outer(a, b)  #外积
z=np.kron(a, b.T)
print(x)
print(y)
print(z)
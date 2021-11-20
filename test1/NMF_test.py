# -*- codeing = utf-8 -*-
# @Time : 2021/1/24 18:31
# @Author : lzf
# @File : NMF_test.py
# @Software :PyCharm
import numpy as np
X = np.array([[1,1,5,2,3], [0,6,2,1,1], [3, 4,0,3,1], [4, 1,5,6,3]])
from sklearn.decomposition import NMF
model = NMF(n_components=2, alpha=0.01)
W = model.fit_transform(X)
H = model.components_
print (W)
print (H)
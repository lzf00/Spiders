# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 15:15
# @Author : lzf
# @File : regular1.py
# @Software :PyCharm
import networkx as nx
import matplotlib.pyplot as plt

# regular graphy
# generate a regular graph which has 20 nodes & each node has 3 neghbour nodes.
RG = nx.random_graphs.random_regular_graph(5, 50)#可以生成一个含有n个节点，每个节点有d个邻居节点的规则图
# the spectral layout
pos = nx.spectral_layout(RG)
# draw the regular graphy
nx.draw(RG, pos, with_labels = False, node_size = 30)
plt.show()
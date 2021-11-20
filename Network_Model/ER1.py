# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 15:15
# @Author : lzf
# @File : ER1.py
# @Software :PyCharm
import networkx as nx
import matplotlib.pyplot as plt

# erdos renyi graph
# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.erdos_renyi_graph(100, 0.1) #生成一个含有n个节点、以概率p连接的ER随机图
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels = False, node_size = 30)
plt.show()
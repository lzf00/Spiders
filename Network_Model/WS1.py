# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 15:10
# @Author : lzf
# @File : WS1.py
# @Software :PyCharm
import networkx as network
import matplotlib.pyplot as plot

ba = network.random_graphs.watts_strogatz_graph(100, 10, 0.3)#生成一个含有n个节点、每个节点有k个邻居、以概率p随机化重连边的WS小世界网络。
ps = network.spring_layout(ba)
network.draw(ba, ps, with_labels = False, node_size = 50)
plot.show()
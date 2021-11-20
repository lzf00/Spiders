# -*- codeing = utf-8 -*-
# @Time : 2021/5/14 15:00
# @Author : lzf
# @File : BA1.py
# @Software :PyCharm
import networkx as network
import matplotlib.pyplot as plot

ba = network.barabasi_albert_graph(300, 2)  #模拟的是300个节点，每次加入m条边
ps = network.spring_layout(ba)
network.draw(ba, ps, with_labels = False, node_size = 50)
plot.show()

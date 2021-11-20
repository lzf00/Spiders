# -*- codeing = utf-8 -*-
# @Time : 2021/3/13 14:47
# @Author : lzf
# @File : test_SIS.py
# @Software :PyCharm
import matplotlib.pylab as plt

N = 1000000
S = N - 1
I = 1
beta = 0.3
gamma = 0.1

sus = []
inf = []

def infection(S, I, N):
    for t in range (0, 1000):
     # S = S - (beta*S*I/N) + gamma * I
     # I = I + (beta*S*I/N) - gamma * I
     S, I = S - beta * ((S * I / N)), I + beta * ((S * I) / N)

     sus.append(S)
     inf.append(I)

infection(S, I, N)

figure = plt.figure()
figure.canvas.set_window_title('SIS model')

inf_line, =plt.plot(inf, label='I(t)')

sus_line, = plt.plot(sus, label='S(t)')
plt.legend(handles=[inf_line, sus_line])

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.xlabel('T')
plt.ylabel('N')

plt.show()
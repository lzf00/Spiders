# -*- codeing = utf-8 -*-
# @Time : 2021/3/18 22:26
# @Author : lzf
# @File : ODEs.py
# @Software :PyCharm
# -*- coding: utf8 -*-
import numpy as np
import matplotlib.pyplot as plt
# -------------------------
# 解微分方程
# -------------------------
# 解微分方程组
# 同名函数，优先调用子类的函数。
# 当子类中没有该函数时，则转向父类中搜索。
# -------------------------------
class RungeKuttaPlus ():
    def __init__(self, fun, Range, init, h):
        # super().__init__(range,x,yinit,h)#搜索父类的初始化函数和成员函数
        # self.__init=init #范围
        self.__Range = Range
        self.__h = h

        self.__num = abs ( self.__Range[1] - self.__Range[0] ) / self.__h + 1
        print ( 'num=', self.__num )
        self.__yz = np.zeros ( (int ( np.ceil ( self.__num ) ), 2) )
        self.__yz[0, :] = init  # 赋初值
        self.__x = np.arange ( self.__Range[0], self.__Range[1] + self.__h, self.__h )
        self.fun = fun
        # print(self.__y)

        self.__calc ()

    # 计算子函数
    def __calc(self):
        h = self.__h
        # L=np.zeros((4,2))
        # print(self.__xx)
        for i in range ( int ( self.__num - 1 ) ):
            y = self.__yz[i, 0]
            z = self.__yz[i, 1]
            x = self.__x[i]
            L1 = self.fun ( z, y, x )
            L2 = self.fun ( z + h * L1 / 2, y + h * z / 2, x + h / 2 )
            L3 = self.fun ( z + h * L2 / 2, y + h * z / 2 + h * h * L1 / 4, x + h / 2 )
            L4 = self.fun ( z + h * L3, y + h * z + h * h * L2 / 2, x + h )

            self.__yz[i + 1, 0] = self.__yz[i, 0] + h * z + (L1 + L2 + L3) * h * h / 6
            self.__yz[i + 1, 1] = self.__yz[i, 1] + h * (L1 + 2 * L2 + 2 * L3 + L4) / 6

    # -----------------------------
    def getResult(self):
        self.__result = np.zeros ( (int ( self.__num ), 3) )
        # print(self.__t)
        self.__result[:, 0] = self.__x.T
        self.__result[:, 1:3] = self.__yz

        return (self.__result)

    # -----------------------------
    def showPlot(self):
        x = self.__result[:, 0]
        y = self.__result[:, 1]
        z = self.__result[:, 2]
        plt.figure ( 1 )
        plt.plot ( x, y, label='First Line:y' )
        # plt.figure(2)
        plt.plot ( x, z, label='Second Line:Dy' )
        # plt.axis([0, 1, -0.8, 0.6]) # x轴起始于-1，终止于10 ，y轴起始于0，终止于6
        plt.legend ()
        plt.show ()


# --------------------------
# 降阶后微分方程的表达形式
def fun(z, y, x=0):
    # f=z+np.exp(2*x)
    f = -3 * z - 2 * y + 1
    return f

# --------------------------
# --------------------------
# 解2个微分方程\2阶微分方程化成一个微分方程组
def calcRungePlus(init, Range, h):
    k = RungeKuttaPlus ( fun, Range, init, h )

    result = k.getResult ()
    print ( 'len(result)=', len ( result ) )
    for i in range ( len ( result ) ):
        print ( '{0:>6.3f}{1:>12.6f}{2:>12.6f}'.format ( result[i, 0], result[i, 1], result[i, 2] ) )
    pass
    k.showPlot ()


# -------------------------------
def main():
    print ( 'The calculation result is below:' )
    # 初始化数据
    init = [0, 0]
    Range = [0, 1]
    h = 0.01
    calcRungePlus ( init, Range, h )

main ()
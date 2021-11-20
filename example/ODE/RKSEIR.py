# -*- codeing = utf-8 -*-
# @Time : 2021/3/27 21:16
# @Author : lzf
# @File : RKSEIR.py
# @Software :PyCharm
import numpy as np
# 包含在'''''' 或 """""" 之间且不属于任何语句的内容将被解释器认为是注释
"""
    Author: Guo
    Step identical 等步长 Runge Kutta 4
    Usage: tval, yval = rks4(dYdt, t_start, t_end, Y_t0, steps -1)
    Parameters: 
    f -- 要求函数f返回导数值的列向量（与MATLAB风格一致）
    Za -- 初始条件的numpy array. (np.array([f1_0, f2_0, f3_0, ...]))
    Return:
    t -- A column vector of t values at each step
    Z -- A matrix containing column vectors of all function values  at each step
"""


def rks4(f, a, b, Za, M):
    # M + 1 steps in total
    h = (b - a) / M
    t = np.linspace ( a, b, M + 1 ).reshape ( M + 1, 1 )
    Z = np.zeros ( (M + 1, Za.size) )
    Z[0, :] = Za
    # print(Z.shape,Z[:,0].shape, Z[0,:].shape)
    for i in range ( 1, M + 1 ):
        k1 = h * f ( t[i - 1], np.transpose ( Z[i - 1, :] ) )
        k2 = h * f ( t[i - 1] + h / 2, np.transpose ( Z[i - 1, :] + k1 / 2 ) )
        k3 = h * f ( t[i - 1] + h / 2, np.transpose ( Z[i - 1, :] + k2 / 2 ) )
        k4 = h * f ( t[i - 1] + h, np.transpose ( Z[i - 1, :] + k3 ) )
        # print(k4.shape)
        Z[i, :] = Z[i - 1, :] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    #     print(t.shape, Z.shape, sep='\n')
    return (t, Z)


def main():
    # 微分方程 dxdt = x; dydt = y
    # 返回dxdt、dydt的列向量
    ode = lambda t, y: np.array ( [y[0], y[1]] ).T
    tval, yval = rks4 ( ode, 0, 1, np.array ( [1, 1] ), 5 )
    # np.diff(ans[::1000,0])
    y = np.exp ( np.linspace ( 0, 1, yval.shape[0] ) )
    # print(yval.shape[0] == y.shape[0])
    print ( np.hstack ( (tval, yval) ) )
    s = np.std ( yval[:, 0] - y ) / np.mean ( y ) * 100
    print ( f"Raletive Error: {s}%" )


if __name__ == '__main__':
    # main()
    # 运行main()函数 请注释掉此语句
    exit ( 'Please use rks4 as module' )

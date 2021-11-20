# -*- codeing = utf-8 -*-
# @Time : 2021/1/24 17:10
# @Author : lzf
# @File : dataclean.py
# @Software :PyCharm
# 引入一个time模块， * 表示time模块的所有功能，
# 作用： 可以统计程序运行的时间
from time import *
begin_time = time()
i=0
while i<1000000:
    print(i)
    i+=1

end_time = time()
run_time = end_time-begin_time
print ('该循环程序运行时间：',run_time,'min')
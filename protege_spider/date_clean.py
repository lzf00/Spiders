# -*- codeing = utf-8 -*-
# @Time : 2021/8/30 23:17
# @Author : lzf
# @File : date_clean.py
# @Software :PyCharm
import csv
import os             #导入设置路径的库
import pandas as pd  #导入数据处理的库
import numpy as np   #导入数据处理的库
# os.chdir('F:/微信公众号/Python/26.基于多列组合删除数据框中的重复值')  #把路径改为数据存放的路径
# name = pd.read_csv('name.csv',sep=',',encoding='gb18030')

def unique_file(filepath):

    # 读入ant-nnop.csv文件
    df=pd.read_csv(filepath, sep=',')
    print(df)
    df1=df.drop_duplicates ( subset='key',keep='last')
    # drop（[0]）表删除0列
    print(df1)
    #d = df.drop([0])
    # d为删除后得到数据，写入1.csv中
    df1.to_csv(filepath,index=False)


if __name__ == '__main__':
    #clearBlankLine()
    filepath='D:\All_Script\Python_deagel/dvids_news350.csv'
    unique_file(filepath)

# -*- codeing = utf-8 -*-
# @Time : 2021/3/26 20:47
# @Author : lzf
# @File : CSV_excel.py
# @Software :PyCharm
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import pandas as pd
from collections import OrderedDict
import sys
import csv
filename=[]
n=0
file_path = r'C:\Users\Lzf\Desktop\动力学模型\result\SIS'
for file in os.listdir(file_path):   #读整个文件夹的csv文件
#可以添加过滤条件if file.endwith(".csv"）
    print (file)
    filename.append(file)
    with open(os.path.join(file_path,file),'r') as f:
      csv_reader = csv.reader(f)
      for line1 in csv_reader:  #读csv文件的每一行
         print (line1)

for i in filename:
    df = pd.read_csv('C:\Users\Lzf\Desktop\动力学模型/result/NEW/'+str(i)+'.csv')
    #filename = 'D:\Anaconda3\envs\DATA set/fake News/fn' + str ( i ) + '.csv'
    # print(df)   #输出csv表格中结果
    data = OrderedDict ()  # 有序字典
    # print(df.columns)     #列名
    for line in list ( df.columns ):
        data[line] = list ( df[line] )  # 构建excel格式

    obj = pd.DataFrame ( data )
    obj.to_excel ( filename[n], index=False )
    print ( '保存成功' )
    n=n+1

# import pandas as pd
# from collections import OrderedDict
#
# #df = pd.read_csv('SEIZ0.csv')
# df = pd.read_csv(r'C:\Users\Lzf\Desktop\动力学模型\result\fn14_result.csv')
#
# # print(df)   #输出csv表格中结果
# data = OrderedDict()   #有序字典
# # print(df.columns)     #列名
# for line in list(df.columns):
#     data[line] = list(df[line])    #构建excel格式
#
# obj = pd.DataFrame(data)
# obj.to_excel('fn14.xlsx',index=False)
# print('保存成功')

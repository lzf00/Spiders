# -*- codeing = utf-8 -*-
# @Time : 2021/11/17 22:34
# @Author : lzf
# @File : x.py
# @Software :PyCharm
import pandas as pd
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myuseragent')

# file_path = r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\2021.11.11\spacecraft111.csv'
# f = open ( file_path, 'a+', encoding='utf-8', newline='' )
# writer = csv.writer ( f )
# writer.writerow ( ['name' ])
#
# filepath1=r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\2021.11.11\spacecraft.csv'
# d = pd.read_csv ( filepath1, usecols=['name'] )  # pandas读文件某一列
# print(d)
# all_lat=[]
# all_lot=[]
# all_spot=[]
# n=1
# num=0
# for xx in d['name'][0:]:
#     try:
#

import os
import re
import time, hashlib
"""批量修改文件夹的图片名"""

def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
def ReFileName(dirPath,pattern):
    """
    :param dirPath: 文件夹路径
    :pattern:正则
    :return:
    """
    # 对目录下的文件进行遍历
    filepath1=r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\spacecraft.csv'
    d = pd.read_csv ( filepath1, usecols=['name'] )  # pandas读文件某一列
    print(d)
    for i in d['name']:
        i=i[0:-1]
        print(i)
    n = 1
    all_id=[]
    for file in os.listdir(dirPath):
        # 判断是否是文件
        if os.path.isfile(os.path.join(dirPath, file)) == True:
           c= os.path.basename(file)
           print(c)
           c1=c.split('-',1)[0]
           print(c1)
           all_id.append(c1)
           #if
           #newName = re.sub(pattern, str(id)+'.png', file)
           #newFilename = file.replace(file, newName)
           # 重命名
           #os.rename(os.path.join(dirPath, file), os.path.join(dirPath, newFilename))
           n+=1
    print("图片名已全部修改成功")
    file_path = r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\2021.11.11\spacecraft111.csv'
    f = open ( file_path, 'w+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['pic'] )
    for x in all_id:
        writer.writerow ( [x] )

if __name__ == '__main__':

    dirPath = r"D:\All_Script\Python_deagel\Img\Spacecraft"
    pattern = re.compile(r'.*')
    ReFileName(dirPath,pattern)









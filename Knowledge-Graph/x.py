# -*- codeing = utf-8 -*-
# @Time : 2021/11/17 22:34
# @Author : lzf
# @File : x.py
# @Software :PyCharm
import pandas as pd
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myuseragent')

file_path = r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\2021.11.11\news111.csv'
f = open ( file_path, 'a+', encoding='utf-8', newline='' )
writer = csv.writer ( f )
writer.writerow ( ['name' ])

filepath1=r'D:\Program Files (x86)\neo4j-community-3.5.28-2\import\2021.11.11\news.csv'
d = pd.read_csv ( filepath1, usecols=['name'] )  # pandas读文件某一列
print(d)
all_lat=[]
all_lot=[]
all_spot=[]
n=1
num=0
for xx in d['name'][0:]:
    try:
        #print("xx",xx)
        #print("last",xx[-1])

        #print("x",x)

        if xx[-1] == ' ':
            x = xx[0:-1]
            all_spot.append ( x )
            print(xx[-1])
            print(n)
            num=num+1
        n=n+1
        print(num)
    except:
        print('此地址无法解析')


for x in range(len(all_spot)):
    writer.writerow ( [all_spot[x]] )
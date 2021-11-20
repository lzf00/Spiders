# -*- codeing = utf-8 -*-
# @Time : 2021/11/17 17:19
# @Author : lzf
# @File : transmap_news.py
# @Software :PyCharm
import pandas as pd
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myuseragent')

file_path = 'D:\All_Script\Python_deagel/trans_news.csv'
f = open ( file_path, 'a+', encoding='utf-8', newline='' )
writer = csv.writer ( f )
writer.writerow ( ['spot','latitude','longitude'] )

filepath1=r'D:\All_Script\Python_deagel\Stanford1.csv'
d = pd.read_csv ( filepath1, usecols=['LOCATION'] )  # pandas读文件某一列
print(d)
all_lat=[]
all_lot=[]
all_spot=[]
for xx in d['LOCATION'][0:]:
    try:
        x=xx.split(';',1)[0]
        print(x)
        all_spot.append(x)
        location = geolocator.geocode(x)
        print ( (location.latitude, location.longitude) )
        all_lat.append(location.latitude)  #纬度
        all_lot.append(location.longitude) #经度
    except:
        print('此地址无法解析')
        all_lat.append ( [] )  # 纬度
        all_lot.append ( [] )
print(len(all_lot))
for x in range(len(all_lot)):
    writer.writerow ( [all_spot[x],all_lat[x],all_lot[x]] )
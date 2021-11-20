# -*- codeing = utf-8 -*-
# @Time : 2021/11/8 22:56
# @Author : lzf
# @File : transmap_act.py
# @Software :PyCharm
import json
from urllib.request import urlopen
import requests

AK = "VYDmvmIWVL0EY3mhSuOnq3o4tb9Vgiml"       #  把复制的AK直接粘贴过来就可以了

# def change(name):
#     url = 'http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s'%(name,AK)
#     res = requests.get(url)
#     if res.status_code == 200:
#         val = res.json()
#         if val["status"] == 0:
#             retval = {'地址':name,'经度':val['result']['location']['lng'],'纬度':val['result']['location']['lat'],'地区标签':val['result']['level'],'是否精确查找':val['result']['precise']}
#         else:
#             retval = None
#         return retval
#     else:
#         print('无法获取%s经纬度'%name)
#
#
# if __name__ == '__main__':
# 	print(change('纽约'))

# def getlnglat(address):
#     url = 'http://api.map.baidu.com/geocoding/v3/'
#     output = 'json'
#     ak = 'SRrx1mGoQw70bjAjvazsKK26OVOVxjte' # 百度地图ak，具体申请自行百度，提醒需要在“控制台”-“设置”-“启动服务”-“正逆地理编码”，启动
#     #address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
#     uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak  +'&callback=showLocation%20'+'//GET%E8%AF%B7%E6%B1%82'
# #     req = urlopen(uri)
# #     res = req.read().decode() 这种方式也可以，和下面的效果一样，都是返回json格式
#     res=requests.get(uri).text
#     temp = json.loads(res) # 将字符串转化为json
#     lat = temp['result']['location']['lat']
#     lng = temp['result']['location']['lng']
#     return lat,lng   # 纬度 latitude,经度 longitude
#
# address='美国阿拉巴MA州阿特伯里营地'
# print(getlnglat(address))


import pandas as pd
import csv
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myuseragent')

file_path = 'D:\All_Script\Python_deagel/trans_act.csv'
f = open ( file_path, 'a+', encoding='utf-8', newline='' )
writer = csv.writer ( f )
writer.writerow ( ['spot','latitude','longitude'] )

filepath1='D:/Program Files (x86)/neo4j-community-3.5.28-2/import/2021.10.21/activity.csv'
d = pd.read_csv ( filepath1, usecols=['spot'] )  # pandas读文件某一列
print(d)
all_lat=[]
all_lot=[]
for x in d['spot'][0:]:
    try:
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
    writer.writerow ( [d['spot'][x],all_lat[x],all_lot[x]] )


# data = [
#         {'Id':'01', 'Address': "BEAU, SC, UNITED STATES", 'Latitude': None, 'Longitude' :None},
#         {'Id':'02', 'Address': "South China Sea", 'Latitude': None, 'Longitude' :None},
#         {'Id':'03', 'Address': "Viale Marconi 197, Rome, Italy", 'Latitude': None, 'Longitude' :None}
#        ]
# df = pd.DataFrame(data)
# df['city_coord']  = df['Address'].apply(geolocator.geocode)
# df['Latitude'] = df['city_coord'].apply(lambda x: (x.latitude))
# df['Longitude'] = df['city_coord'].apply(lambda x: (x.longitude))
# #print(df[['Address',  'Id',   'Latitude','Longitude']])
# print(df[['Address','Latitude','Longitude']])


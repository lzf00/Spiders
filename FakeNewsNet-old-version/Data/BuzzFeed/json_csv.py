# -*- codeing = utf-8 -*-
# @Time : 2021/2/4 15:46
# @Author : lzf
# @File : json_csv.py
# @Software :PyCharm
import csv
import json
import pandas as pd
import sys
import codecs
import csv
import json
import sys
import codecs
for i in range(1,92):
    #path=r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\FakeNewsContent/BuzzFeed_Fake_'+str(i)+'-Webpage'
    path=r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\RealNewsContent/BuzzFeed_Real_'+str(i)+'-Webpage'

    jsonData = codecs.open ( path + '.json', 'r', encoding ='utf-8' )
    csvfile = open ( r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\RealNewsContent/BuzzFeed_Real_1-Webpage' + '.csv', 'a', newline='',encoding = 'utf-8')  # python3下
    writer = csv.writer ( csvfile, delimiter=',', quoting=csv.QUOTE_ALL )
    flag = True
    for line in jsonData:
        dic = json.loads ( line[0:-1] )
        if flag:
            # 获取属性列表
            keys = list ( dic.keys () )
            if (i==1):
                print ( i,keys )
                writer.writerow ( keys )  # 将属性列表写入csv中
            flag = False
            # 读取json数据的每一行，将values数据一次一行的写入csv中
        writer.writerow ( list ( dic.values () ) )
    jsonData.close ()
    csvfile.close ()

# if __name__ == '__main__':
#       # 获取path参数
#     print ( path )
#     for i in range(1,92) :
#       path = r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\FakeNewsContent/BuzzFeed_Fake_'+str(i)+'-Webpage'
#       trans ( path )
      #a=a+1
#path=r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\FakeNewsContent/BuzzFeed_Fake_1-Webpage'

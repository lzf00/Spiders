# -*- codeing = utf-8 -*-
# @Time : 2021/2/7 19:54
# @Author : lzf
# @File : fake_news.py
# @Software :PyCharm
import csv
import json
import pandas as pd
import codecs

f = open('fake_news16.csv', 'w', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow (['内容'])
for i in range(1,17):
    #path=r'D:\demo\shixun\untitled\douban\FakeNewsNet-old-version\Data\BuzzFeed\FakeNewsContent/BuzzFeed_Fake_'+str(i)+'-Webpage'
    path=r'D:\Anaconda3\envs\DATA set\fake News\fn'+str(i)+ '.csv'
    df = pd.read_csv ( path )
    print(i,':',df.iloc[0]["original_text"])
    text=df.iloc[0]["original_text"]
    writer.writerow ([text])


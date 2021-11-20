# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 16:21
# @Author : lzf
# @File : Selenium_html.py
# @Software :PyCharm
from selenium import webdriver
import pandas as pd
import csv

d = pd.read_csv('D:\All_Script\Janes\janes.csv', usecols=['href'])#pandas读文件某一列
print(d)
d1 = pd.read_csv('D:\All_Script\Janes\janes.csv', usecols=['key_num'])#pandas读文件某一列
print(d1)
keynum=[]
for y in d1['key_num']:
   keynum.append(y)
n=1
for x in d['href']:
    #if (n>35):
       try:
          print(n,':::',x)
          driver = webdriver.Chrome()
          driver.get(x)
          #driver.get("https://www.janes.com/defence-news/news-detail/usindopacom-commander-pushes-case-for-aegis-ashore-on-guam")

          # 1. 执行 Chome 开发工具命令，得到html内容
          res = driver.execute_cdp_cmd('Page.captureSnapshot', {})

          # 2. 写入文件
          with open('D:\All_Script\Janes/Janes_'+keynum[n-1]+'_'+str(n)+'.html', 'w') as f:
              f.write(res['data'])
          n=n+1
          driver.close()
       except:
          print('无')

# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 15:27
# @Author : lzf
# @File : url_html.py
# @Software :PyCharm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import urllib.request
from urllib.request import urlopen
import csv
import pandas as pd
import time, hashlib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import *
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
begin = time.time()

d = pd.read_csv('D:\All_Script\Janes\janes.csv', usecols=['href'])#pandas读文件某一列
print(d)

def getHtml(url):

    request = urllib.request.Request(url,header)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def saveHtml(file_name,file_content):
    with open(file_name.replace('/','_')+'.html','wb') as f:
        f.write(file_content)

# html = getHtml("http://www.baidu.com")
# saveHtml('test1',html)

for x in d['href']:
    #if (n>0):
        print(x)
        #date = urllib.parse.quote_plus ( x ).encode ( "utf-8" )
        #date = urllib.parse.urlencode ( x ).encode ( encoding='UTF8' )
        #date="https://www.janes.com/defence-news/news-detail/usindopacom-commander-pushes-case-for-aegis-ashore-on-guam"
        date = urllib.parse.quote ( x,safe='/'+':').encode ( encoding='UTF8' )
        #date = urllib.parse.quote ( date, safe=':' ).encode ( encoding='UTF8' )
        header='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        #html = getHtml(date,header)
        html = getHtml ( date)
        saveHtml(x,html)

print("结束")

# -*- codeing = utf-8 -*-
# @Time : 2021/8/31 12:36
# @Author : lzf
# @File : USNI_href.py
# @Software :PyCharm
import csv
from tokenize import String
import pandas as pd
import time, hashlib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import *
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
from selenium.webdriver.common.by import By

begin = time.time()

def USNI(file_path):
    #file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['id', 'time', "content", "related", "href"] )
    for i in range(1,2):  #页数
        url='https://news.usni.org/category/fleet-tracker/page/'+str(i)


        # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
        # writer1 = csv.writer ( f1 )
        # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )

        chrome_options1 = Options ()
        chrome_options1.add_argument ( 'headless' )
        chrome_options1.add_argument ( 'disable-gpu' )
        driver = webdriver.Chrome ( chrome_options=chrome_options1 )
        #driver = webdriver.Chrome( )
        #url='https://www.deagel.com/Offensive%20Weapons'
        driver.get(url)
        driver.maximize_window()
        #time.sleep(3)
        driver.implicitly_wait(2)
        try:
            driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
        except:
            print()
        #driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()

        html = driver.page_source
        # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
        soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
        ol=soup.find('ol', {'class', 'wp-paginate font-inherit'} )
        li=ol.find()


        h1s = soup.find_all ( 'h1', {'class', 'entry-title'} )
        times=soup.find_all('time',{'class','entry-date'})
        all_time=[]
        all_href=[]
        for h1 in h1s:
            a=h1.find('a')
            href=a.get('href')
            print(href)
            all_href.append(href)

        for item in times:
            date=item.text
            print(date)
            all_time.append(date)
        print(len(all_href),len(all_time))

        for x in range(0,10):
            writer.writerow ([x+(i-1)*10,all_time[x],'1','1',all_href[x]])



USNI('D:\All_Script\Python_USNI/usni_href10.31.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
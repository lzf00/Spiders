# -*- codeing = utf-8 -*-
# @Time : 2021/11/16 13:56
# @Author : lzf
# @File : space_news.py
# @Software :PyCharm
# -*- codeing = utf-8 -*-
# @Time : 2021/9/6 16:22
# @Author : lzf
# @File : missilethreat_href.py
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
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

begin = time.time()

def Spacenews(file_path,file_href):
    f = open ( file_path, 'a+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['time','title','content','href'] )

    f1 = open ( file_href, 'a+', encoding='utf-8', newline='' )
    writer1 = csv.writer ( f1 )
    writer1.writerow ( ['key', 'href'] )

    all_href = []
    num=1
    for key in range(1,2):
      #if num<3:

            print(num,":::",key)
            url='https://spacenews.com/section/militaryspace/'
        #try:
            # chrome_options1 = Options ()
            # chrome_options1.add_argument ( 'headless' )
            # chrome_options1.add_argument ( 'disable-gpu' )
            # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
            driver = webdriver.Chrome( )
            #url='https://www.deagel.com/Offensive%20Weapons'
            driver.get(url)
            driver.maximize_window()
            #time.sleep(3)
            driver.implicitly_wait(2)
            try:
                driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
            except:
                print()
            for x in range(0,1):  #一页18个新闻
                print(x)
                driver.find_element_by_xpath ( '//*[@id="main"]/p/a' ).click ()
                time.sleep(2.5)
                js = "var q=document.documentElement.scrollTop=10000"  # 下拉滑轮
                driver.execute_script ( js )
                time.sleep(2.5)

            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页

            div=soup.find('div',{'class','launch-section'})
            h2s=div.find_all('h2',{'class','launch-title'})
            all_href=[]
            num1 = 1
            for x in h2s :
                a=x.find('a')
                href=a.get('href')
                print(href)
                all_href.append(href)
                #writer1.writerow ( [ num,href] )
                num1=num1+1
    driver.close()
    print(len(all_href))
    numh=0
    #try:
    filepath1 = r'D:\All_Script\Python_deagel\space_href.csv'
    d = pd.read_csv ( filepath1, usecols=['href'] )  # pandas读文件某一列
    print ( d[752:] )
    for x in d['href'][1092:]:
        print(numh,":::",x)
        driver = webdriver.Chrome ()
        driver.get ( x )
        driver.maximize_window ()
        # time.sleep(3)
        driver.implicitly_wait ( 2 )
        try:
            driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
        except:
            print ()
        time1 = driver.find_element_by_xpath ( '//*[@id="main"]/article/section/span/time' )
        time2 = time1.get_attribute ( 'textContent' )
        print ( time2 )

        title1 = driver.find_element_by_xpath ( '//*[@id="main"]/article/section/h1' )
        title2 = title1.get_attribute ( 'textContent' )
        print ( title2 )

        html = driver.page_source
        # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
        soup = BeautifulSoup ( html, 'html.parser', from_encoding='utf-8' )  # 解析网页
        ehtml = etree.HTML ( html, parser=etree.HTMLParser ( encoding='utf-8' ) )

        intro = ehtml.xpath ( '//div[@class="tablet-wrapper"]/p//text()' )
        print ( intro )
        intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
        print ( intro1 )
        writer.writerow ( [ time2, title2, intro1,x] )
        numh = numh + 1
        driver.close ()
    # except:
    #
    #   print("网络错误")

Spacenews('D:\All_Script\Python_deagel/space_news.csv','D:\All_Script\Python_deagel/space_href.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
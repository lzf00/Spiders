# -*- codeing = utf-8 -*-
# @Time : 2021/9/6 17:04
# @Author : lzf
# @File : missilethreat_news.py
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

#/html/body/div[2]/div[8]/div/div[1]/div/div[5]

def USNI(file_path):
    d = pd.read_csv ( 'D:\All_Script\Python_deagel/missilethreat_href1117.csv', usecols=['href'] )  # pandas读文件某一列
    #print ( d[0:138] )
    print(d)
    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['key','time','title','style','content'] )

    num=1
    for key in d['href']:
        #if num<139:
        print(num,":::",key)
        url=key

        try:
            # chrome_options1 = Options ()
            # chrome_options1.add_argument ( 'headless' )
            # chrome_options1.add_argument ( 'disable-gpu' )
            # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
            driver = webdriver.Chrome()
            #url='https://www.deagel.com/Offensive%20Weapons'
            driver.get(url)
            driver.maximize_window()
            #time.sleep(3)
            driver.implicitly_wait(2)
            try:
                driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
            except:
                print()
            time1=driver.find_element_by_xpath ( '//div[@class="post-meta post-meta__date"]' )
            time2=time1.get_attribute('textContent')
            print(time2)

            style1 = driver.find_element_by_xpath ( '//div[@class="post-meta post-meta__authors"]/a' )
            style2 = style1.get_attribute ( 'textContent' )
            print ( style2 )

            title1 = driver.find_element_by_xpath ( '//h1[@class="single__header-title"]' )
            title2 = title1.get_attribute ( 'textContent' )
            print ( title2 )


            #//*[@id="site-content"]/header/div/div[1]/h1/font/font
            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser',from_encoding='utf-8' )  # 解析网页
            ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))

            intro = ehtml.xpath ( '//div[@class="single__content"]/p//text()' )
            print(intro)
            intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
            print(intro1)
            writer.writerow ( [key,time2,title2,style2,intro1] )
            num=num+1
            driver.close()
        except:
            print(num,"--------------------网络错误--------------------------")

USNI('D:\All_Script\Python_deagel/missilethreat_news1117.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
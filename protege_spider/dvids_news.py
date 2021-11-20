# -*- codeing = utf-8 -*-
# @Time : 2021/9/7 14:52
# @Author : lzf
# @File : dvids_news.py
# @Software :PyCharm
#https://www.dvidshub.net/search/?q=F-35&filter%5Bdate%5D=1y&filter%5Btype%5D=news&filter%5Bcountry%5D=United+States&view=list&page=1

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
    d = pd.read_csv ( 'D:\All_Script\Python_deagel/dvids_href10.31.csv', usecols=['href'] )  # pandas读文件某一列
    #print ( d[0:138] )
    print(d[0:])
    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'a+', encoding='utf-8', newline='')
    writer = csv.writer ( f )
    writer.writerow ( ['key','time','title','spot','unit','tags','content'] )

    num=1
    for key in d['href'][0:]:
    #for key in d['href']:
        #if num<139:
        try:
            print(num,":::",key)
            url=key

            # chrome_options1 = Options ()
            # chrome_options1.add_argument ( 'headless' )
            # chrome_options1.add_argument ( 'disable-gpu' )
            # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
            driver = webdriver.Chrome()
            #url='https://www.deagel.com/Offensive%20Weapons'
            driver.get(url)
            driver.maximize_window()
            #time.sleep(1)
            driver.implicitly_wait(2)
            try:
                driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
            except:
                print()
            #time.sleep(1)
            time1=driver.find_element_by_xpath ( '//div[@class="uk-grid asset_information"]/div/h3[2]' )
            time2=time1.get_attribute('textContent')
            print(time2)

            spot1 = driver.find_element_by_xpath (  '//div[@class="uk-grid asset_information"]/div/h3[1]' )
            spot2 = spot1.get_attribute ( 'textContent' )
            print ( spot2 )

            title1 = driver.find_element_by_xpath ( '//h1[@class="asset-title"]' )
            title2 = title1.get_attribute ( 'textContent' )
            print ( title2 )

            unit1 = driver.find_element_by_xpath ( '//h3[@class="the_unit"]/a' )
            unit2 = unit1.get_attribute ( 'textContent' )
            print ( unit2 )

            #//*[@id="site-content"]/header/div/div[1]/h1/font/font
            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
            ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))

            all_tag=[]
            tags=soup.find_all('div',{'class','readonly'})
            for tag in tags :
                try:
                    tag1=tag.find('a')
                    tag2=tag1.text
                    print(tag2)
                    all_tag.append(tag2)
                except:
                    print("标签错误")


            intro = ehtml.xpath ( '//div[@class="uk-width-10-10 uk-width-small-10-10 uk-width-medium-7-10 uk-width-large-7-10 asset_news_container asset_container"]/p//text()' )
            print(intro)
            intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
            print(intro1)
            writer.writerow ( [key,time2,title2,spot2,unit2,all_tag,intro1] )
            num=num+1
            driver.close()
        except:
            print(num,"网络错误")
            #driver.close()

USNI('D:\All_Script\Python_deagel/dvids_news10.31.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
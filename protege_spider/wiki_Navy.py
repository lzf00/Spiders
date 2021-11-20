# -*- codeing = utf-8 -*-
# @Time : 2021/9/10 11:50
# @Author : lzf
# @File : wiki_Navy.py
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

begin = time.time()

def USNI(file_path):

    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['id','content1','catalogue'] )



    try:
            driver = webdriver.Chrome( )
            url='https://en.wikipedia.org/wiki/List_of_units_of_the_United_States_Navy'
            driver.get(url)
            driver.maximize_window()
            #time.sleep(3)
            driver.implicitly_wait(2)
            try:
                driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
            except:
                print()
            # time1=driver.find_element_by_xpath ( '//div[@class="uk-grid asset_information"]/div/h3[2]' )
            # time2=time1.get_attribute('textContent')
            # print(time2)

            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' )  # 解析网页
            ehtml = etree.HTML ( html )

#//*[@id="toc"]
            intro = ehtml.xpath ( '//div[@class="mw-parser-output"]//text()' )
            print(intro)
            intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
            print ( intro1 )
            intro2=intro1.split ( '10 References', 1 )[1]
            intro3 = intro2.split ( 'Operational Test and Evaluation Force', 1 )[0]
            print(intro3)

            intro4 = ehtml.xpath ( '//div[@id="toc"]//text()' )
            #print ( intro4 )
            intro5 = ''.join ( intro4 ).strip ()
            print(intro5)

            num=1
            writer.writerow ( [num, intro3,intro5] )
            # for i in intro:
            #     print(i)
            #     writer.writerow ( [ num,i ] )
            #     num=num+1  U.S. Transportation Command

    except:
        print("网络错误")

USNI('D:\All_Script\Python_deagel/wiki_Navy.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
# -*- codeing = utf-8 -*-
# @Time : 2021/9/9 17:58
# @Author : lzf
# @File : wiki_Combatant.py
# @Software :PyCharm
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
import numpy as np
from selenium.webdriver.common.by import By

begin = time.time()

#/html/body/div[2]/div[8]/div/div[1]/div/div[5]

def USNI(file_path):

    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['id','content1','content2','catalogue'] )

    try:
            driver = webdriver.Chrome( )
            url='https://en.wikipedia.org/wiki/Structure_of_the_United_States_Armed_Forces#Combatant_Commands'
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


            intro = ehtml.xpath ( '//div[@class="mw-parser-output"]//text()' )
            print(intro)
            intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
            print ( intro1 )
            intro2=intro1.split ( 'Chief Master Sergeant of the Space Force', 1 )[1]
            intro3 = intro2.split ( 'See also', 1 )[0]
            print(intro3)
            intro33 = intro2.split ( 'See also', 1 )[0]
            print ( intro33 )
            intro4 = intro3.split ( 'U.S. Strategic Command', 1 )[0]
            print(intro4)
            intro5 = intro33.split ( 'U.S. Strategic Command', 1 )[1]
            print ( intro5 )
            num=1
            intro6 = ehtml.xpath ( '//div[@id="toc"]//text()' )
            # print ( intro4 )
            intro7 = ''.join ( intro6 ).strip ()
            print ( intro7 )

            writer.writerow ( [num, intro4,intro5,intro7] )
            # for i in intro:
            #     print(i)
            #     writer.writerow ( [ num,i ] )
            #     num=num+1  U.S. Transportation Command

    except:
        print("网络错误")

USNI('D:\All_Script\Python_deagel/wiki.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
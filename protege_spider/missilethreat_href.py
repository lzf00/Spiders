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
import numpy as np
from selenium.webdriver.common.by import By

begin = time.time()

#//*[@id="post-9644"]/h2/a
def USNI(file_path):
    f = open ( file_path, 'a+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['id','href'] )

    all_href = []
    num=1
    for key in range(1,10):
      #if num<3:
        print(num,":::",key)
        url='https://missilethreat.csis.org/category/news/page/'+str(key)

        # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
        # writer1 = csv.writer ( f1 )
        # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )
        try:
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
            #driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()

            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页

            section=soup.find('section',{'class','archive__posts'})
            h2s=section.find_all('h2',{'class','post-block__title text--semibold'})
            for x in h2s :
                a=x.find('a')
                href=a.get('href')
                print(href)
                writer.writerow ( [ key,href] )
            num=num+1
        except:
            print("网络错误")

USNI('D:\All_Script\Python_deagel/missilethreat_href1117.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
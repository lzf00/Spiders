# -*- codeing = utf-8 -*-
# @Time : 2021/9/5 17:51
# @Author : lzf
# @File : sputniknews.py
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
#http://sputniknews.com/military/20150528/1022674154.html
def USNI(file_path):
    d = pd.read_csv ( 'D:\All_Script\Python_deagel/sputniknews_news1.csv', usecols=['source'] )  # pandas读文件某一列
    print ( d[0:162] )
    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['id','key','content'] )

    all_href = []
    num=1
    for key in d['source'][0:162]:
        # if num<163:
        #     print(num,":::",key)
            url=key

        # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
        # writer1 = csv.writer ( f1 )
        # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )
        # try:
            chrome_options1 = Options()
            chrome_options1.add_argument ( 'headless' )
            chrome_options1.add_argument ( 'disable-gpu' )
            driver = webdriver.Chrome (chrome_options=chrome_options1 )
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

            ehtml = etree.HTML ( html,parser=etree.HTMLParser(encoding='utf-8') )
            # intro = ehtml.xpath ( '/html/body/div[2]/div[8]/div/div[1]/div/div[5]//text()' )
            intro = ehtml.xpath ( '//*[@id="endless"]/div/div/div/div/div[1]/div/div[3]//text()' )

            print(intro)
            #//*[@id="endless"]/div/div/div/div/div[1]/div/div[3]
            intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
            print(intro1)
            writer.writerow ( [ num,key,intro1] )
            num=num+1
        # except:
        #     print("网络错误")

USNI('D:\All_Script\Python_deagel/sputniknews_news.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
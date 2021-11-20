# -*- codeing = utf-8 -*-
# @Time : 2021/9/1 13:10
# @Author : lzf
# @File : USNI_news.py
# @Software :PyCharm
#https://news.usni.org/2021/08/30/usni-news-fleet-and-marine-tracker-aug-30-2021

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

def USNI(file_path):
    d = pd.read_csv ( 'D:\All_Script\Python_USNI\\usni_href10.31.csv', usecols=['href'] )  # pandas读文件某一列
    print ( d )
    # file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'w', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['time', "context1","context2","context3","context4","context5","context6","context7","context8","context9","context10","context11","context12","context13", "href","key_num"] )

    all_href = []
    num=1
    for key in d['href']:
      #if num<3:
        print(key)
        url=key
        date=url[22:32]
        print(date)

        # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
        # writer1 = csv.writer ( f1 )
        # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )
        try:
            chrome_options1 = Options ()
            chrome_options1.add_argument ( 'headless' )
            chrome_options1.add_argument ( 'disable-gpu' )
            driver = webdriver.Chrome ( chrome_options=chrome_options1 )
            # driver = webdriver.Chrome( )
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

            ehtml = etree.HTML ( html,parser=etree.HTMLParser(encoding='utf-8') )
            intro = ehtml.xpath ( '//div[@class="entry-content"]//text()' )
            print(intro)
            intro1 = '\n'.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割

            body=soup.find('div', {'class', 'entry-content'} )
            #ps=soup.find_all('p')

            h2s=body.find_all('h2')
            all_h2=[]
            for h2 in h2s:
                spot=h2.text
                print(spot)
                all_h2.append(spot)
            print(len(all_h2))


            context = [[] for i in range ( 100 )]
            xtext = []
            xname=[]
            # for ns in range ( len ( ths ) ):
            for ii in range ( len ( intro ) ):
                # xtext.append(0)
                if intro[ii] in all_h2:
                    # print ( ii, ':::', intro[ii] )
                    if intro[ii] not in xname:
                        xname.append ( intro[ii] )
                        xtext.append ( ii )

            xtext.insert ( 0, 0 )
            xtext.append ( len ( intro ) )
            #print ( len ( xtext ) )
            for it in range ( 2, len ( xtext ) ):
                for x in range ( xtext[it - 1], xtext[it] ):
                    context[it].append ( intro[x] )
                context[it] = ''.join ( context[it] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
                #print ( "it:::", it, context[it] )  # 分离各武器信息
            if len(all_h2)==6:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],'','','','','','','',key,len(all_h2)])
            if len(all_h2)==7:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],'','','','','','',key,len(all_h2)])
            if len(all_h2)==8:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],'','','','','',key,len(all_h2)])
            if len(all_h2)==9:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],context[10],'','','','',key,len(all_h2)])
            if len(all_h2)==10:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],context[10],context[11],'','','',key,len(all_h2)])
            if len(all_h2)==11:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],context[10],context[11],context[12],'','',key,len(all_h2)])
            if len(all_h2)==12:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],context[10],context[11],context[12],context[13],'',key,len(all_h2)])
            if len(all_h2)==13:
                writer.writerow ([date,context[2],context[3],context[4],context[5],context[6],context[7],context[8],context[9],context[10],context[11],context[12],context[13],context[14],key,len(all_h2)])
            num=num+1
        except:
            print("浏览器错误")

USNI('D:\All_Script\Python_USNI/usni_news10.31.csv')#
end = time.time ()
print ( '6-13/运行时间：', (end - begin) / 60 )  # 50分钟


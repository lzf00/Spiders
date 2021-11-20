# -*- codeing = utf-8 -*-
# @Time : 2021/9/7 15:35
# @Author : lzf
# @File : dvids_href.py
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

#//*[@id="post-9644"]/h2/a
def USNI(file_path):
    f = open ( file_path, 'a+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['key','id','href'] )
    d = pd.read_csv ( 'D:\All_Script\Python_deagel/Weaponname.csv', usecols=['name'] )  # pandas读文件某一列
    print ( d[769:] )
    #print ( d[728:] )
    all_href = []
    xx=1
    for word in d['name'][769:]:  #序号减 2
        print("武器序号",xx)
        num = 1
        for key in range(1,3):
          #if num<11:
            url='https://www.dvidshub.net/search/?q='+str(word)+'&filter%5Btype%5D=news&filter%5Bcountry%5D=United+States&filter%5Bdate%5D=20211101-20211117&view=list&sort=relevance&page='+str(key)
            #url='https://www.dvidshub.net/search/?q='+str(word)+'&filter%5B&filter%5Btype%5D=news&filter%5Bcountry%5D=United+States&view=list&page='+str(key)
            print ( num, ":::", url )
            # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
            # writer1 = csv.writer ( f1 )
            # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )
            try:
                chrome_options1 = Options ()
                chrome_options1.add_argument ( 'headless' )
                chrome_options1.add_argument ( 'disable-gpu' )
                driver = webdriver.Chrome ( chrome_options=chrome_options1 )
                #url='https://www.deagel.com/Offensive%20Weapons'
                #driver = webdriver.Chrome()
                driver.get(url)
                driver.maximize_window()
                #time.sleep(3)
                driver.implicitly_wait(2)
                #driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()

                html = driver.page_source
                # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
                soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
            except:
                print ( "网络错误" )

                #section=soup.find('div',{'class','search_results_info_inner_wrapper'})
            #try:
            ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))
            intro = ehtml.xpath ( '//div[@id="search_results_views"]/p//text()' )
            intro1 = ''.join ( intro ).strip ()
            #print ( intro1 )
            if intro1=='No results found for your search.  Please try fewer keywords or expand your date range.':
                print("wu")
                break

            h2s=soup.find_all('h2',{'class','assetTitle'})

            for x in h2s :
                    a=x.find('a')
                    href=a.get('href')
                    href='https://www.dvidshub.net'+href
                    print(href)
                    writer.writerow ( [ word,key,href] )
            num=num+1
            driver.close()
        xx=xx+1
            #except:
                # num=11
                # print("此武器无新闻")

USNI('D:\All_Script\Python_deagel/dvids_href11.17.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
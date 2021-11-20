# -*- codeing = utf-8 -*-
# @Time : 2021/7/14 11:14
# @Author : lzf
# @File : Janes_scrapy.py
# @Software :PyCharm
import csv
import pandas as pd
import time, hashlib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import *
import time
begin = time.time()

d = pd.read_csv('weapon-all.csv', usecols=['产品'])#pandas读文件某一列
print(d)
file_path = 'D:\All_Script\Janes/janes1.csv'
f = open(file_path, 'w', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['id','key','key进展',"time",'title',"content","href"])

n=1

all_href=[]
for key in d['产品']:
     #if (n<2) :
        print(n,'::',key,"----------------------------")
        #n=n+1
        driver = webdriver.Chrome( )
        url='https://www.janes.com/search-results?indexCatalogue=all---production&searchQuery='+key+'&wordsMode=AllWords'
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        driver.implicitly_wait(2)
        try:
            driver.find_element_by_xpath ( '//div[@id="onetrust-button-group"]/button[2]' ).click ()  # 同意按钮
        except:
            print()
        html = driver.page_source
        soup = BeautifulSoup ( html, 'html.parser' )
        uls = soup.find_all ( 'div', {'class','list-item border-bottom border-primary px-3 pb-2 mb-4'} ) #文章主体
        j=0
        for ul in uls :
          if(j<10):
            print ( '3333333' )
            time_class=ul.find_all('div',{'class','tag-list small float-left'})
            #print(time_class)
            #time = time_class.find_all ( '//span[@class="mr-2 pr-2 mb-2 tag"][2]' )
            for x1 in time_class:
                try:
                    time1=x1.find_all ('span',{'class','mr-2 pr-2 mb-2 tag'})[1].text
                    print(time1)
                except:
                     print("无时间")
            a = ul.find_all ( 'a',limit=1)

            for x in a:
                href = x.get ( 'href' )
                all_href.append ( href )
                title=x.text
                print(title)
                print ( "j:", j )
                print ( "href:", all_href[j] )
                j=j+1

                driver.get ( href )
                html = driver.page_source
                soup = BeautifulSoup ( html, 'html.parser' )
                ehtml = etree.HTML ( html ) #etree
                strings = ehtml.xpath ( "//div[@class='sf_colsIn col-md-12']/div/p/text()" )#提取文章内容
                ys=[]
                for y in strings:
                    y=y.replace('\n',' ')  #str.replace("is", "was", 3)
                    print(y)
                    ys.append(y)
                #driver.find_element_by_xpath ( '//div[@id="Contentplaceholder1_T478E928A005_Col00"]' )
                # html = driver.page_source
                # soup = BeautifulSoup ( html, 'html.parser' )
                writer.writerow ( [n,key,key+'-'+str(j),time1,title, ys,href] )
                #driver.close()
        n=n+1
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟





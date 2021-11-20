# -*- codeing = utf-8 -*-
# @Time : 2021/10/8 23:16
# @Author : lzf
# @File : WIKI_weapon.py
# @Software :PyCharm

import csv
from tokenize import String
import pandas as pd
import time, hashlib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import *
import pandas as pd
import time, hashlib
import urllib
import urllib.request
import  requests
from selenium.webdriver.chrome.options import Options

begin = time.time()

def WIKI_weapon(file_path,imgpath):
    f = open ( file_path, 'a+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['key', 'href','content','canshu','picture','imgurl'] )
    d = pd.read_csv ( 'D:/Program Files (x86)/neo4j-community-3.5.28-2/import/fleet.csv', usecols=['name'] )  # pandas读文件某一列
    print ( d[10:] )
    # print ( d[728:] )
    all_href = []
    xx = 1
    for word in d['name'][0:1]:
            print ( "武器序号", xx )
            num = 1

        #try:
            #url='https://en.wikipedia.org/wiki/'+str(word)
            url='https://en.wikipedia.org/wiki/USS_Kidd_(DDG-100)'

            # chrome_options1 = Options ()
            # chrome_options1.add_argument ( 'headless' )
            # chrome_options1.add_argument ( 'disable-gpu' )
            # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
            driver = webdriver.Chrome ()
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
            imgurl = driver.find_element_by_xpath ( '//*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td/a' ).get_attribute('href')
            print(imgurl)
            # imgurl1='https://en.wikipedia.org'+imgurl
            #//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[1]/td/a   //*[@id="mw-content-text"]/div[1]/table[1]/tbody/tr[1]/td/div[1]/div/a
            #https://en.wikipedia.org/wiki/File:USS_Alaska_SSBN-732.jpg
            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
            ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))

            intro = ehtml.xpath ( '//*[@id="mw-content-text"]/div[1]/p[2]//text()' )
            # print(intro)  //*[@id="mw-content-text"]/div[1]/p[2]
            intro1 = ''.join ( intro ).strip ()
            print ( intro1 )

            table = soup.find ( 'table', {'class', 'infobox'} )
            tbody = table.find('tbody')
            #print(tbody)
            trs= tbody.find_all('tr',attrs={'style','vertical-align:top;'})
            trs= tbody.find_all('tr')
            all_td=[]
            for tr in trs :
                tds=tr.find_all('td')
                for td in tds:
                    keys=td.text
                    keys = ''.join ( keys ).strip ()
                    print(keys)
                    all_td.append(keys)

            del all_td[0]
            print(len(all_td))
            num=1
            for i in range(0,len(all_td)):
                if i%2==1:
                    all_td.insert(i+num,';')
                    num=num+1
            print(all_td)

            # for i in range(0,len(all_td)):
            #     if i%2==0:
            #         all_td.insert(i,';')
            # print(all_td)
            #time.sleep(5)
            #dataimg = requests.get ( imgurl )
            driver.get ( imgurl )
            #//*[@id="file"]/a
            imgurl1 = driver.find_element_by_xpath ('//*[@id="file"]/a' ).get_attribute ( 'href' )
            print ( imgurl1 )

            img=imgurl1.split('/', 7)[7]
            #img1="1198px-"+img
            print(img)

            writer.writerow ( [word, url,intro1,all_td,img,imgurl1] )
            xx=xx+1
            driver.close()
        # except:
        #     print("网络错误")
        #     writer.writerow ( [word, url, '[]', '[]', '[]', '[]'] )
        #     xx = xx + 1

WIKI_weapon('D:\All_Script\Python_deagel/wiki_weapon1017.csv','D:\All_Script\Python_deagel\Img\Fleet/')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
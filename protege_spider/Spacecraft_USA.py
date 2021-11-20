# -*- codeing = utf-8 -*-
# @Time : 2021/8/31 12:36
# @Author : lzf
# @File : USNI_href.py
# @Software :PyCharm
import csv
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time, hashlib
import urllib
import urllib.request


begin = time.time()
def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
def Spacecraft(file_path):
    #file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open ( file_path, 'a+', encoding='utf-8', newline='' )
    writer = csv.writer ( f )
    writer.writerow ( ['name','context','paras,','version', "href","img"] )

    for i in range(1,2):  #页数
        url='https://space.skyrocket.de/directories/sat_mil_usa.htm'

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
        # try:
        #driver.find_element_by_xpath ( '//a[@class="cc_btn cc_btn_accept_all"]' ).click ()  # 同意按钮
        # except:
        #     print("wu")

        html = driver.page_source
        # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
        soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='iso-8859-1')  # 解析网页
        ol=soup.find('tbody' )
        lis=ol.find_all('li')
        print(lis)
        all_href=[]
        for li in lis:
            try:
                a=li.find('a')
                #print(a)
                #href1=a.get_attribute ( 'href' )
                a=str(a)
                #print(a)
                href1=a.split('"', 3)[1]
                href1=href1.split('/',1)[1]
                print(href1)
                all_href.append(href1)

            except:
                print("无href")
    print(len(all_href))
    for x in all_href[505:]:
        url1='https://space.skyrocket.de/'+str(x)
        print("name:::",x)
        driver.get ( url1 )

        #driver.find_element_by_xpath ( '//a[@class="cc_btn cc_btn_accept_all"]' ).click ()  # 同意按钮
#/html/body/div[2]/div[2]/div/h1

        name1 = driver.find_element_by_xpath ( '/html/body/div[2]/div[2]/div/h1' )
        name2 = name1.get_attribute ( 'textContent' )
        print(name2)
        try:
            img1 = driver.find_element_by_xpath ( '/html/body/div[2]/div[2]/div/div/div/img' )#//*[@id="contimg"]/img
            img2 = img1.get ( 'src' )
            print(img2)
        except:
            print('无图片')

        html = driver.page_source
        soup = BeautifulSoup ( html, 'html.parser', from_encoding='iso-8859-1' )  # 解析网页
        ehtml = etree.HTML ( html, parser=etree.HTMLParser ( encoding='iso-8859-1' ) )
        intro = ehtml.xpath ( '//*[@id="satdescription"]/p//text()' )
        #print(intro)
        intro1 = ''.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
        print ( intro1 )
        tabs = ehtml.xpath ( '//*[@id="satdata"]/tbody/tr//text()' )
        tabs1 = ''.join ( tabs ).strip ()
        #print(tabs1)  //*[@id="contimg"]/img
        try:
            imgx=soup.find ( 'div', {'class','ibox'} )
            imgx1=imgx.find('img')
            imgurl=imgx1.get ( 'src' ) #https://space.skyrocket.de/img_sat/opticube__1.jpg
            imgurl=imgurl.split('/',1)[1]
            imgurl1='https://space.skyrocket.de/'+imgurl
            print(imgurl1)
        except:
            print('无img')
            imgurl1=[]
        try:
            dataimg = urllib.request.urlopen ( imgurl1 ).read ()
            #key = key.replace ( '/', '.' )
            id = create_id ()
            imgname = name2 + '-' + id + '.png'
            f = open ( 'D:\All_Script\Python_deagel\Img\Spacecraft/' + name2 + '-' + id + '.png', 'wb' )
            f.write ( dataimg )
        except:
            print("无img")

        table1 = soup.find ( 'table', {'class','data'} )#//*[@id="satdata"]
        #print(table1)

        all_td=[]
        all_th=[]
        ths = table1.find_all ( 'th' )
        for th in ths:
            texta=th.text
            print(texta)
            all_th.append(texta)
        tds=table1.find_all('td')
        for td in tds:
            textb=td.text
            print(textb)
            all_td.append(textb)

        #//*[@id="satlist"]/tbody
        table2 = soup.find ( 'table', id= 'satlist' )  # //*[@id="satdata"]
        all_th1 = []
        all_td1 = []
        try:
            tbody=table2.find_all("tr")
            #print(tbody)
            for x in tbody:
                tr1=x.find_all('th')
                for xx in tr1:
                    th1=xx.text
                    print(th1)
                    all_th1.append(th1)

            for x in tbody:
                tr1=x.find_all('td')
                for xx in tr1:
                    td1=xx.text
                    print(td1)
                    all_td1.append(td1)

            tabsat = ehtml.xpath ( '//*[@id="satlist"]/tbody/tr//text()' )
            tabsat1 = ''.join ( tabsat ).strip ()
            #print ( tabsat1 )
        except:
            print("无tbody")

        # for x in range(0,10):
        writer.writerow ([name2,intro1,all_th+['///']+all_td,all_th1+['///']+all_td1,url1,imgname])

Spacecraft('D:\All_Script\Python_deagel/Spacecraft2.csv')#
end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟
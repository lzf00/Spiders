# -*- codeing = utf-8 -*-
# @Time : 2021/8/23 10:28
# @Author : lzf
# @File : deagel_missile.py
# @Software :PyCharm
#source_a = source.find ( 'a', attrs={'target': '_blank'} )  # 按标签名查找,格式：( 'a', attrs={'target': '_blank'} )

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

def deagel(file_path,url,usa,usanews):
    #file_path = 'D:\All_Script\Python_deagel/missile_news.csv'
    f = open(file_path, 'w', encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['id','key','key_V','group',"time","title","content",'related','zuzhi',"href","source"])

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
    driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()
    driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/div/div/ul/li[' + str (usa) + ']/label' "" ).click ()

    #driver.find_element_by_xpath ( '//div[@class="table-responsive table-hover guide"]/table/tbody/' )
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    uls1 = soup.find('tbody')
    print(uls1)
    tds=uls1.find_all('td',{'class','pl-3'})
    groups=uls1.find_all('td',{'class','d-none d-md-table-cell'})
    j=0
    all_href=[]
    all_name=[]
    all_type=[]
    for group in groups:
        type=group.text
        #print ( type )
        all_type.append ( type )
        j = j + 1


    for td in tds:
        a=td.find('a')
        href=a.get('href')
        all_href.append ( href )
        name=a.get_text()
        all_name.append ( name )

        #print(href)
        #print(name)

    all_href1=[]
    all_name1=[]
    for i in range(0,j):
        try:

            url = 'https://www.deagel.com/'+all_href[i]
            #print('href:',all_href[i])
            print(i,':::武器',url)
            driver.get(url = url)
            time.sleep(1)
            #driver.find_element_by_xpath ( '//div[@class="d-flex flex-row ng-star-inserted"]/a[1]' ).click ()  #点击新闻

            html = driver.page_source
            #html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup(html,'html.parser') #解析网页

            div1 = soup.find ( 'div', attrs={'class', 'd-flex flex-row ng-star-inserted'} )

        except:
            print("url没打开/网络错误")
        try:
            a1 = div1.find ( 'a' )
            hrefnews = a1.get ( 'href' )  #取出新闻链接href
            #print(i,":::::::::;:",hrefnews)
            if hrefnews not in all_href1:
                all_href1.append ( hrefnews )
                all_name1.append(all_name[i])
        except:
            print("此武器没有新闻链接")
    print ( "武器新闻数量:::", len ( all_href1 ) )

    for i1 in range(0,len(all_href1)):
    #for i1 in range ( 0, 1 ):

        try:
            url1='https://www.deagel.com/'+all_href1[i1]
            print ( i1, ':::新闻', url1)
            driver.get ( url=url1 )
            driver.find_element_by_xpath ( '//div[@class="col-12 col-md-6 col-xl-8"]/button[2]' ).click ()  #点击过滤器
            #time.sleep(1)
            driver.find_element_by_xpath ( '//ul[@class="nav nav-tabs"]/li[3]/a' ).click ()  #点击过滤器
            #driver.find_element_by_xpath ( '//div[@class="tab-pane container fade active show"]/ul/li[50]/label' ).click ()  #点击美国
            driver.find_element_by_xpath ("" '//div[@class="tab-content"]/div[3]/ul/li['+str(usanews)+']/label' "").click ()  # 点美国
            time.sleep(1)
            driver.find_element_by_xpath ('//div[@class="modal-dialog"]/div/div[3]/button[1]' ).click ()  # 点结果
            time.sleep(1)
            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' )  # 解析网页
        except:
            print("无过滤器")
        try:#无新闻

            allnews=soup.find ( 'div', {'class', 'col-12 card-deck card-news'} )
            time.sleep(1)
            anews=allnews.find_all('a')#新闻href
            pnews=allnews.find_all('p',{'class','card-text ng-star-inserted'})#新闻摘要
            timenews=allnews.find_all('h5',{'class','card-title ng-star-inserted'})#新闻时间
            all_newslj=[]
            all_title=[]
            for news in anews:
                newslj=news.get('href')
                #print(newslj)  #新闻链接
                all_newslj.append(newslj)
                title=news.get_text()
                #print(title)#新闻标题
                all_title.append(title)
            print("武器相关新闻数量：",url,":::",len(all_title))

            all_pnews=[]
            all_timenews=[]
            for x in pnews:
                pnews1=x.text
                print("新闻摘要:::",pnews1)
                all_pnews.append(pnews1)


            for n in range(len(all_newslj)):
            #for n in range ( 2 ):
                urllj='https://www.deagel.com/'+all_newslj[n]
                print(i,"武器序号/",len(all_newslj),"新闻序号//",n,":::",urllj)
                driver.get ( url=urllj )
                time.sleep ( 1 )

                html = driver.page_source
                # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
                soup = BeautifulSoup ( html, 'html.parser' )  # 解析网页
                body = soup.find ( 'div', {'class', 'col-12 col-xl-10 bg-white'} )
                #print(body)
                time.sleep(1)
                date1=body.find('i')
                date2=date1.text
                print(date2)  #新闻时间

                source=soup.find ( 'div', {'class', 'col-12 col-lg-8 mb-5'} )#col-12 col-lg-8 mb-5
                #source_a=source.find('a',attrs={'class','ng-star-inserted'})
                source_a = source.find ( 'a', attrs={'target': '_blank'} )  # 按标签名查找,格式：( 'a', attrs={'target': '_blank'} )
                print("找到a")
                try:
                    source_href=source_a.get('href')
                    print('source:::',source_href)
                    source_text=source_a.text
                    print('sourcetext:::',source_text)
                except:
                    print("无来源信息source")
                print("wua")
                related=soup.find ( 'div', {'class', 'col-12 col-lg-4 card-deck card-photo'} )
                related_div=related.find_all('div',{'class', 'card-body'},limit=2)

                relatedlist=[]  #相关国家和武器
                for div in related_div:
                    a1=div.find_all('a')
                    for a in a1:
                        print('aaaaa',a.text)#涉及的国家和装备
                        relatedlist.append(a.text)

                ehtml = etree.HTML ( html )
                intro = ehtml.xpath ( '//div[@class="col-12 col-lg-8 mb-5"]//text()' )
                intro1 = '\n'.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
                #print(intro1)

                related_b = related.find_all ( 'div', {'class', 'card-body'} ,limit=3)
                b_num = 1
                for b in related_b:
                    print ( 'bbbbb', b.text )  # 文章中词的缩写
                    if b_num == 3:
                        print ( 'bbbbb33333', b.text )
                        zuzhi = b.text
                        zuzhi=list(zuzhi)
                        #zuzhi.append('-')
                        for x in range(len(zuzhi)-1):
                            #print ( zuzhi[x] )
                            if zuzhi[x].islower() and zuzhi[x+1].isupper():#判断字母大小写
                                zuzhi.insert(x+1,'.\n')
                                #print("cg")
                        zuzhi = ''.join ( zuzhi ).strip ()

                    b_num = b_num + 1
                print(zuzhi)

                writer.writerow ( [i1, all_name1[i1],all_name1[i1]+'_'+str(n+1), all_type[i1], date2,all_title[n],intro1, relatedlist,zuzhi,urllj,source_href] )
                time.sleep(1)
        except:
            print("无新闻")

#deagel('D:\All_Script\Python_deagel/missile_news.csv','https://www.deagel.com/Offensive%20Weapons',76,50)#导弹
# deagel('D:\All_Script\Python_deagel/Aircraft_news.csv','https://www.deagel.com/Combat%20Aircraft',135,50)#战斗机
# deagel('D:\All_Script\Python_deagel/Fships_news.csv','https://www.deagel.com/Fighting%20Ships',70,50)#战舰
# deagel('D:\All_Script\Python_deagel/defensive_news.csv','https://www.deagel.com/Defensive%20Weapons',111,50)#防御性武器
# deagel('D:\All_Script\Python_deagel/protection_news.csv','https://www.deagel.com/Protection%20Systems',72,50)#保护系统
deagel('D:\All_Script\Python_deagel/Support_Aircraft_news.csv','https://www.deagel.com/Support%20Aircraft',133,50)#支援飞机

deagel('D:\All_Script\Python_deagel/Armored_Vehicles_news.csv','https://www.deagel.com/Armored%20Vehicles',139,50)#装甲车
deagel('D:\All_Script\Python_deagel/Artillery_Systems_news.csv','https://www.deagel.com/Artillery%20Systems',113,48)#火炮系统
deagel('D:\All_Script\Python_deagel/Auxiliary_Vessels_news.csv','https://www.deagel.com/Auxiliary%20Vessels',62,50)#辅助舰艇
deagel('D:\All_Script\Python_deagel/Space_Systems_news.csv','https://www.deagel.com/Space%20Systems',32,50)#空间系统

deagel('D:\All_Script\Python_deagel/Tactical_Vehicles_news.csv','https://www.deagel.com/Tactical%20Vehicles',116,50)#战术车辆
deagel('D:\All_Script\Python_deagel/Cannons_Gear_news.csv','https://www.deagel.com/Cannons%20&%20Gear',152,50)#大炮和装备
deagel('D:\All_Script\Python_deagel/Propulsion_Systems_news.csv','https://www.deagel.com/Propulsion%20Systems',140,50)#推进系统
deagel('D:\All_Script\Python_deagel/Sensor_news.csv','https://www.deagel.com/Sensor%20Systems',83,50)#传感器（雷达）



end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟






# -*- codeing = utf-8 -*-
# @Time : 2021/9/2 19:34
# @Author : lzf
# @File : deagel_news2015.py
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

usanews=50
file_path = 'D:\All_Script\Python_deagel/news2021.11.17.csv'
f = open(file_path, 'a+', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(["time","title","content",'related','zuzhi',"href","source"])

def page0():
    # try:
        url = 'https://www.deagel.com/news' #https://www.deagel.com/news


        # chrome_options1 = Options ()
        # chrome_options1.add_argument ( 'headless' )
        # chrome_options1.add_argument ( 'disable-gpu' )
        # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
        # url='https://www.deagel.com/Offensive%20Weapons'
        driver = webdriver.Chrome()
        driver.get ( url )
        driver.maximize_window ()
        # time.sleep(3)
        driver.implicitly_wait ( 2 )
        try:
            driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
        except:
            print()
        driver.find_element_by_xpath ( '//div[@class="col-12 col-md-6 col-xl-8"]/button[2]' ).click ()  # 点击过滤器
        # time.sleep(1)
        driver.find_element_by_xpath ( '//ul[@class="nav nav-tabs"]/li[3]/a' ).click ()  # 点击过滤器
        # driver.find_element_by_xpath ( '//div[@class="tab-pane container fade active show"]/ul/li[50]/label' ).click ()  #点击美国
        driver.find_element_by_xpath ("" '//div[@class="tab-content"]/div[3]/ul/li[' + str ( usanews ) + ']/label' "" ).click ()  # 点美国
        time.sleep ( 1 )
        driver.find_element_by_xpath ( '//div[@class="modal-dialog"]/div/div[3]/button[1]' ).click ()  # 点结果
        time.sleep ( 1 )

        for x in range(1,2):
            html = driver.page_source
            #html = html1.read ().decode ( "utf-8" )
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser',from_encoding='utf-8' )  # 解析网页

            #allnews = soup.find ( 'div', {'class', 'col-12 card-deck card-news'} )  # col-12 card-deck card-news
            allnews = soup.find ( 'div', {'class', 'row mt-3 ng-star-inserted'} ) #col-12 card-deck card-news
            time.sleep ( 1 )
            print(allnews)
            anews = allnews.find_all ( 'a' )  # 新闻href
            print(anews)
            pnews = allnews.find_all ( 'p', {'class', 'card-text ng-star-inserted'} )  # 新闻摘要
            timenews = allnews.find_all ( 'h5', {'class', 'card-title ng-star-inserted'} )  # 新闻时间
            all_newslj = []
            all_title = []
            for news in anews:
                #/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[1]/div[2]/div/h5/a
                #/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[1]
                newslj = news.get ( 'href' )
                print(newslj)  #新闻链接
                all_newslj.append ( newslj )
                title = news.get_text ()
                # print(title)#新闻标题
                all_title.append ( title )
            print ( "武器相关新闻数量：", url, ":::", len ( all_title ) )

            all_pnews = []
            all_timenews = []
            for x in pnews:
                pnews1 = x.text
                print ( "新闻摘要:::", pnews1 )
                all_pnews.append ( pnews1 )

        # except:
        #     print('无')
    #
            for n in range ( len ( all_newslj ) ):
            #for n in range ( 2 ):
                urllj = 'https://www.deagel.com/' + all_newslj[n]
                print (  "武器序号/", len ( all_newslj ), "新闻序号//", n, ":::", urllj )
                driver.get ( url=urllj )
                time.sleep ( 1 )

                html = driver.page_source
                # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
                soup = BeautifulSoup ( html, 'html.parser',from_encoding='utf-8' )  # 解析网页
                body = soup.find ( 'div', {'class', 'col-12 col-xl-10 bg-white'} )
                # print(body)
                time.sleep ( 1 )
                date1 = body.find ( 'i' )
                date2 = date1.text
                print ( date2 )  # 新闻时间

                source = soup.find ( 'div', {'class', 'col-12 col-lg-8 mb-5'} )  # col-12 col-lg-8 mb-5
                # source_a=source.find('a',attrs={'class','ng-star-inserted'})
                source_a = source.find ( 'a', attrs={'target': '_blank'} )  # 按标签名查找,格式：( 'a', attrs={'target': '_blank'} )
                print ( "找到a" )
                try:
                    source_href = source_a.get ( 'href' )
                    print ( 'source:::', source_href )
                    source_text = source_a.text
                    print ( 'sourcetext:::', source_text )
                except:
                    print ( "无来源信息source" )
                print ( "wua" )
                related = soup.find ( 'div', {'class', 'col-12 col-lg-4 card-deck card-photo'} )
                related_div = related.find_all ( 'div', {'class', 'card-body'}, limit=2 )

                relatedlist = []  # 相关国家和武器
                for div in related_div:
                    a1 = div.find_all ( 'a' )
                    for a in a1:
                        print ( 'aaaaa', a.text )  # 涉及的国家和装备
                        relatedlist.append ( a.text )

                #ehtml = etree.HTML ( html)
                ehtml = etree.HTML ( html,parser=etree.HTMLParser(encoding='utf-8') )
                intro = ehtml.xpath ( '//div[@class="col-12 col-lg-8 mb-5"]//text()' )
                intro1 = '\n'.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
                # print(intro1)
                zuzhi="zuzhi"
                try:
                    related_b = related.find_all ( 'div', {'class', 'card-body'}, limit=3 )
                    b_num = 1
                    for b in related_b:
                        print ( 'bbbbb', b.text )  # 文章中词的缩写
                        if b_num == 3:
                            print ( 'bbbbb33333', b.text )
                            zuzhi = b.text
                            zuzhi = list ( zuzhi )
                            # zuzhi.append('-')
                            for x in range ( len ( zuzhi ) - 1 ):
                                # print ( zuzhi[x] )
                                if zuzhi[x].islower () and zuzhi[x + 1].isupper ():  # 判断字母大小写
                                    zuzhi.insert ( x + 1, '.\n' )
                                    # print("cg")
                            zuzhi = ''.join ( zuzhi ).strip ()

                        b_num = b_num + 1
                    print ( zuzhi )
                except:
                    print("组织错误")

                writer.writerow ([  date2, all_title[n], intro1,relatedlist, zuzhi, urllj, source_href] )
                time.sleep ( 1 )

def page(num):
    try:
        url = 'https://www.deagel.com/news' #https://www.deagel.com/news

        chrome_options1 = Options ()
        chrome_options1.add_argument ( 'headless' )
        chrome_options1.add_argument ( 'disable-gpu' )
        driver = webdriver.Chrome ( chrome_options=chrome_options1 )
        # url='https://www.deagel.com/Offensive%20Weapons'
        driver.get ( url )
        driver.maximize_window ()
        # time.sleep(3)
        driver.implicitly_wait ( 2 )
        try:
            driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
        except:
            print()
        driver.find_element_by_xpath ( '//div[@class="col-12 col-md-6 col-xl-8"]/button[2]' ).click ()  # 点击过滤器
        # time.sleep(1)
        driver.find_element_by_xpath ( '//ul[@class="nav nav-tabs"]/li[3]/a' ).click ()  # 点击过滤器
        # driver.find_element_by_xpath ( '//div[@class="tab-pane container fade active show"]/ul/li[50]/label' ).click ()  #点击美国
        driver.find_element_by_xpath ("" '//div[@class="tab-content"]/div[3]/ul/li[' + str ( usanews ) + ']/label' "" ).click ()  # 点美国
        time.sleep ( 1 )
        driver.find_element_by_xpath ( '//div[@class="modal-dialog"]/div/div[3]/button[1]' ).click ()  # 点结果
        time.sleep ( 1 )
        driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']' "").click ()  #
        driver.implicitly_wait ( 2 )
        print( "lixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" , driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']/a' "").get_attribute('textContent'))  #)
    except:
        print ( "无过滤器" )

#def news80():
    for x in range(1,2):
        try:  # 无新闻

            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
            allnews = soup.find ( 'div', {'class', 'col-12 card-deck card-news'} ) #col-12 card-deck card-news
            time.sleep ( 1 )
            anews = allnews.find_all ( 'a' )  # 新闻href
            pnews = allnews.find_all ( 'p', {'class', 'card-text ng-star-inserted'} )  # 新闻摘要
            timenews = allnews.find_all ( 'h5', {'class', 'card-title ng-star-inserted'} )  # 新闻时间
            all_newslj = []
            all_title = []
            for news in anews:
                newslj = news.get ( 'href' )
                #print(newslj)  #新闻链接
                all_newslj.append ( newslj )
                title = news.get_text ()
                # print(title)#新闻标题
                all_title.append ( title )
            print (  url, ":::", len ( all_title ) )

            all_pnews = []
            all_timenews = []
            for x in pnews:
                pnews1 = x.text
                #print ( "新闻摘要:::", pnews1 )
                all_pnews.append ( pnews1 )

        # except:
        #     print('无')
    #
            for n in range ( len ( all_newslj ) ):
            #for n in range ( 1 ):
                urllj = 'https://www.deagel.com/' + all_newslj[n]
                print (  "武器序号/", len ( all_newslj ), "新闻序号//", n, ":::", urllj )
                driver.get ( url=urllj )
                time.sleep ( 1 )

                html = driver.page_source
                # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
                soup = BeautifulSoup ( html, 'html.parser',from_encoding='utf-8' )  # 解析网页
                body = soup.find ( 'div', {'class', 'col-12 col-xl-10 bg-white'} )
                # print(body)
                time.sleep ( 1 )
                date1 = body.find ( 'i' )
                date2 = date1.text
                print ( date2 )  # 新闻时间

                source = soup.find ( 'div', {'class', 'col-12 col-lg-8 mb-5'} )  # col-12 col-lg-8 mb-5
                # source_a=source.find('a',attrs={'class','ng-star-inserted'})
                source_a = source.find ( 'a', attrs={'target': '_blank'} )  # 按标签名查找,格式：( 'a', attrs={'target': '_blank'} )
                print ( "找到a" )
                try:
                    source_href = source_a.get ( 'href' )
                    print ( 'source:::', source_href )
                    source_text = source_a.text
                    print ( 'sourcetext:::', source_text )
                except:
                    print ( "无来源信息source" )
                print ( "wua" )
                related = soup.find ( 'div', {'class', 'col-12 col-lg-4 card-deck card-photo'} )
                related_div = related.find_all ( 'div', {'class', 'card-body'}, limit=2 )

                relatedlist = []  # 相关国家和武器
                for div in related_div:
                    a1 = div.find_all ( 'a' )
                    for a in a1:
                        print ( 'aaaaa', a.text )  # 涉及的国家和装备
                        relatedlist.append ( a.text )

                ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))
                intro = ehtml.xpath ( '//div[@class="col-12 col-lg-8 mb-5"]//text()' )
                intro1 = '\n'.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
                # print(intro1)

                related_b = related.find_all ( 'div', {'class', 'card-body'}, limit=3 )
                b_num = 1
                for b in related_b:
                    print ( 'bbbbb', b.text )  # 文章中词的缩写
                    if b_num == 3:
                        print ( 'bbbbb33333', b.text )
                        zuzhi = b.text
                        zuzhi = list ( zuzhi )
                        # zuzhi.append('-')
                        for x in range ( len ( zuzhi ) - 1 ):
                            # print ( zuzhi[x] )
                            if zuzhi[x].islower () and zuzhi[x + 1].isupper ():  # 判断字母大小写
                                zuzhi.insert ( x + 1, '.\n' )
                                # print("cg")
                        zuzhi = ''.join ( zuzhi ).strip ()

                    b_num = b_num + 1
                print ( zuzhi )

                writer.writerow ([  date2, all_title[n], intro1,relatedlist, zuzhi, urllj, source_href] )
                time.sleep ( 1 )

        except:
            print ( "无新闻" )

def pagenext(num,off):  #num=8__13
    try:
        url = 'https://www.deagel.com/news' #https://www.deagel.com/news

        chrome_options1 = Options ()
        chrome_options1.add_argument ( 'headless' )
        chrome_options1.add_argument ( 'disable-gpu' )
        driver = webdriver.Chrome ( chrome_options=chrome_options1 )
        # url='https://www.deagel.com/Offensive%20Weapons'
        driver.get ( url )
        driver.maximize_window ()
        # time.sleep(3)
        driver.implicitly_wait ( 2 )
        try:
            driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
        except:
            print()
        driver.find_element_by_xpath ( '//div[@class="col-12 col-md-6 col-xl-8"]/button[2]' ).click ()  # 点击过滤器
        # time.sleep(1)
        driver.find_element_by_xpath ( '//ul[@class="nav nav-tabs"]/li[3]/a' ).click ()  # 点击过滤器
        # driver.find_element_by_xpath ( '//div[@class="tab-pane container fade active show"]/ul/li[50]/label' ).click ()  #点击美国
        driver.find_element_by_xpath ("" '//div[@class="tab-content"]/div[3]/ul/li[' + str ( usanews ) + ']/label' "" ).click ()  # 点美国
        time.sleep ( 1 )
        driver.find_element_by_xpath ( '//div[@class="modal-dialog"]/div/div[3]/button[1]' ).click ()  # 点结果
        # time.sleep ( 1 )
        # driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']' "").click ()  #
        time.sleep ( 1 )
        driver.find_element_by_xpath ("/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li[12]").click ()  #点击next
        if off == 0:
            #driver.find_element_by_xpath ("/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li[12]" ).click ()  #

            driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']' "").click ()  #

        elif off==17:
            driver.find_element_by_xpath ("/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li[13]" ).click ()  #
            # time.sleep ( 1 )
            # driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']' "").click ()  #

        elif off==18:
            driver.find_element_by_xpath ("/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li[13]" ).click ()  #
            time.sleep(2)
            driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']' "").click ()  #
        else:
            print('off')
        print( "lixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" , driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']/a' "").get_attribute('textContent'))  #)

        time.sleep(1)
    #print( "lixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" , driver.find_element_by_xpath ("" '/html/body/app-root/div/div/app-news/div/div[2]/div[4]/div[2]/ul/li['+ str ( num ) +']/a' "").get_attribute('textContent'))  #)
    except:
        print ( "无过滤器" )

    for x in range(1,2):
        try:  # 无新闻
            time.sleep(1)
            html = driver.page_source
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
            allnews = soup.find ( 'div', {'class', 'col-12 card-deck card-news'} ) #col-12 card-deck card-news
            time.sleep ( 1 )
            anews = allnews.find_all ( 'a' )  # 新闻href
            pnews = allnews.find_all ( 'p', {'class', 'card-text ng-star-inserted'} )  # 新闻摘要
            timenews = allnews.find_all ( 'h5', {'class', 'card-title ng-star-inserted'} )  # 新闻时间
            all_newslj = []
            all_title = []
            for news in anews:
                newslj = news.get ( 'href' )
                #print(newslj)  #新闻链接
                all_newslj.append ( newslj )
                title = news.get_text ()
                # print(title)#新闻标题
                all_title.append ( title )
            print (  url, ":::", len ( all_title ) )

            all_pnews = []
            all_timenews = []
            for x in pnews:
                pnews1 = x.text
                #print ( "新闻摘要:::", pnews1 )
                all_pnews.append ( pnews1 )

        # except:
        #     print('无')
    #
            for n in range ( len ( all_newslj ) ):
            #for n in range ( 1 ):
                urllj = 'https://www.deagel.com/' + all_newslj[n]
                print (  "武器序号/", len ( all_newslj ), "新闻序号//", n, ":::", urllj )
                driver.get ( url=urllj )
                time.sleep ( 1 )

                html = driver.page_source
                # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
                soup = BeautifulSoup ( html, 'html.parser' ,from_encoding='utf-8')  # 解析网页
                body = soup.find ( 'div', {'class', 'col-12 col-xl-10 bg-white'} )
                # print(body)
                time.sleep ( 1 )
                date1 = body.find ( 'i' )
                date2 = date1.text
                print ( date2 )  # 新闻时间

                source = soup.find ( 'div', {'class', 'col-12 col-lg-8 mb-5'} )  # col-12 col-lg-8 mb-5
                # source_a=source.find('a',attrs={'class','ng-star-inserted'})
                source_a = source.find ( 'a', attrs={'target': '_blank'} )  # 按标签名查找,格式：( 'a', attrs={'target': '_blank'} )
                print ( "找到a" )
                try:
                    source_href = source_a.get ( 'href' )
                    print ( 'source:::', source_href )
                    source_text = source_a.text
                    print ( 'sourcetext:::', source_text )
                except:
                    print ( "无来源信息source" )
                print ( "wua" )
                related = soup.find ( 'div', {'class', 'col-12 col-lg-4 card-deck card-photo'} )
                related_div = related.find_all ( 'div', {'class', 'card-body'}, limit=2 )

                relatedlist = []  # 相关国家和武器
                for div in related_div:
                    a1 = div.find_all ( 'a' )
                    for a in a1:
                        print ( 'aaaaa', a.text )  # 涉及的国家和装备
                        relatedlist.append ( a.text )

                ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))
                intro = ehtml.xpath ( '//div[@class="col-12 col-lg-8 mb-5"]//text()' )
                intro1 = '\n'.join ( intro ).strip ()  # 用回车符将列表里的每个元素进行分割
                # print(intro1)

                related_b = related.find_all ( 'div', {'class', 'card-body'}, limit=3 )
                b_num = 1
                for b in related_b:
                    print ( 'bbbbb', b.text )  # 文章中词的缩写
                    if b_num == 3:
                        print ( 'bbbbb33333', b.text )
                        zuzhi = b.text
                        zuzhi = list ( zuzhi )
                        # zuzhi.append('-')
                        for x in range ( len ( zuzhi ) - 1 ):
                            # print ( zuzhi[x] )
                            if zuzhi[x].islower () and zuzhi[x + 1].isupper ():  # 判断字母大小写
                                zuzhi.insert ( x + 1, '.\n' )
                                # print("cg")
                        zuzhi = ''.join ( zuzhi ).strip ()

                    b_num = b_num + 1
                print ( zuzhi )

                writer.writerow ([  date2, all_title[n], intro1,relatedlist, zuzhi, urllj, source_href] )
                time.sleep ( 1 )

        except:
            print ( "无新闻" )
page0()
# page(2)
# page(3)
# page(4)
# page(5)
# page(6)
# page(7)
# page(8)
# page(9)
# page(10)
# page(11)
# print(11,"next")
# pagenext(12,1)  #12
# pagenext(8,0)  #13
# pagenext(9,0)   #14
# pagenext(10,0)   #15
# pagenext(11,0)   #16
# pagenext(12,0)   #17
# pagenext(13,17)   #18
# pagenext(8,18)   #19
# pagenext(9,18)   #20
# pagenext(10,18)   #21
# pagenext(11,18)   #22
# pagenext(12,18)   #23

end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟








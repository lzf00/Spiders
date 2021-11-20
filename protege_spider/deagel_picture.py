# -*- codeing = utf-8 -*-
# @Time : 2021/9/27 10:44
# @Author : lzf
# @File : deagel_picture.py
# @Software :PyCharm
#driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[0] )
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
from selenium.webdriver.chrome.options import Options
import numpy as np
from selenium.webdriver.common.by import By

begin = time.time()
def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
def Picture(filepath,imgpath):
    d = pd.read_csv ( filepath, usecols=['name'] )  # pandas读文件某一列
    print(d)
    context = []
    num=1
    for key in d['name'][0:]:
        # if num<139:
        print ( num, ":::", key )
        url = 'https://www.deagel.com/photo' #https://www.deagel.com/news

        # chrome_options1 = Options ()
        # chrome_options1.add_argument ( 'headless' )
        # chrome_options1.add_argument ( 'disable-gpu' )
        # driver = webdriver.Chrome ( chrome_options=chrome_options1 )
        try:
            driver = webdriver.Chrome ()
            # url='https://www.deagel.com/Offensive%20Weapons'
            driver.get ( url )
            driver.maximize_window ()
            # time.sleep(3)
            driver.implicitly_wait ( 2 )
            try:
                driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
            except:
                print("111")
            driver.find_element_by_xpath ( '//html/body/app-root/div/div/app-photo/div/div[2]/div[3]/div[1]/div/input' ).send_keys ( key )  #输入武器关键词
            driver.find_element_by_xpath ( '//div[@class="input-group-prepend"]/span' ).click ()
            time.sleep ( 3 )
            for i in range(0,5):
                js = "var q=document.documentElement.scrollTop=2000"  # 下拉滑轮—— 0,10000
                driver.execute_script ( js )
                time.sleep ( 0.5 )

            time.sleep ( 1 )
            html = driver.page_source
            # html = html1.read ().decode ( "utf-8" )
            # html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup ( html, 'html.parser', from_encoding='utf-8' )  # 解析网页
            allphoto = soup.find ( 'div', {'class', 'col-12 card-deck card-photo'} )  # col-12 card-deck card-news
            #time.sleep ( 1 )
            allname = allphoto.find_all ( 'div', {'class', 'card-body'} )

            for x in allname:
                name=x.text
                if name==key:
                    print(key,":::",name)
            # js = "var q=document.documentElement.scrollTop=5000"  # 下拉滑轮—— 0,10000
            # driver.execute_script ( js )
            # time.sleep ( 3 )
            photos = allphoto.find_all ( 'img' )  # 新闻href
            #print(photos)
            if len(photos)==0:
                context.append ( key )

            off=1
            off1=1
            for photo in photos:
              if off==1  :
                imgurl=photo.get("src")
                alt=photo.get("alt")
                #print(alt)
                if key in alt:

                    imgurl1="https://www.deagel.com/"+imgurl
                    print(imgurl1)

                    dataimg = urllib.request.urlopen ( imgurl1 ).read ()
                    key=key.replace('/','.')
                    id=create_id()
                    imgname=key+'-'+id+'.png'
                    context.append ( imgname)
                    print(context)
                    f = open ( imgpath +key+'-'+id+'.png', 'wb' )
                    f.write ( dataimg )
                    off=0
                    #f.close ()
                else:
                    if key not in context:
                        if off1==1:
                            context.append ( key )
                            print("else:::",key)
                            off1=0

            num=num+1
            driver.close()
        except:
            print("网络错误")
    try:
        data = pd.read_csv ( filepath )  # pandas读文件某一列
        # print ( data )
        print ( data.columns )  # 获取列索引值
        data1 = context  # 获取列名为flow的数据作为新列的数据
        #context.append ( "xxx ")
        print(len(context))
        print("context:::",context)
        data['picture'] = data1  # 将新列的名字设置为cha
        data.to_csv ( filepath, mode='w', index=False ,encoding='utf-8')
        # mode=a，以追加模式写入,header表示列名，默认为true,index表示行名，默认为true，再次写入不需要行名
        print ( data )
    except:
        print("写入错误")
    end = time.time ()
    print ( '运行时间：', (end - begin) / 60 )  # 50分钟



#Picture('D:\All_Script\Python_deagel\wuqi924/Missile.csv','D:\All_Script\Python_deagel\Img\Missile/')
# Picture('D:\All_Script\Python_deagel\wuqi924/Nucleus-Warhead.csv','D:\All_Script\Python_deagel\Img\he/')
#Picture('D:\All_Script\Python_deagel\wuqi924/Naval.csv','D:\All_Script\Python_deagel\Img\hai/')
#Picture('D:\All_Script\Python_deagel\wuqi924/Electromagnetism.csv','D:\All_Script\Python_deagel\Img\Electromagnetism/')
#Picture('D:\All_Script\Python_deagel\wuqi924/Radar.csv','D:\All_Script\Python_deagel\Img\Radar/')
#Picture('D:\All_Script\Python_deagel\wuqi924/Anti-Missile.csv','D:\All_Script\Python_deagel\Img\Anti-Missile/')

#Picture('D:\All_Script\Python_deagel\wuqi924/Ground-Force.csv','D:\All_Script\Python_deagel\Img\Ground-Force/')
Picture('D:\All_Script\Python_deagel\wuqi924/Air-Force.csv','D:\All_Script\Python_deagel\Img\Air-Force/')

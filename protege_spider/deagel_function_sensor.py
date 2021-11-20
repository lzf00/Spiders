# -*- codeing = utf-8 -*-
# @Time : 2021/8/23 10:28
# @Author : lzf
# @File : deagel_missile.py
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
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

begin = time.time()

def deagel(file_path,url,usa):
    #file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open(file_path, 'w', encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['id','key','group',"key_V","content","href",'param'])

    chrome_options1 = Options ()
    chrome_options1.add_argument ( 'headless' )
    chrome_options1.add_argument ( 'disable-gpu' )
    driver = webdriver.Chrome ( chrome_options=chrome_options1 )

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
    driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/div/div/ul/li['+str(usa)+']/label' "").click ()
    #点击操作员，美国
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
    # li_n=soup.find('div',{'class','dropdown-menu show'})
    # li_n1=li_n.find_all('li',{'class','ng-star-inserted'})
    # print('选美国',":::::::::::::::::::::::::::::::::::::::::::::::",len(li_n1))
    #driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[4]/app-table-filter/div/div/div/ul/li['+str(-1)+']/label' "").click ()

    uls1 = soup.find('tbody')
    #print(uls1)
    tds=uls1.find_all('td',{'class','pl-3'})
    groups=uls1.find_all('td',{'class','d-none d-md-table-cell'})
    j=0
    all_href=[]
    all_name=[]
    all_type=[]
    all_name1=[]
    for group in groups:
        type=group.text
        #print ( type )
        all_type.append ( type )


    for td in tds:
        a = td.find ( 'a' )
        href = a.get ( 'href' )
        if href not in all_href:
            all_href.append ( href )

            name = a.get_text ()
            all_name.append ( name )
        # print(href)
            print ( name )
            j = j + 1


    for i in range(0,len(all_href)):
    #for i in range ( 0, 10):

        url1 = 'https://www.deagel.com/'+all_href[i]
        #print('href:',all_href[i])
        print(i,':::',url1)
        driver.get(url = url1)
        time.sleep(1)
        try:
            driver.find_element_by_xpath ( '//div[@class="col-12 col-xl-10 bg-white"]/div[4]/ul/li[2]/a' ).click ()#点击武器规格
        except:
            print ( '无武器规格' )
        try:
            html = driver.page_source
            #html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8') #解析网页

            ehtml = etree.HTML ( html,parser=etree.HTMLParser(encoding='utf-8'))
            intro = ehtml.xpath('//div[@class="row mt-5"]/div//text()')
            intro1 = '\n'.join(intro).strip()  #用回车符将列表里的每个元素进行分割
            #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyy',intro)
            #table = soup.find('div',{'class':'row mt-5'}) #所有文本内容
            #print(table)

            print(all_name,all_type,url)
            params = soup.find ( 'div', {'class': 'table-responsive table-hover eq-spec mt-3'} )

            #divname = soup.find ( 'div', {'class': 'row mt-5'} )#从简介中提取武器版本名
        except:
            print("网站错误")

        try:

            ths = params.find_all ( 'th', {'class': 'ng-star-inserted'} ) #从参数中提取武器名

            all_thname = []
            all_param = []
            for th in ths:
                thname = th.text
                print ( thname )  # 武器各种版本的名字
                all_thname.append ( thname )

            #收集武器信息
            context = [[] for i in range ( 100 )]
            xtext = []
            xname=[]
            # for ns in range ( len ( ths ) ):
            for ii in range ( len ( intro ) ):
                # xtext.append(0)
                if intro[ii] in all_thname:
                    # print ( ii, ':::', intro[ii] )
                    if intro[ii] not in xname:
                        xname.append ( intro[ii] )
                        xtext.append ( ii )

            if intro[xtext[0]]==intro[xtext[1]] :
                del xtext[0]

            xtext.insert ( 0, 0 )
            xtext.append ( len ( intro ) )
            print ( len ( xtext ) )
            for it in range ( 2, len ( xtext ) ):
                for x in range ( xtext[it - 1], xtext[it] ):
                    context[it].append ( intro[x] )
                context[it] = '\n'.join ( context[it] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
                print ( "it:::",it,context[it] )  #分离各武器信息
            off=0
        except:
            off=1
            print('无武器版本名字和信息')
            print ( i, '单一版本武器', url1 )
            context1 = []
            for io in range ( 0, len(intro) ):
                context1.append ( intro[io] )
            context1 = '\n'.join ( context1 ).strip ()
            print ( "武器原始信息：：：", context1 )

            #写参数
            try:
                trs = params.find_all ( 'tr', {'class', 'ng-star-inserted'} )  # 参数
                sensor=0
            except:
                print ( '无参数' )
                sensor=1
            if sensor==0: #说明有参数
                for tr in trs:   #len(trs)参数个数
                    tds = tr.find_all ( 'td' )
                    tdx = 0

                    for td in tds:
                        tdparam = td.text
                        #print ( tdparam )  # 武器各种版本的参数
                        all_param.append ( tdparam )
                        tdx = tdx + 1  # 武器版本个数

                print ( len ( all_param ) )  #分离参数信息
                print ( len ( all_thname ) )  # 10
                print ( len ( ths ) )  # 10
                print ( len ( trs ) )  # 6+1
                print ( all_param )  # 所有参数
                paramsT = [[] for i in range ( 100 )]
                for ns1 in range ( 1, len ( ths ) + 2 ):
                    for ip in range ( 1, len ( all_param ) ):
                        if ((ip % (len ( all_thname ) + 1)) == ns1):
                            # print ( ip, ":::", all_param[ip] )
                            paramsT[ns1].append ( all_param[ip] )

                        if ((ip % (len ( all_thname ) + 1)) == 0):
                            # print ( ip, ":::", all_param[ip] )
                            paramsT[len ( ths ) + 1].append ( all_param[ip] )
                        # paramsT[ns] = '\n'.join ( paramsT[ns] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
                    paramsT[len ( ths ) + 1] = paramsT[len ( ths ) + 1][:(len ( trs ) - 1)]
                    #print ( paramsT[ns] )  # 分离各武器信息

                for ns in range(len(ths)):
                    a = np.array ( paramsT[1] )
                    b = np.array ( paramsT[ns+2] )
                    dict1 = [{} for i in range ( 100 )]
                    dict1[ns] = dict ( zip ( a, b ) )
                    print ( ns, ':::', dict1[ns] )
                    print(dict1)

                    writer.writerow ( [i, all_name[i], all_type[i], all_name[i], context1, url1, dict1[ns] ] )
            else:
                writer.writerow ( [i, all_name[i], all_type[i], all_name[i], context1, url1,'[]' ])


        if off!=1:
            try:
                trs = params.find_all ( 'tr', {'class', 'ng-star-inserted'} )  # 参数
                param_num=0

                for tr in trs:   #len(trs)参数个数
                    tds = tr.find_all ( 'td' )
                    tdx = 0

                    for td in tds:
                        tdparam = td.text
                        #print ( tdparam )  # 武器各种版本的参数
                        all_param.append ( tdparam )
                        tdx = tdx + 1  # 武器版本个数


                print ( len ( all_param ) )  #分离参数信息
                print ( len ( all_thname ) )  # 10
                print ( len ( ths ) )  # 10
                print ( len ( trs ) )  # 6+1
                print ( all_param )  # 所有参数
                paramsT = [[] for i in range ( 100 )]
                for ns1 in range ( 1, len ( ths ) + 2 ):
                    for ip in range ( 1, len ( all_param ) ):
                        if ((ip % (len ( all_thname ) + 1)) == ns1):
                            # print ( ip, ":::", all_param[ip] )
                            paramsT[ns1].append ( all_param[ip] )

                        if ((ip % (len ( all_thname ) + 1)) == 0):
                            # print ( ip, ":::", all_param[ip] )
                            paramsT[len ( ths ) + 1].append ( all_param[ip] )
                        # paramsT[ns] = '\n'.join ( paramsT[ns] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
                    paramsT[len ( ths ) + 1] = paramsT[len ( ths ) + 1][:(len ( trs ) - 1)]
                    #print ( paramsT[ns] )  # 分离各武器信息

                for ns in range(len(ths)):
                    a = np.array ( paramsT[1] )
                    b = np.array ( paramsT[ns+2] )
                    dict1 = [{} for i in range ( 100 )]
                    dict1[ns] = dict ( zip ( a, b ) )
                    print ( ns, ':::', dict1[ns] )
                    print(dict1)

                    writer.writerow ( [i, all_name[i], all_type[i], all_thname[ns], context[ns+2], url1, dict1[ns] ] )
            except:
                print ( '无参数' )

    print(url,'完成')

# except:
    #     print('无参数')

deagel('D:\All_Script\Python_deagel/Support_Aircraft.csv','https://www.deagel.com/Support%20Aircraft',133)#支援飞机
deagel('D:\All_Script\Python_deagel/Propulsion_Systems.csv','https://www.deagel.com/Propulsion%20Systems',140)#推进系统
deagel('D:\All_Script\Python_deagel/protection.csv','https://www.deagel.com/Protection%20Systems',72)#保护系统

deagel('D:\All_Script\Python_deagel/missile.csv','https://www.deagel.com/Offensive%20Weapons',76)#导弹
deagel('D:\All_Script\Python_deagel/Aircraft.csv','https://www.deagel.com/Combat%20Aircraft',135)#战斗机
deagel('D:\All_Script\Python_deagel/Fships.csv','https://www.deagel.com/Fighting%20Ships',70)#战舰
deagel('D:\All_Script\Python_deagel/defensive.csv','https://www.deagel.com/Defensive%20Weapons',111)#防御性武器


deagel('D:\All_Script\Python_deagel/Armored_Vehicles.csv','https://www.deagel.com/Armored%20Vehicles',139)#装甲车
deagel('D:\All_Script\Python_deagel/Artillery_Systems.csv','https://www.deagel.com/Artillery%20Systems',113)#火炮系统
deagel('D:\All_Script\Python_deagel/Auxiliary_Vessels.csv','https://www.deagel.com/Auxiliary%20Vessels',62)#辅助舰艇
deagel('D:\All_Script\Python_deagel/Space_Systems.csv','https://www.deagel.com/Space%20Systems',32)#空间系统

deagel('D:\All_Script\Python_deagel/Tactical_Vehicles.csv','https://www.deagel.com/Tactical%20Vehicles',116)#战术车辆
deagel('D:\All_Script\Python_deagel/Cannons_Gear.csv','https://www.deagel.com/Cannons%20&%20Gear',152)#大炮和装备
deagel('D:\All_Script\Python_deagel/Sensor.csv','https://www.deagel.com/Sensor%20Systems',83)#传感器（雷达）

#单独处理，武器信息格式不同(ns+3)

end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟

# deagel('D:\All_Script\Python_deagel/Airliners.csv','https://www.deagel.com/Airliners',139)#客机
# deagel('D:\All_Script\Python_deagel/Private_Aircraft.csv','https://www.deagel.com/Private%20Aircraft',131)#私人飞机
#不需要的信息




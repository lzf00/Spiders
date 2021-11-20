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
from selenium.webdriver.chrome.options import Options
import numpy as np


from selenium.webdriver.common.by import By

begin = time.time()

def deagel(file_path,url,usa):
    #file_path = 'D:\All_Script\Python_deagel/missile.csv'
    f = open(file_path, 'w', encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(['id','key','group',"key_V","related","href"])

    # f1 = open ( file_path1, 'w', encoding='utf-8', newline='' )
    # writer1 = csv.writer ( f1 )
    # writer1.writerow ( ['id', 'key', 'group', "key_V", "content", "href", 'param'] )

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
        a=td.find('a')
        href=a.get('href')
        if href not in all_href:
            all_href.append ( href )

            name=a.get_text()
            all_name.append ( name )
            #print(href)
            print(name)
            j = j + 1


    for i in range(0,len(all_href)):

        url1 = 'https://www.deagel.com/'+all_href[i]
        #print('href:',all_href[i])
        print(i,':::',url1)
        driver.get(url = url1)
        time.sleep(1)
        try:
            driver.find_element_by_xpath ( '//div[@class="col-12 col-xl-10 bg-white"]/div[4]/ul/li[3]/a' ).click ()#点击武器相关
        except:
            print ( '无related' )
        try:
            html = driver.page_source
            #html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
            soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8') #解析网页

            ehtml = etree.HTML ( html ,parser=etree.HTMLParser(encoding='utf-8'))
            intro = ehtml.xpath('//*[@id="tab_applications"]/div/table/tbody//text()')
            print(intro)
            #intro1 = '\n'.join(intro).strip()  #用回车符将列表里的每个元素进行分割

            #print(all_name,all_type,url)

            relateds = soup.find ( 'div', {'id': 'tab_applications'} )
            related=relateds.find('tbody')
            trs=related.find_all('tr')
            ths=relateds.find_all('th')
            all_thname=[]
            all_trname=[]
            for tr in trs:
                trname=tr.text  #所有消息
                print(trname)
                all_trname.append(trname)

            for th in ths:
                thname=th.text
                print("相关武器：：：",thname)
                all_thname.append(thname)

            context = [[] for i in range ( 100 )]
            xtext=[]
            for xx in range (0,len(intro)):
                if intro[xx] in all_thname:
                    xtext.append(xx)

            xtext.append ( len ( intro ) )
            print ( len ( xtext ) )
            for it in range ( 1, len ( xtext ) ):
                for x in range ( xtext[it - 1], xtext[it] ):
                    if intro[x] == 'Active' :
                        print ( "Active" )
                    elif intro[x] == 'Cancelled':
                        print("Cancelled")
                    elif intro[x] == 'Under Development':
                        print('UD')
                    elif intro[x] == 'Retired':
                        print('Retired')
                    else:
                        context[it].append ( intro[x] )


                context[it] = '\n'.join ( context[it] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
                print ( "it:::", it, context[it] )  # 分离各武器信息

                writer.writerow ( [i, all_name[i], all_type[i], all_thname[it-1], context[it],url1  ] )

        except:
             print ( "无tbody" )

    print(url,'完成')


#deagel('D:\All_Script\Python_deagel/missile_re.csv','https://www.deagel.com/Offensive%20Weapons',76)#导弹
deagel('D:\All_Script\Python_deagel/Aircraft_re.csv','https://www.deagel.com/Combat%20Aircraft',135)#战斗机
deagel('D:\All_Script\Python_deagel/Fships_re.csv','https://www.deagel.com/Fighting%20Ships',70)#战舰
deagel('D:\All_Script\Python_deagel/defensive_re.csv','https://www.deagel.com/Defensive%20Weapons',111)#防御性武器
deagel('D:\All_Script\Python_deagel/protection_re.csv','https://www.deagel.com/Protection%20Systems',72)#保护系统

deagel('D:\All_Script\Python_deagel/Support_Aircraft_re.csv','https://www.deagel.com/Support%20Aircraft',133)#支援飞机
deagel('D:\All_Script\Python_deagel/Armored_Vehicles_re.csv','https://www.deagel.com/Armored%20Vehicles',139)#装甲车
deagel('D:\All_Script\Python_deagel/Artillery_Systems_re.csv','https://www.deagel.com/Artillery%20Systems',113)#火炮系统
deagel('D:\All_Script\Python_deagel/Auxiliary_Vessels_re.csv','https://www.deagel.com/Auxiliary%20Vessels',62)#辅助舰艇
deagel('D:\All_Script\Python_deagel/Space_Systems_re.csv','https://www.deagel.com/Space%20Systems',32)#空间系统

deagel('D:\All_Script\Python_deagel/Tactical_Vehicles_re.csv','https://www.deagel.com/Tactical%20Vehicles',116)#战术车辆
deagel('D:\All_Script\Python_deagel/Cannons_Gear_re.csv','https://www.deagel.com/Cannons%20&%20Gear',152)#大炮和装备
deagel('D:\All_Script\Python_deagel/Propulsion_Systems_re.csv','https://www.deagel.com/Propulsion%20Systems',140)#推进系统
deagel('D:\All_Script\Python_deagel/Sensor_re.csv','https://www.deagel.com/Sensor%20Systems',83)#传感器（雷达）


#单独处理，武器信息格式不同

end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟

# deagel('D:\All_Script\Python_deagel/Airliners.csv','https://www.deagel.com/Airliners',139)#客机
# deagel('D:\All_Script\Python_deagel/Private_Aircraft.csv','https://www.deagel.com/Private%20Aircraft',131)#私人飞机
#不需要的信息




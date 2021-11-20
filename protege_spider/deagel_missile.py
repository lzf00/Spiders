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


from selenium.webdriver.common.by import By

begin = time.time()

file_path = 'D:\All_Script\Python_deagel/missile.csv'
f = open(file_path, 'w', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['id','key','group',"key_V","content","href",'param'])

driver = webdriver.Chrome( )
url='https://www.deagel.com/Offensive%20Weapons'
driver.get(url)
driver.maximize_window()
#time.sleep(3)
driver.implicitly_wait(2)
try:
    driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
except:
    print()
driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[4]/app-table-filter/div/button' ).click ()
driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[4]/app-table-filter/div/div/div/ul/li[23]/label' ).click ()
#driver.find_element_by_xpath ( '//div[@class="table-responsive table-hover guide"]/table/tbody/' )
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
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
    print ( type )
    all_type.append ( type )
    j=j+1

for td in tds:
    a=td.find('a')
    href=a.get('href')
    all_href.append ( href )
    name=a.get_text()
    all_name.append ( name )
    #print(href)
    print(name)

for i in range(0,j):

    url = 'https://www.deagel.com/'+all_href[i]
    #print('href:',all_href[i])
    print(i,':::',url)
    driver.get(url = url)
    time.sleep(1)
    try:
        driver.find_element_by_xpath ( '//div[@class="col-12 col-xl-10 bg-white"]/div[4]/ul/li[2]/a' ).click ()#点击武器规格
    except:
        print('无武器规格')
    html = driver.page_source
    #html =html.replace('<br>',' ')  #用空格替换网页中的换行<br>
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8') #解析网页

    ehtml = etree.HTML ( html )
    intro = ehtml.xpath('//div[@class="row mt-5"]/div//text()')
    intro1 = '\n'.join(intro).strip()  #用回车符将列表里的每个元素进行分割
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyy',intro)
    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',intro1)




    table = soup.find('div',{'class':'row mt-5'}) #所有文本内容
    #print(table)
    #h1s=table.find_all('h1',{'class':'ng-star-inserted'})
    h1s = table.find_all ( 'h1' )
    ps=table.find_all('p',{'class':'ng-star-inserted'})

    all_h1 = []
    all_p = []
    n=1
    for h1 in h1s :
        weaponV=h1.text
        #print(n,":::",weaponV)
        n=n+1
    x=1
    for p in ps :
        ptext=p.text
        #print(x,':::',ptext)
        all_p.append(ptext)
        x=x+1
    print(all_name,all_type,url)

    params = soup.find ( 'div', {'class': 'table-responsive table-hover eq-spec mt-3'} )
    try:

        ths = params.find_all ( 'th', {'class': 'ng-star-inserted'} )
    except:
        print('无版本信息')
    all_thname = []
    all_param = []
    for th in ths:
        thname = th.text
        print ( thname )  # 武器各种版本的名字
        all_thname.append ( thname )


    try:
        trs = params.find_all ( 'tr', {'class', 'ng-star-inserted'} )  # 参数
        param_num=0

        for tr in trs:   #len(trs)参数个数
            tds = tr.find_all ( 'td' )
            tdx = 0

            for td in tds:
                tdparam = td.text
                print ( tdparam )  # 武器各种版本的参数
                all_param.append ( tdparam )
                tdx = tdx + 1  # 武器版本个数


        context = [[] for i in range ( 100 )]
        xtext = []
        # for ns in range ( len ( ths ) ):
        for ii in range ( len ( intro ) ):
            # xtext.append(0)
            if intro[ii] in all_thname:
                print ( ii, ':::', intro[ii] )
                xtext.append ( ii )

        xtext.insert ( 0, 0 )
        xtext.append ( len ( intro ) )
        print ( len ( xtext ) )
        for it in range ( 2, len ( xtext ) ):
            for x in range ( xtext[it - 1], xtext[it] ):
                context[it].append ( intro[x] )
            context[it] = '\n'.join ( context[it] ).strip ()  # 用回车符将列表里的每个元素进行分割,并将列表变为字符串
            print ( context[it] )  #分离各武器信息


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

            writer.writerow ( [i, all_name[i], all_type[i], all_thname[ns], context[ns+2], url, dict1[ns] ] )


    except:
        print ( '无参数' )

# except:
    #     print('无参数')



end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟





# -*- codeing = utf-8 -*-
# @Time : 2020/12/7 10:39
# @Author : lzf
# @File : Vessel_MMSI.py
# @Software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
d = pd.read_csv('D:\All_Script\Python_vessel_MMSI/mmsi1.csv', encoding ='UTF-8',usecols=['MMSI'])#pandas读文件某一列
print(d)
file_path = 'D:\All_Script\Python_vessel_MMSI/MMSI.csv'
file_path1 = 'D:\All_Script\Python_vessel_MMSI/MMSIlast.csv'
f = open(file_path, 'a', encoding='utf-8',newline='')
f1 = open(file_path1, 'a', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['key', 'port', 'arriver', 'port_time'])
writer1 = csv.writer(f1)
writer1.writerow(['key','lasttime','lastrep'])
x=0
for key1 in d['MMSI']:

        print(x,'::',key1,"----------------------------")
        x=x+1
        driver = webdriver.Chrome('D:\chromedriver.exe')
        url='https://www.vesselfinder.com'
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)
        driver.implicitly_wait(5)
        #key='338912000'

        try:
         driver.find_element_by_xpath('//div[@class="pprem_col lpprc"]/button').click()  #同意按钮
        except:
            print('button')
        time.sleep(5)
        key=str(key1)
        #print(type(key))
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[0] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[1] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[2] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[3] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[4] )
        time.sleep(1)
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[5] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[6] )
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[7] )
        time.sleep(1)
        driver.find_element_by_xpath ( '//div[@class = "oERgz"]/input' ).send_keys ( key[8] )

        time.sleep(5)
        try :
           driver.find_element_by_xpath('//div[@class="_187jq"]').click()
        except:
            print(key,":无此呼号信息")
            #writer.writerow ( [key] )
            driver.close()
            continue

        time.sleep(1)
        try:
         driver.find_element_by_xpath('//div[@class="pprem_col lpprc"]/button').click()  #同意按钮pprem_col lpprc
        except:
            print('button')
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        #print(soup)
        try:
            lastrep = soup.find('td',{'id':'lastrep'}).get('data-title')  #最后时间
        except:
            print(key,":无lastrep信息")
            print(lastrep)
        lastinfo0 = soup.find('p',{'class':'text2'}).text  #位置信息
        lastinfo = lastinfo0.strip()
        lastinfo = lastinfo.replace("\n", " ")
        lastinfo = lastinfo.replace("\r", " ")
        print(lastinfo)
        writer1.writerow ( [key, lastrep,lastinfo] )

        info = soup.find('tbody',{'id':'port-calls'})
        try:
           infos=info.find_all('tr')
        except:
            print ( key, ":此船无历史信息" )
            #writer.writerow ( [key,'0','0','0',lastrep,lastinfo] )

        for item in infos:
            try:
                tds = item.find_all ( 'td' )
                port0=item.find ( 'td', {'class': 'n3 n3ata'} )
                port=port0.find('a').get('href')
                port2=port.split('-')[0]
                port1=port2.split('/')[2]
                print(port1)
                arriver = tds[1].string
                print(arriver)
                port_time = tds[2].string
                print(port_time)
            except:
                print('---')
            writer.writerow ( [key, port1, arriver, port_time] )









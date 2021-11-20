# -*- codeing = utf-8 -*-
# @Time : 2020/12/7 10:39
# @Author : lzf
# @File : Vessel_MMSI.py
# @Software :PyCharm
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time, hashlib
begin=time.time()
d = pd.read_csv('D:\All_Script\Python_vessel_MMSI/mmsi45.csv', encoding ='UTF-8',usecols=['MMSI'])#pandas读文件某一列
print(d)
file_path = 'D:\All_Script\Python_vessel_MMSI/MMSI_7.9.csv'
file_path1 = 'D:\All_Script\Python_vessel_MMSI/MMSIlast_7.9.csv'
f = open(file_path, 'a', encoding='utf-8',newline='')
f1 = open(file_path1, 'a', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['key', 'port', 'arriver', 'port_time'])
writer1 = csv.writer(f1)
writer1.writerow(['key','lasttime','lastrep','picture'])
def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
x=0
for key1 in d['MMSI']:

        print(x,'::',key1,"----------------------------")
        x=x+1
        driver = webdriver.Chrome( )
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
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[0] )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[1] )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[2] )
        time.sleep ( 1 )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[3] )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[4] )
        time.sleep(1)
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[5] )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[6] )
        time.sleep ( 1 )
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[7] )
        time.sleep(1)
        driver.find_element_by_xpath ( '//div[@class = "_1ynDQ"]/input' ).send_keys ( key[8] )

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
        time.sleep(1)
        try:
            lastinfo0 = soup.find('p',{'class':'text2'}).text  #位置信息
            lastinfo = lastinfo0.strip()
            lastinfo = lastinfo.replace("\n", " ")
            lastinfo = lastinfo.replace("\r", " ")
            print(lastinfo)
            picture=key+'_'+create_id()+'.png'
            print(picture)
        except:
            print('无lastrep1')
        writer1.writerow ( [key, lastrep,lastinfo,picture] )

        info = soup.find('div',{'id':'port-calls'})
        try:
           infos=info.find_all('div')
        except:
            print ( key, ":此船无历史信息" )
            #writer.writerow ( [key,'0','0','0',lastrep,lastinfo] )

        for item in infos:
            try:

                port0=item.find ( 'a', {'class': 'flx _rLk t5UW5'} ).text
                #port1=port0.find('span', {'class': 'flag-icon _jFl3'})
                #port1=port.split('/')[2]
                print(port0)
                print('prot')
                arriver0 = item.find ( 'div', {'class': 'flx _1hgmG'} )
                arriver=arriver0.find('div',{'class':'_211eJ'})
                arriver = arriver0.find ( 'div', {'class': '_1GQkK'} ).text
                print ( arriver )
                print('arriver')
                port_time0 = item.find ( 'div', {'class': 'flx _1hgmG'} )
                port_time = port_time0.find ( 'div', {'class': '_2q7TN'} )
                port_time1 = port_time.find ( 'div', {'class': '_1GQkK'} ).text

                print(port_time1)
                print('port_time')
                writer.writerow ( [key, port0, arriver, port_time1] )
            except:
                print('---')
            #writer.writerow ( [key, port1, arriver, port_time] )
            # try:
            #     writer.writerow ( [key, port1, arriver, port_time] )
            # except:
            #    print('无port信息')
        #driver.close()
        href0=soup.find('div',{'id':'map-holder'})
        try:
            href1=href0.find('a').get('href')
            print(href1)
            url1=url+href1
            driver.get ( url1 )#进入截图网站
            time.sleep(2)
            pyautogui.moveTo ( 220, 515, 1 )# 鼠标移动轨迹按钮
            pyautogui.click ()
            #driver.find_element_by_xpath ( '//button[@id="track-req"]' ).click ()  # 轨迹按钮'
            print('qqq')
            time.sleep(2)
            driver.find_element_by_xpath ( '//div[@class="ol-zoom ol-unselectable ol-control"]/button[2]' ).click ()
            print('ttttttt')
            time.sleep(1)
            driver.find_element_by_xpath ( '//div[@class="ol-zoom ol-unselectable ol-control"]/button[2]' ).click ()
            time.sleep(1)
            driver.find_element_by_xpath ( '//div[@class="ol-zoom ol-unselectable ol-control"]/button[2]' ).click ()
            time.sleep(5)
            pyautogui.click ()
            time.sleep (1)
            pyautogui.click ()
            time.sleep ( 1 )
            pyautogui.screenshot( 'D:\All_Script\Python_vessel_MMSI\MMSI_picture/'+picture ,region=(466, 191, 1145, 704))
            print('111')
        except:
            print('无地图')
end=time.time()
print('运行时间：',(end-begin)/60)  #50分钟

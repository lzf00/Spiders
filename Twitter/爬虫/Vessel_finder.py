# -*- codeing = utf-8 -*-
# @Time : 2020/11/26 15:01
# @Author : lzf
# @File : Vessel_finder.py
# @Software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedriver.exe')
# url ='https:/www.vesselfinder.com//ports/APRA-GUAM-22041'
# key='APRA'
# url ='https://www.vesselfinder.com/ports/YOKOSUKA-JAPAN-165'
# key='YOKOSUKA'
url ='https://www.vesselfinder.com/ports/SASEBO-JAPAN-78'
key='SASEBO'

driver.get(url)
driver.maximize_window()
time.sleep(2)
tables= driver.find_elements_by_xpath('//table[@class="ships-in-range table is-hoverable is-fullwidth"]')

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
infos = soup.find_all('table',{'class':'ships-in-range table is-hoverable is-fullwidth'})

file_path = 'D:\All_Script\Python_vesselfinder/vesselfinder'+key+'.csv'
f = open(file_path, 'w', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['state', key,'data', 'callsign', 'name', 'type'])

for info in infos:
    info1=(infos[1])
    info2 = (infos[2])
i=0
trs1=info1.find_all('tr')
for item in trs1:
    try:
            if (i == 0):
                i = i + 1
                continue
            else:
                    #tr = item.get_text()
                    #print ( tr )
                    data = item.find ( 'td', {'class': 'etacol'} ).get_text()
                    print ( 'time:', data )
                    print ('--------------')

                    a = item.find('a',{'class':'named-item'})
                    href=a['href']
                    #MMSI=href.split('-')[5]
                    MMSI = href[-9:]
                    print('MMSI:',MMSI)
                    name=item.find ( 'div', {'class': 'named-title'} ).get_text()
                    print('name:',name)
                    type=item.find ('div',{'class':'named-subtitle'}).get_text()
                    print('type:',type)

                    writer.writerow ( ['arrivals',key, data, MMSI, name, type] )

                    print("111111")
                    #data1= item.find_all('td').get_text()

    except:
     print('aaaaaaaaaa')

j=0
trs2=info2.find_all('tr')
for item in trs2:
         try:
             if (j == 0):
                 j = i + 1
                 continue
             else:
                    data1 = item.find_all ( 'td' )
                    time=data1[0].string  # 这里提取第一个值
                    print(time)

                    a = item.find ( 'a', {'class': 'named-item'} )
                    href = a['href']
                    #MMSI1 = href.split ( '-' )[5]
                    MMSI1=href[-9:]

                    print ( 'MMSI:', MMSI1 )

                    name1 = item.find ( 'div', {'class': 'named-title'} ).get_text ()
                    print (' name:',name1 )
                    type1 = item.find ( 'div', {'class': 'named-subtitle'} ).get_text ()
                    print ( 'type',type1 )
                    writer.writerow ( ['departures', key,time, MMSI1, name1, type1] )
         except:
               print('bbbbbbbb')

driver.close()

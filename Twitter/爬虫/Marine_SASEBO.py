# -*- codeing = utf-8 -*-
# @Time : 2020/12/7 11:12
# @Author : lzf
# @File : Marine_SASEBO.py
# @Software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
driver = webdriver.Chrome('D:\chromedriver.exe')
key='SASEBO'
file_path = 'D:\All_Script\Python_MarineT/MarineT1'+key+'.csv'
f = open(file_path, 'a', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['state', 'key','data' ,'callsign', 'name'])
url='https://www.marinetraffic.com/en/data/?asset_type=arrivals_departures&columns=shipname,move_type,port_type,port_name,ata_atd,mmsi,imo,origin_port_atd,ship_type,dwt&port_in|begins|SASEBO|port_in=17936'
driver.get(url)
driver.maximize_window()
time.sleep(5)
try:
   driver.find_element_by_xpath('//div[@class="qc-cmp2-summary-buttons"]/button[2]').click()
except:
    print('button')
time.sleep(1)
driver.find_element_by_xpath('//div[@class="MuiInputBase-root MuiTablePagination-input jss108 MuiTablePagination-selectRoot jss112"]').click()
driver.find_element_by_xpath('//ul[@class="MuiList-root MuiMenu-list MuiList-padding"]/li[2]').click()

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
infoname = soup.find('div',{'class':'ag-pinned-left-cols-container'})
names=infoname.find_all('a',{'class':'ag-cell-content-link'})
shipname1=[]
shipname2=[]
i=1
for name in names:
    if (i%2==1):
      print(name.text)
      #print("----------")
      shipname1.append(name.text)
    i=i+1

j=1
for name in names:
    if (j%2==0):
      print(name.text)
      #("111111111")
      shipname2.append(name.text)
    j=j+1

infos = soup.find('div',{'class':'ag-body-container'})
infommsi1 = infos.find_all ( 'div', {'class': 'ag-row ag-row-no-focus ag-row-even ag-row-no-animation ag-row-level-0'} )
infommsi2= infos.find_all ( 'div',  {'class': 'ag-row ag-row-no-focus ag-row-odd ag-row-no-animation ag-row-level-0'} )
a=0
for mmsi1 in infommsi1:
    #print('11111')
    mmsi = mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[4]
    # y = mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[7]
    print(mmsi.div.div.div.text )
    callsign1 = mmsi.div.div.div.text

    state= mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[0]
    print ( state.div.div.div.text )
    state1 = state.div.div.div.text

    data= mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[3]
    print ( data.div.div.text )
    time1 = data.div.div.text

    writer.writerow ( [state1, key, time1, callsign1, shipname1[a]] )
    a=a+1

b=0
for mmsi2 in infommsi2:
    #print('11111')
    mmsi = mmsi2.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[4]
    # y = mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[7]
    print(mmsi.div.div.div.text )
    callsign=mmsi.div.div.div.text

    state2= mmsi2.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[0]
    print ( state2.div.div.div.text )
    state3=state2.div.div.div.text

    data= mmsi2.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[3]
    print ( data.div.div.text )
    time=data.div.div.text

    writer.writerow ( [state3, key, time,callsign,shipname2[b]] )
    b=b+1




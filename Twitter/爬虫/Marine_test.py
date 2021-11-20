# -*- codeing = utf-8 -*-
# @Time : 2020/12/3 19:11
# @Author : lzf
# @File : Marine_test.py
# @Software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import pandas as pd
driver = webdriver.Chrome('D:\chromedriver.exe')
url ='https://www.marinetraffic.com/en/ais/details/ports/20289/Guam_port:GUAM'
driver.get(url)
driver.maximize_window()
time.sleep(2)
js = "var q=document.documentElement.scrollTop=700"    #下拉滑轮
driver.execute_script ( js )

time.sleep(3)
driver.find_element_by_xpath('//div[@class="qc-cmp2-summary-buttons"]/button[2]').click()
#driver.find_element_by_xpath('//button[@class="sc-ifAKCX ljEJIv"]').click()

time.sleep(4)
driver.find_element_by_xpath('//ul[@class="nav nav-tabs fluidwidth"]/li[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@id="tabs-arr-dep"]/div[3]/a').click()
time.sleep(2)
try:
 driver.find_element_by_xpath('//div[@class="qc-cmp2-summary-buttons"]/button[2]').click()
except:
    print('xxxxx1')
time.sleep(3)

driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-colorInherit"]').click()

#driver.find_element_by_xpath('//div[@class="header-actions"]/button').click()
time.sleep(3)
# driver.find_element_by_xpath('//div[@class="MuiExpansionPanelDetails-root jss130"][1]/div/div/label[9]').click()

driver.find_element_by_xpath('//label[@class="MuiFormControlLabel-root jss134"]').click()
time.sleep(1)
driver.find_element_by_xpath('//label[@class="MuiFormControlLabel-root jss134"]').click()
time.sleep(1)
# driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[3]').click()
# driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[4]').click()
# driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[6]').click()
driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[7]').click()
driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[8]').click()
driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[6]').click()
#driver.find_element_by_xpath('//div[@class="MuiPaper-root MuiExpansionPanel-root jss129 Mui-expanded MuiExpansionPanel-rounded MuiPaper-elevation0 MuiPaper-rounded"]/div[2]/div/div/div//div/div/div/label[10]').click()

driver.find_element_by_xpath('//button[@class="MuiButtonBase-root MuiButton-root MuiButton-contained jss124 MuiButton-containedSecondary MuiButton-containedSizeSmall MuiButton-sizeSmall"]').click()
key='APRA'

file_path = 'D:\All_Script\Python_MarineT/MarineT'+key+'.csv'
f = open(file_path, 'a', encoding='utf-8',newline='')
writer = csv.writer(f)
writer.writerow(['state', 'key','data' ,'callsign', 'name'])


html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
#infos = soup.find_all('div',{'id':'borderLayout_eRootPanel'})

infos = soup.find('div',{'class':'ag-body-container'})
#print(infos)
state=[]
key=[]
time=[]
for div in infos:
    state = div.find ( 'div', {'class': 'ag-cell-content'} ).get_text ()
    print ( 'state:', state )

infommsi1 = infos.find_all ( 'div', {'class': 'ag-row ag-row-no-focus ag-row-even ag-row-no-animation ag-row-level-0'} )
infommsi2= infos.find_all ( 'div', {'class': 'ag-row ag-row-no-focus ag-row-odd ag-row-no-animation ag-row-level-0'} )

for mmsi1 in infommsi1:
    print('11111')
    #mmsi2=mmsi1.find_all('div ',{'class':'ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value'})
    print ( '222222' )
    #print(mmsi2.text)

    x = mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[0]
    # y = mmsi1.select ('div[class="ag-cell ag-cell-not-inline-editing ag-cell-no-focus mt-grid-cell-orientation ag-cell-value"]' )[7]

    y=mmsi1.find_next_sibling ()
    print(x.div.div.div.text )
    print ( y.div.div.div.text )
    #soup.select ( '#pagediv table tbody  tr' )[2].td[1].a
    #mmsi3 = mmsi2.find_all ( 'div', {'class': 'ag-react-container'} )

for div in infos:
    item=div.find_all('div',{'class':'ag-react-container'})
    for it in item:
      #print(it.text)
      #print('aaaaaa')
      data = it.find_all ( 'div', {'class': 'ag-cell-content ag-cell-content-wrap'} )
      for i in data:
        print(i.text)
        time=i.text
        #time.append(time)
        #writer.writerow ( [ key,time ] )


infoname = soup.find('div',{'class':'ag-pinned-left-cols-container'})
names=infoname.find_all('a',{'class':'ag-cell-content-link'})
for name in names:
    print(name.text)
    #print("----------")
    shipname=name.text
    # name.append(name)
# for i in range(len(state)) :



# data1 = {'state':state,'key':key,'data':time,'callsign':'mmsi','name':shipname}
#
# dataframe = pd.DataFrame(data1,columns = ['state','key','date','callsign','name'])
# dataframe.to_csv(f)








#driver.close()
# -*- codeing = utf-8 -*-
# @Time : 2020/12/14 21:08
# @Author : lzf
# @File : Radarbox_ScrapyROTM.py
# @Software :PyCharm
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedriver.exe')
# file_path = 'D:\All_Script\Python_Radarbox/callsignTomodel.csv'
#获取网站信息输入关键字查找
url = 'https://www.radarbox.com'
driver.get(url=url)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('//div[@id = "search"]/button').click()
time.sleep(3)
driver.find_element_by_xpath('//div[@id = "form"]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@id ="by-airport"]').click()
driver.implicitly_wait(5)
key = 'ROTM' #Marine Corps Air Station Futenma，MCAS Futenma——ROTM
driver.find_element_by_xpath('//div[@id = "input-container"]/input').send_keys(key)

driver.find_element_by_xpath('//div[@id = "more-options"]/div/input').send_keys(key)
time.sleep(3)
driver.find_element_by_xpath('//ul[@class = "List__ListStyle-kkoxgo-0 hulxMV"]/li').click()
time.sleep(2)
driver.find_element_by_xpath('//div[@id = "name"]').click()
time.sleep(2)
all_href = []
j = 0
#获取机场起飞降落数据
for i in range(1,3):
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    uls = soup.find_all('ul',{'class','List__ListStyle-kkoxgo-0 AirportFlightList__AirportFlightListStyle-sc-1984pmz-0 dJJPIf'})
    print('00000000')
    for ul in uls:
        print('111111')
        lis = ul.find_all('li')
        print('2222222')
        num = 0
        for li in lis:
            try:
                print('3333333')
                a = li.find('a') #取a标签中的值
                href = a.get('href')
                all_href.append(href)
                print("j:",j)
                print("href:", all_href[j])
                j = j + 1
            except:
                print('没有a标签！')
    driver.find_element_by_xpath('//button[@id ="departures"]').click()
    time.sleep(2)
#获取各个航班的历史数据
file_path = 'D:\All_Script\Python_Radarbox/Radarbox_'+key+'.csv'
f = open(file_path, 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(["time", "origin", "std", "atd", "arrival", "sta", "aircraft", "status", "duration","href","image","trace1"])
for i in range(0,j):

    url = 'https://www.radarbox.com'+all_href[i]
    print('href:',all_href[i])
    driver.get(url = url)
    time.sleep(3)

    html = driver.page_source
    html =html.replace('<br>',' ')
    soup = BeautifulSoup(html,'html.parser') #解析网页
    table = soup.find('table',{'class':'DataTable__DataTableStyle-sc-1v0dawd-0 dyBhEJ'})
    tbody = table.find('tbody')
    trs = tbody.find_all('tr')
    print('999999')

    for tr in trs:
        try:

            trace=tr.get('id')   #得到标签tr中属性id的值
            trace1 = url+'/'+trace.split("_")[0]  #split选用符号“-”切片，取切片后的第0个元素
            print('trace:',trace1)

            image=url.split("/")[5]+'-'+trace.split("_")[0]+'.png'

            date = tr.find('td',{'id':'date'}).text
            print('time:',date)

            origin = tr.find('td',{'id':'departure'}).get_text()
            print('origin:',origin)

            std = tr.find('td',{'id':'std'}).text
            print('std:',std)
            atd = tr.find('td',{'id':'atd'}).text
            print('atd:',atd)

            arrival = tr.find('td',{'id':'arrival'}).text
            print('arrival:',arrival)

            sta = tr.find('td',{'id':'sta'}).text
            print('sta:',sta)

            try:
                aircraft = tr.find('td',{'id':'aircraft'}).text
                print('aircraft:',aircraft)
            except:
                divs = soup.find_all('div', {'id': 'aircraft-info'})
                model = ''
                print('0000000')
                for div in divs:
                    print('1122323')
                    a = div.find_all('a')
                    num = 0
                    for it in a:
                        if num == 0:
                            text = it.text
                            model = text
                            print('model:', model)
                            num = num + 1
                        else:
                            text = it.text
                            Registration = text
                            print('Registration:', Registration)
                            num = num + 1
                            break
                aircraft = model +'('+Registration+')'
                print('no a')


            t = tr.find( 'span', {'id': 'status'} ).text
            print('status:', t )
            duration = tr.find('td',{'id':'duration'}).text
            print('duration:',duration)

            writer.writerow( [date, origin, std , atd, arrival, sta, aircraft, t, duration, all_href[i],image,trace1])
        except:
            print('pass！')





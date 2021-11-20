import time
import datetime
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')

def connent_url(url):
    print('erwerwerw')
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(2)
    print('12')
    driver.find_element_by_id('U').click()
    #缩小地图以看到所有的飞机
    try:
        for y in range(1,10):
            driver.find_element_by_class_name('ol-zoom-out').click()
            print('1212778')
        print('最小状态！')
    except:
        print('缩小失败！')
    print('23')
    #截图保存
    time.sleep(20)
    try:
         driver.get_screenshot_as_file('D:\python_data\southsea/all/ads-b.png')
         print('成功！')
    except:
        print('失败！')
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find_all('td', {'class': 'icaoCodeColumn'})
    print('7686786786')
    for tr in trs:
        print('0000000')
        text = tr.text
        print('flight_num:',text)
        url = 'https://globe.adsbexchange.com/?icao='+text
        get_flight_info(url = url)

def get_flight_info(url):
    driver.get(url = url)
    for y in range(1, 2):
        driver.find_element_by_class_name('ol-zoom-out').click()
    time.sleep(2)
    name = url.split('=')[1]
    try:
         driver.get_screenshot_as_file('D:\python_data\southsea/picture/'+name+'.png')
         print('截图成功！')
    except:
        print('失败！')

def Run():
    connent_url(url='https://globe.adsbexchange.com')
if __name__ == '__main__':
    print('0000')
    Run()
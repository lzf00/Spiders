# -*- codeing = utf-8 -*-
# @Time : 2021/3/22 14:34
# @Author : lzf
# @File : fakenews.py
# @Software :PyCharm

# https://service.account.weibo.com/index?type=5&status=4&page=1
#https://service.account.weibo.com/index?type=5&status=4&page=2
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
#https://service.account.weibo.com/index?type=5&status=4&page=1
driver = webdriver.Chrome( )
# file_path = 'D:\All_Script\Python_Radarbox/callsignTomodel.csv'
#获取网站信息输入关键字查找

user='15972978685'
pwd='19980816lzf..'
# https://service.account.weibo.com/index?type=0&status=4&page=1
url = 'https://service.account.weibo.com/index?type=0&status=4&page=1'
# driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')
driver = webdriver.Chrome ()
driver.maximize_window ()
driver.implicitly_wait ( 10 )
driver.get ( 'https://weibo.com/' )
driver.find_element_by_id ( 'loginname' ).clear ()
driver.find_element_by_id ( 'loginname' ).send_keys ( user )
driver.find_element_by_name ( 'password' ).send_keys ( pwd )
driver.find_element_by_css_selector ( '.W_btn_a.btn_32px' ).click ()
cookies = driver.get_cookies ()

with open ( "cookie.data", "w" ) as f:
    for cookie in driver.get_cookies ():
        # print(cookie)
        f.write (
            str ( cookie ) + "\n"
        )
with open ( "cookie.data", "r" ) as f:
    lis_lines = f.readlines ()

driver.get ( 'https://weibo.com' )
driver.delete_all_cookies ()
for line in lis_lines:
    dic_line = eval ( line.strip () )
    driver.add_cookie ( dic_line )
driver.refresh ()
driver.get ( 'https://weibo.com/u/6085205676/home' )

####

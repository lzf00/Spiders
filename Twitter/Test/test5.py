# -*- codeing = utf-8 -*-
# @Time : 2020/11/22 21:47
# @Author : lzf
# @File : test5.py
# @Software :PyCharm
from selenium import webdriver
from time import sleep
import csv
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

print('Before search================')

# 打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(1)

print('After search================')

# 再次打印当前页面title
title = driver.title
print(title)

# 打印当前页面URL
now_url = driver.current_url
print(now_url)

# 获取结果数目
user = driver.find_element_by_class_name('nums').text
#user = driver.find_element_by_class_name('nums_text').get_text()  #
print(user)

#driver.quit()
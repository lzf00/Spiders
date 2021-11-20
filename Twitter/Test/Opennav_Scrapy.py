# -*- codeing = utf-8 -*-
# @Time : 2020/11/21 21:09
# @Author : lzf
# @File : Opennav_Scrapy.py
# @Software :PyCharm
import click
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
import csv
driver=webdriver.Chrome('D:\chromedriver.exe')
driver.get(url='https://opennav.com/airport/RKPS')
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element_by_name('q').send_keys("U-Tapao Airport")
driver.find_element_by_xpath("//div[@class='searchbar']/input[2]").click()
#driver.find_element_by_xpath("//div[@class='column']/a").click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("html > body > section > div > section >div>div>div>div>a").click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//button[@class="gm-control-active gm-fullscreen-control"]').click()
driver.implicitly_wait(10)
for i in range(0,3):
 driver.find_element_by_xpath('//div[@class="gmnoprint"][2]/div/button[1]').click()  #div[@class="gmnoprint"][2]下找button[1]！！！

time.sleep(3)
today_date=time.strftime('%Y-%m-%d',time.localtime(time.time())) #获得当前时间
driver.get_screenshot_as_file('D:\All_Script\\Python_U-Tapao/'+'U-Tapao1-'+ today_date +'.png')

driver.find_element_by_xpath('//div[@class="gm-style"]/div/div[3]/div/div/div').click()

#ActionChains(driver).move_by_offset(200, 100).click().send_keys(Keys.UP).perform()  #坐标定位，移动+点击！！！
for i in range(0,500):
 ActionChains(driver).click().send_keys(Keys.UP).perform()
driver.get_screenshot_as_file('D:\All_Script\\Python_U-Tapao/'+'U-Tapao2-'+ today_date +'.png')

for i in range(0,900):
 ActionChains(driver).click().send_keys(Keys.DOWN).perform()
driver.get_screenshot_as_file ('D:\All_Script\\Python_U-Tapao/'+'U-Tapao3-'+ today_date +'.png')


# -*- codeing = utf-8 -*-
# @Time : 2020/11/18 20:24
# @Author : lzf
# @File : test2.py
# @Software :PyCharm
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#使用click()单击元素
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()  #单击百度一下

driver.maximize_window()  #设置浏览器全屏显示
#driver.quit()

#使用submit()提交表单，即回车操作
search_text = driver.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
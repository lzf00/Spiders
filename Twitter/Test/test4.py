# -*- codeing = utf-8 -*-
# @Time : 2020/11/18 20:50
# @Author : lzf
# @File : test4.py
# @Software :PyCharm
from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()  #设置浏览器全屏显示
# 定位到要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

#找到链接
elem1=driver.find_element_by_link_text("搜索设置")
elem1.click()

time.sleep(1)

#通过元素选择器找到id=sh_2,并点击设置
elem2=driver.find_element_by_id('sh_1')
elem2.click()

#保存设置
elem3=driver.find_element_by_class_name("prefpanelrestore")
elem3.click()
# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 16:11
# @Author : lzf
# @File : test_javascript.py
# @Software :PyCharm
from selenium import webdriver
from time import sleep

#1.访问百度
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

#2.搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

#3.休眠2s目的是获得服务器的响应内容，如果不使用休眠可能报错
sleep(2)

#4.通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,800);"   #长 ，宽
driver.execute_script(js)



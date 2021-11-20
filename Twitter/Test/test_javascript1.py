# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 16:35
# @Author : lzf
# @File : test_javascript1.py
# @Software :PyCharm
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.set_window_size(400,400)
driver.get("https://www.baidu.com")

#2.搜索
# driver.find_element_by_id("kw").send_keys("selenium")
# driver.find_element_by_id("su").click()

#3.休眠2s目的是获得服务器的响应内容，如果不使用休眠可能报错
sleep(2)

#4 滚动左右滚动条---向右
js2 = "var q=document.documentElement.scrollLeft=10000"
driver.execute_script(js2)
sleep(2)

#5 滚动左右滚动条---向左
js3 = "var q=document.documentElement.scrollLeft=0"
driver.execute_script(js3)
sleep(2)

#6 拖动到滚动条底部---向下
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(2)

#7 拖动到滚动条底部---向上
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(2)




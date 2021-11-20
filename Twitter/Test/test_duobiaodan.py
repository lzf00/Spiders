# -*- codeing = utf-8 -*-
# @Time : 2020/11/23 23:02
# @Author : lzf
# @File : test_duobiaodan.py
# @Software :PyCharm
from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get("http://www.126.com")
time.sleep(2)

#driver.switch_to.frame(0)  #到iframe窗口

i=driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(i)  #第二种方法

driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("15972978685")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("19980816lzf")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()



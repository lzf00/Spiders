# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 15:31
# @Author : lzf
# @File : up_file.py
# @Software :PyCharm
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('up_file.html')
driver.get(file_path)

time.sleep(1)
# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')
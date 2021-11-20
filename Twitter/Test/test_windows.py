# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 15:09
# @Author : lzf
# @File : test_windows.py
# @Software :PyCharm
from selenium import webdriver
import time

driver = webdriver.Chrome ( )
driver.implicitly_wait ( 10 )
driver.get ( "http://www.baidu.com" )
driver.maximize_window()
# 1.获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle

driver.find_element_by_link_text ( '登录' ).click ()
driver.find_element_by_link_text ( "立即注册" ).click ()

# 1.获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 3.进入注册窗口
for handle in all_handles:
    if  handle != sreach_windows:
        driver.switch_to.window ( handle )
        print ( '跳转到注册窗口' )
        time.sleep(2)
        driver.find_element_by_class_name ( "pass-text-input pass-text-input-userName" ).send_keys ( '123456789' )
        driver.find_element_by_class_name ( 'pass-text-input pass-text-input-password pass-text-input-error' ).send_keys ( '123456789' )
        time.sleep ( 2 )



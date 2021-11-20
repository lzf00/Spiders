# -*- codeing = utf-8 -*-
# @Time : 2020/11/24 15:45
# @Author : lzf
# @File : test_cookie.py
# @Software :PyCharm

from selenium import webdriver
import time

browser = webdriver.Chrome ( )
browser.get ( "http://www.youdao.com" )
browser.maximize_window()

# 1.打印cookie信息
print ( '=====================================' )
print ( "打印cookie信息为：" )
print ( browser.get_cookies )
#1可单独执行，所得结果不同

# 2.添加cookie信息
dict = {'name': "lzf", 'value': 'Zoro'}
browser.add_cookie ( dict )

print ( '=====================================' )
print ( '添加cookie信息为：' )
print(dict)
print ( '=====================================' )
# 3.遍历打印cookie信息
print ( '遍历打印所有cookie信息：' )
for cookie in browser.get_cookies ():
    print ( '%s ---- %s\n' % (cookie['name'], cookie['value']) )

# 4.删除一个cookie
browser.delete_cookie ( 'lzf' )
print ( '=====================================' )
print ( '删除一个name为’lzf‘的cookie' )
for cookie in browser.get_cookies ():
    print ( '%s----%s\n' % (cookie['name'], cookie['value']) )

print ( '=====================================' )
print ( '删除所有cookie后：' )
# 5.删除所有cookie,无需传递参数
browser.delete_all_cookies ()
for cookie in browser.get_cookies ():
    print ( '%s----%s\n' % (cookie['name'], cookie['value']) )

time.sleep ( 3 )


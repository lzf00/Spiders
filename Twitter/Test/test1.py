# -*- codeing = utf-8 -*-
# @Time : 2020/11/17 16:43
# @Author : lzf
# @File : test1.py
# @Software :PyCharm

from selenium import webdriver as wd
driver = wd.Chrome()
# driver.get("https://twitter.com/navywatcher451")
#
# #print("设置浏览器宽480、高800显示")
# #driver.set_window_size(480, 800)
driver.maximize_window()  #设置浏览器全屏显示
# driver.refresh() #刷新当前页面


#访问百度首页
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)

#访问新闻页面
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)

#返回（后退）到百度首页
print("back to  %s "%(first_url))
driver.back()  #后退

#前进到新闻页
print("forward to  %s"%(second_url))
driver.forward()  #前进
#driver.quit()



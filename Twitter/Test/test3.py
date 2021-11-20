# -*- codeing = utf-8 -*-
# @Time : 2020/11/18 20:36
# @Author : lzf
# @File : test3.py
# @Software :PyCharm

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得输入框的尺寸
size = driver.find_element_by_id('kw').size
print(size)

# 返回百度页面底部备案信息
text = driver.find_element_by_id("bottom_layer").text
print(text)

# 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

# 返回元素的结果是否可见， 返回结果为 True 或 False
result = driver.find_element_by_id("kw").is_displayed()
print(result)

# 执行上面的程序并查看结果： size 方法用于获取百度输入框的宽、 高，
# text 方法用于获得百度底部的备案信息，
# get_attribute()用于获得百度输入的 type 属性的值，
# is_displayed()用于返回一个元素是否可见， 如果可见则返回 True， 否则返回 False。
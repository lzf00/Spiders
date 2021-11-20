# -*- codeing = utf-8 -*-
# @Time : 2020/11/22 22:45
# @Author : lzf
# @File : test_wait.py
# @Software :PyCharm
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()

# 设置隐式等待为10秒
#implicitly_wait() 默认参数的单位为秒，本例中设置等待时长为10秒。
# 首先这10秒并非一个固定的等待时间，它并不影响脚本的执行速度。
# 其次，它并不针对页面上的某一元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行；
# 如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到。
# 假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常。
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')  #正确id为 kw，此处捕获异常
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    #driver.quit()
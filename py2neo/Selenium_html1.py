# -*- codeing = utf-8 -*-
# @Time : 2021/7/15 17:06
# @Author : lzf
# @File : Selenium_html1.py
# @Software :PyCharm
# coding=utf-8

from selenium import webdriver
import win32api
import win32con
import win32clipboard
from ctypes import *
import time
import os
#　浏览器打开百度网页
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.baidu.com/")

time.sleep(2)
# 获取页面title作为文件名
title = browser.title
# 设置路径为：当前项目的绝对路径+文件名
path = ('D:\All_Script\Janes'+ "\\" + title + ".html")

# 将路径复制到剪切板
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(path)
win32clipboard.CloseClipboard()

# 按下ctrl+s
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x53, 0, 0, 0)
win32api.keybd_event(0x53, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(2)

# 鼠标定位输入框并点击
windll.user32.SetCursorPos(700, 510)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
time.sleep(2)

# 按下ctrl+a
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x41, 0, 0, 0)
win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(2)

# 按下ctrl+v
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x56, 0, 0, 0)
win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
time.sleep(1)

# 按下回车
win32api.keybd_event(0x0D, 0, 0, 0)
win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)

browser.close()
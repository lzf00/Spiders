#-*- codeing = utf-8 -*-
#@Time : 2020/8/28 17:39
#@Author : lzf
#@File : t1.py
#@Software :PyCharm

from bs4 import BeautifulSoup   #网页解析，获取数据
import re     #正则表达式，进行文字匹配
import urllib.request,urllib.error  #制定URL，获取网页数据
import xlwt   #进行excel操作
import sqlite3  #进行SQLite数据库操作
import csv

def add(a,b):
    return a+b
#print(add(3,5))
import scipy.sparse as sp
a=sp.rand(74,5,density=1,).todense()
print(a)
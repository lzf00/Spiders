#-*- codeing = utf-8 -*-
#@Time : 2020/8/29 10:49
#@Author : lzf
#@File : testBs4.py
#@Software :PyCharm

from bs4 import BeautifulSoup

file=open("./baidu.html","rb")
html=file.read().decode("utf-8")
bs=BeautifulSoup(html,"html.parser")

#print(bs.title)
#print((bs.a))

# print(bs.head)
#print(type(bs.head))

#1. Tag  标签及其内容：拿到它所找到的第一个内容

print(bs.title.string)
print(type(bs.title.string))


#2.NavigableString  标签里的内容（字符串）

#print(bs.a.attrs)

# print(bs)
# print(type(bs))


#3.BeautifulSoup  表示整个文档

# print(bs.name)
# print(bs.attrs)  #标签
#
# print(bs.a.string)
# print(type(bs.a.string))


#4.Comment 是一个特殊的NavigableString,输出的内容不包含注释符号

#------------------------------------------

#文档的遍历

#print(bs.head.contents)
#print(bs.head.contents[1])

#更多内容，搜索BeautifulSoup文档



#文档的搜索

#1.find_all()   字符串过滤：会查找与字符串完全匹配的内容
t_list=bs.find_all("a")
#print(t_list)   #输出所有为tag为a的信息

import re
#2.正则表达式搜索：使用search()方法来匹配内容
#t_list=bs.find_all(re.compile("a"))


#3.方法： 传入一个函数（方法），根据函数的要求来搜索  (了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list=bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)   #打印列表

#print(t_list)



#kwargs  参数

#t_list=bs.find_all(id="head")
#t_list=bs.find_all(href="http://news.baidu.com")
#t_list=bs.find_all(class_=True)

# for item in t_list:
#     print(item)


#text参数

#t_list=bs.find_all(text="hao123")
#t_list=bs.find_all(text=["hao123","地图","贴吧"])

# t_list=bs.find_all(text=re.compile("\d"))  #应用正则表达式来查找包含特定文本的内容（标签里的字符串）
# for item in t_list:
#     print(item)


#limit参数

# t_list=bs.find_all("a",limit=3)  #只输出3个
# for item in t_list:
#      print(item)


#css选择器

# t_list=bs.select('title')  #通过标签来查找
#
# t_list=bs.select(".mnav")  #通过类名来查找
#
t_list=bs.select("#u1")   #通过id来查找
print(t_list[0].get_text())

t_list=bs.select("a[class='mnav']")   #通过属性来查找
print(t_list[2].get_text()) #获得文本内容
# t_list=bs.select("a[class='bri']")   #通过属性来查找
#
# t_list=bs.select("head>title")  #通过子标签来查找
#
t_list=bs.select(".mnav~.bri")  #通过兄弟节点来查找
print(t_list[0].get_text()) #获得文本内容

# for item in t_list:
#      print(item)
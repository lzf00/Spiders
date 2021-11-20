#-*- codeing = utf-8 -*-
#@Time : 2020/8/28 18:02
#@Author : lzf
#@File : testUrllib.py
#@Software :PyCharm

import urllib.request

#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码


#获取一个post请求

# import  urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")  #用户名：密码  /  表单封装
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)    #传递data
# print( response.read().decode("utf-8") )

#超时处理
'''
try:

   response=urllib.request.urlopen("http://httpbin.org/get",timeout=0.1) #超时设置
   print(response.read().decode("utf-8"))

except urllib.error.URLError as e:
    print("time out!!!")
'''

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)  #返回状态码
# print("Bdqid:"+response.getheader('Bdqid'))  #获得网页的Response Headers中的一个属性的值
# print(response.getheaders())  #获得网页的Response Headers


# url="http://httpbin.org/post"
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
# }
# data=bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
#
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
#
# response=urllib.request.urlopen(req)
# print( response.read().decode("utf-8") )


url="http://www.douban.com"
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}   #浏览器的用户信息, 加双引号将信息变成字符串（字典类型）

req=urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
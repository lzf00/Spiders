# -*- codeing = utf-8 -*-
# @Time : 2021/11/11 13:23
# @Author : lzf
# @File : sousuoyemian.py
# @Software :PyCharm
from urllib.request import urlopen
from urllib.request import Request
from fake_useragent import UserAgent
from urllib.parse import urlencode

#设置request header
ua = UserAgent()
headers = {
    "User-Agent":ua.random
}
#拼接url
args = {
    "ie":"utf-8",
    "wd":"博客园"
}
url = "https://www.baidu.com/s?{}".format(urlencode(args))

#封装request
request = Request(url,headers=headers)

# 发送请求，获取服务器给的响应
response = urlopen(request)

# 读取结果,无法正常显示中文
html = response.read()

# 进行解码操作，转为utf-8
html_decode = html.decode()

# 打印结果
print(html_decode)
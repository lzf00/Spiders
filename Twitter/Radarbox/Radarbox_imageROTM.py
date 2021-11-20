# -*- codeing = utf-8 -*-
# @Time : 2020/11/30 20:11
# @Author : lzf
# @File : Radarbox_image.py
# @Software :PyCharm
import csv
import pandas as pd
import time
import time, hashlib
from selenium import webdriver
# with open('D:\All_Script\Python_Radarbox/Radarbox_UAM.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     trace=[1000]
#     trace = [row[10]for row in reader]
#     print(trace)
d = pd.read_csv('D:\All_Script\Python_Radarbox/Radarbox_ROTM_clean1_f1.csv', usecols=['trace1'])#pandas读文件某一列
print(d)
driver=webdriver.Chrome('D:\chromedriver.exe')
driver.maximize_window()

def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
print ( type ( create_id () ) )
print ( create_id () )

for i in d['trace1']:   #d【‘trace1’】：取trace1这一列中的每个元素
    try:
       print(i)
       driver.get(url=i)
       time.sleep ( 4 )
       js = "var q=document.documentElement.scrollTop=85"    #下拉滑轮
       driver.execute_script ( js )
       time.sleep ( 4 )
       a=i.split ( "/" )[6]
       b = i.split ( "/" )[5]
       print(a)
       driver.get_screenshot_as_file ( 'D:\All_Script\Python_Radarbox\Image_ROTM/'+ b+'-'+a +'-'+create_id()+'.png' )
       print('----------------------------------')
    except:
        print('-------------')




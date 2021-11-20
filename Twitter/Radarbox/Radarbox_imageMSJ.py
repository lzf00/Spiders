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
begin_time = time.time()
d = pd.read_csv('D:\All_Script\Python_Radarbox/Radarbox_MSJ_clean1_f1.csv', usecols=['trace1'])#pandas读文件某一列
print(d)
d1 = pd.read_csv('D:\All_Script\Python_Radarbox/Radarbox_MSJ_clean1_f1.csv', usecols=['image'])
print(d1)
driver=webdriver.Chrome( )
driver.maximize_window()

def create_id():
    m = hashlib.md5 ()
    m.update ( bytes ( str ( time.perf_counter() ), encoding='utf-8' ) )
    return m.hexdigest ()
print ( type ( create_id () ) )
print ( create_id () )
name=[]
for x in d1['image']:

    print(x)
    #print("----------")
    name.append(x)
a=0
for i in d['trace1']:   #d【‘trace1’】：取trace1这一列中的每个元素
    try:
       #print(i)
       driver.get(url=i)
       time.sleep ( 4 )
       js = "var q=document.documentElement.scrollTop=85"    #下拉滑轮
       driver.execute_script ( js )
       time.sleep ( 4 )
       # a=i.split ( "/" )[6]
       # b = i.split ( "/" )[5]
       print(i)
       driver.get_screenshot_as_file ( 'D:\All_Script\Python_Radarbox\Image_MSJ/'+ name[a] )
       a=a+1
       print(a)
       print('----------------------------------')
    except:
        print('-------------')
end_time=time.time()
print("运行时间：",(end_time-begin_time)/60,'min')



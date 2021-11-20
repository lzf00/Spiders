# -*- codeing = utf-8 -*-
# @Time : 2021/8/26 11:12
# @Author : lzf
# @File : operate_num.py
# @Software :PyCharm
# -*- codeing = utf-8 -*-
# @Time : 2021/8/23 10:28
# @Author : lzf
# @File : deagel_missile.py
# @Software :PyCharm
import csv
from tokenize import String

import pandas as pd
import time, hashlib
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from time import *
import time
import numpy as np
from selenium.webdriver.common.by import By
begin = time.time()

def deagel(file_path,url):
    #file_path = 'D:\All_Script\Python_deagel/missile.csv'
    # f = open(file_path, 'w', encoding='utf-8',newline='')
    # writer = csv.writer(f)
    # writer.writerow(['id','key','group',"key_V","content","href",'param'])

    driver = webdriver.Chrome( )
    #url='https://www.deagel.com/Offensive%20Weapons'
    driver.get(url)
    driver.maximize_window()
    #time.sleep(3)
    driver.implicitly_wait(2)
    try:
        driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
    except:
        print()
    driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()
    #driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/div/div/ul/li['+str(usa)+']/label' "").click ()
    #点击操作员，美国

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser',from_encoding='utf-8')
    li_n=soup.find('div',{'class','dropdown-menu show'})
    li_n1=li_n.find_all('li',{'class','ng-star-inserted'})
    print('国家数量:::',url,":::",len(li_n1)+1)
    #driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[4]/app-table-filter/div/div/div/ul/li['+str(-1)+']/label' "").click ()



def deagel1(file_path, url,num ):

    driver = webdriver.Chrome ()
    #url='https://www.deagel.com/Offensive%20Weapons'
    driver.get ( url )
    driver.maximize_window ()
    # time.sleep(3)
    driver.implicitly_wait ( 2 )
    try:
        driver.find_element_by_xpath ( '//div[@id="gdpr_message"]/button' ).click ()  # 同意按钮
    except:
        print ()
    driver.find_element_by_xpath ( '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/button' ).click ()
    # driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/div/div/ul/li['+str(usa)+']/label' "").click ()
    # 点击操作员，美国
    for x in range (1,num):
        USA=driver.find_element_by_xpath ( "" '//thead[@class="thead-dark"]/tr/th[5]/app-table-filter/div/div/div/ul/li['+str(x)+']/label' "").get_attribute('textContent')
        #print(x,":::",USA)
        if (str(USA) == (' United States of America')):
            print(USA,url,":::::",x)






# except:
    #     print('无参数')
# deagel('D:\All_Script\Python_deagel/missile.csv','https://www.deagel.com/Offensive%20Weapons',80)#导弹
# deagel('D:\All_Script\Python_deagel/Aircraft.csv','https://www.deagel.com/Combat%20Aircraft',143)#战斗机
# deagel('D:\All_Script\Python_deagel/Sensor.csv','https://www.deagel.com/Sensor%20Systems',88)#传感器（雷达）
# deagel('D:\All_Script\Python_deagel/Fships.csv','https://www.deagel.com/Fighting%20Ships',74)#战舰
# deagel('D:\All_Script\Python_deagel/defensive.csv','https://www.deagel.com/Defensive%20Weapons',119)#防御性武器
# deagel('D:\All_Script\Python_deagel/protection.csv','https://www.deagel.com/Protection%20Systems',75)#保护系统
#
# deagel('D:\All_Script\Python_deagel/Airliners.csv','https://www.deagel.com/Airliners',147)#客机
# deagel('D:\All_Script\Python_deagel/Private_Aircraft.csv','https://www.deagel.com/Private%20Aircraft',137)#私人飞机
# deagel('D:\All_Script\Python_deagel/Support_Aircraft.csv','https://www.deagel.com/Support%20Aircraft',140)#支援飞机
# deagel('D:\All_Script\Python_deagel/Tactical_Vehicles.csv','https://www.deagel.com/Tactical%20Vehicles',120)#战术车辆
# deagel('D:\All_Script\Python_deagel/Armored_Vehicles.csv','https://www.deagel.com/Armored%20Vehicles')#装甲车
# deagel('D:\All_Script\Python_deagel/Artillery_Systems.csv','https://www.deagel.com/Artillery%20Systems')#火炮系统
# deagel('D:\All_Script\Python_deagel/Auxiliary_Vessels.csv','https://www.deagel.com/Auxiliary%20Vessels')#辅助舰艇
# deagel('D:\All_Script\Python_deagel/Space_Systems.csv','https://www.deagel.com/Space%20Systems')#空间系统
deagel('D:\All_Script\Python_deagel/Cannons_Gear.csv','https://www.deagel.com/Cannons%20&%20Gear')#大炮和装备
# deagel('D:\All_Script\Python_deagel/Propulsion_Systems.csv','https://www.deagel.com/Propulsion%20Systems')#推进系统


# deagel1('D:\All_Script\Python_deagel/missile.csv','https://www.deagel.com/Offensive%20Weapons',80)#导弹
# deagel1('D:\All_Script\Python_deagel/Aircraft.csv','https://www.deagel.com/Combat%20Aircraft',143)#战斗机
# deagel1('D:\All_Script\Python_deagel/Sensor.csv','https://www.deagel.com/Sensor%20Systems',88)#传感器（雷达）
# deagel1('D:\All_Script\Python_deagel/Fships.csv','https://www.deagel.com/Fighting%20Ships',74)#战舰
# deagel1('D:\All_Script\Python_deagel/defensive.csv','https://www.deagel.com/Defensive%20Weapons',119)#防御性武器
# deagel1('D:\All_Script\Python_deagel/protection.csv','https://www.deagel.com/Protection%20Systems',75)#保护系统
#
# deagel1('D:\All_Script\Python_deagel/Airliners.csv','https://www.deagel.com/Airliners',147)#客机
# deagel1('D:\All_Script\Python_deagel/Private_Aircraft.csv','https://www.deagel.com/Private%20Aircraft',137)#私人飞机
# deagel1('D:\All_Script\Python_deagel/Support_Aircraft.csv','https://www.deagel.com/Support%20Aircraft',140)#支援飞机
# deagel1('D:\All_Script\Python_deagel/Tactical_Vehicles.csv','https://www.deagel.com/Tactical%20Vehicles',120)#战术车辆
# deagel1('D:\All_Script\Python_deagel/Armored_Vehicles.csv','https://www.deagel.com/Armored%20Vehicles',147)#装甲车
# deagel1('D:\All_Script\Python_deagel/Artillery_Systems.csv','https://www.deagel.com/Artillery%20Systems',120)#火炮系统
# deagel1('D:\All_Script\Python_deagel/Auxiliary_Vessels.csv','https://www.deagel.com/Auxiliary%20Vessels',66)#辅助舰艇
# deagel1('D:\All_Script\Python_deagel/Space_Systems.csv','https://www.deagel.com/Space%20Systems',33)#空间系统
deagel1('D:\All_Script\Python_deagel/Cannons_Gear.csv','https://www.deagel.com/Cannons%20&%20Gear',159)#大炮和装备
# deagel1('D:\All_Script\Python_deagel/Propulsion_Systems.csv','https://www.deagel.com/Propulsion%20Systems',148)#推进系统

#deagel1('D:\All_Script\Python_deagel/missile.csv','https://www.deagel.com/Offensive%20Weapons',80)#导弹



end = time.time ()
print ( '运行时间：', (end - begin) / 60 )  # 50分钟






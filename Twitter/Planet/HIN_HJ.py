# -*- codeing = utf-8 -*-
# @Time : 2020/12/29 15:39
# @Author : lzf
# @File : test_shubiao.py
# @Software :PyCharm
#此程序在大屏幕运行！！！
import time
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
key = 'HIN'
file_path = 'D:\All_Script\Python_planet_picture\\HIN2.28/' + key + '.csv'
f = open ( file_path, 'a', encoding='utf-8', newline='' )
writer = csv.writer ( f )
writer.writerow ( ['num', 'key', 'picture','picture1', 'data'] )

driver = webdriver.Chrome ()#打开谷歌浏览器
driver.get ( url='https://www.planet.com/login/' )
driver.maximize_window ()
time.sleep ( 2 ) #程序睡眠，使网页完全响应后再做操作
name = '3543359760@qq.com' #12.22创建，14天，1月3号爬取
password = '19980816lzf'
driver.find_element_by_name ( 'email' ).send_keys ( name )
driver.find_element_by_name ( 'password' ).send_keys ( password )
driver.find_element_by_xpath ( '//span[@class="MuiButton-label"]' ).click () #登录
time.sleep ( 15 )
driver.find_element_by_xpath ( '//button[@class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-disableElevation"] ').click ()#skip按钮
time.sleep ( 5 )
driver.find_element_by_xpath ( '//div[@title="Search and browse Planet’s imagery catalogue"]/button' ).click () #点击搜索框
time.sleep ( 5 )
driver.find_element_by_xpath ('//div[@class="MuiInputBase-root jss370 MuiInputBase-fullWidth"]' ).click ()  # 搜索框
time.sleep ( 2 )
driver.find_element_by_xpath ( '//input[@class="MuiInputBase-input"]' ).send_keys ( ''' 35° 5' 18.60" N,128° 4' 12.03" E ''' )
time.sleep ( 5 )
# 测试
html = driver.page_source
soup = BeautifulSoup ( html, 'html.parser' )  # 解析网页内容
s = soup.find ( 'div', {'class': 'jss371'} )
print ( s )
driver.find_element_by_xpath ( '//div[@class="MuiListItemText-root jss373 MuiListItemText-dense"]' ).click ()#搜索点击第一个按钮
time.sleep ( 5 )
driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall"]' ).click ()#使图片正序排列
time.sleep ( 1 )

all_date = driver.find_elements_by_id ( 'timeline-period' )
#all_time = driver.find_elements_by_xpath ('//span[@class="MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock"]/div/div[2]/p' )
i = 1
driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiFab-root MuiSpeedDialAction-fab jss334 jss342 MuiFab-sizeSmall"]' ).click ()  # 点击放大按钮
#driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiFab-root MuiSpeedDialAction-fab jss334 jss342 MuiFab-sizeSmall"]' ).click ()  # 点击放大按钮
time.sleep(1)
for date in all_date:
    try:

        date.find_element_by_xpath ('./div[@class="MuiAvatar-root MuiAvatar-circle jss1157 MuiAvatar-colorDefault"]' ).click ()#图片下的日期按钮
        time.sleep ( 10 )
        print ( "11111" )#测试代码
        data = driver.find_element_by_xpath ('//div[@class="MuiButtonBase-root MuiListItem-root jss1679 MuiListItem-gutters MuiListItem-divider MuiListItem-button MuiListItem-secondaryAction Mui-selected jss1680"]/div[2]/div[1]/h6' )
        # 显示图片时间
        driver.execute_script ( 'arguments[0].scrollIntoView ();', data )  #鼠标滑轮到显示该元素

        print ( "22222" )
        text = data.get_attribute ( 'textContent' )
        text1 = text.replace ( ' ', '_' )
        text1 = text1.replace ( ',', '_' )#处理textContent的文本格式
        print ( text1 )
        time.sleep(2)
        pyautogui.screenshot( 'D:\All_Script\Python_planet_picture\\HIN2.28/' + key + '_' + text1 + '.png' ,region=(1080, 197, 646, 646))#顶点位置，图片尺寸
        #driver.get_screenshot_as_file ( 'D:\All_Script\Python_planet_picture\\test/' + key + '_' + text1 + '.png' )#截图并以日期命名
        print ( '已截图111' )
        #driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiFab-root MuiSpeedDialAction-fab jss334 jss342 MuiFab-sizeSmall"]' ).click ()#点击放大按钮
        time.sleep(1)
        x=1523
        y=518
        pyautogui.click(x, y, duration=1)
        pyautogui.scroll ( 1000, x, y, _pause=1 )
        time.sleep(1)
        pyautogui.scroll (  440, x, y, _pause=1 )
        time.sleep ( 7 )
        #pyautogui.screenshot( 'D:\All_Script\Python_planet_picture\\UTP/' + key + '_' + text1 +'_T'+ '.png' ,region=(720, 325, 1021, 690))
        pyautogui.screenshot( 'D:\All_Script\Python_planet_picture\\HIN2.28/' + key + '_' + text1 +'_T'+ '.png' ,region=(609, 197, 1093, 835))
        #driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiFab-root MuiSpeedDialAction-fab jss334 jss342 MuiFab-sizeSmall"]' ).click ()#点击放大按钮
        print ( '已截图222' )
        pyautogui.scroll ( -440, x, y, _pause=1 )
        time.sleep(1)
        pyautogui.scroll ( -1000, x, y, _pause=1 )

        time.sleep(1)
        #driver.find_element_by_xpath ('//button[@class="MuiButtonBase-root MuiFab-root MuiSpeedDialAction-fab jss334 jss343 MuiFab-sizeSmall"]' ).click ()#点击缩小按钮
        #time.sleep ( 3 )
        #缩小地图
        writer.writerow ( [i, key, key + '_' + text1 + '.png', key + '_' + text1 +'_T'+ '.png',text] )
        i = i + 1
        driver.execute_script ( 'arguments[0].scrollIntoView ();', data )  # 鼠标滑轮到显示该元素
    except:
        print ( '今天没有图像！' ) #用try跳过图片为空的日期



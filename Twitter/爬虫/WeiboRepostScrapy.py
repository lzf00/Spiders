import requests
import csv
import xlrd
from lxml import etree
from bs4 import BeautifulSoup
import pandas as pd
import random
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from queue import Queue
import numpy as np
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def login(user,pwd,driver):
    # driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://weibo.com/')
    driver.find_element_by_id('loginname').clear()
    driver.find_element_by_id('loginname').send_keys(user)
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_css_selector('.W_btn_a.btn_32px').click()
    cookies = driver.get_cookies()

    with open("cookie.data", "w") as f:
        for cookie in driver.get_cookies():
            # print(cookie)
            f.write(
                str(cookie) + "\n"
            )
    with open("cookie.data", "r") as f:
        lis_lines = f.readlines()

    driver.get('https://weibo.com/')
    driver.delete_all_cookies()
    for line in lis_lines:
        dic_line = eval(line.strip())
        driver.add_cookie(dic_line)
    driver.refresh()


def base62_encode(num, alphabet=ALPHABET):
    """Encode a number in Base X

    `num`: The number to encode
    `alphabet`: The alphabet to use for encoding
    """
    if (num == 0):
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)
def base62_decode(string, alphabet=ALPHABET):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num
def url_to_mid(url):
    url = str(url)[::-1]
    size2 = len(url) / 4 if len(url) % 4 == 0 else len(url) / 4 + 1
    size = int(size2)
    result = []
    for i in range(size):
        s = url[i * 4: (i + 1) * 4][::-1]
        s = str(base62_decode(str(s)))
        s_len = len(s)
        if i < size - 1 and s_len < 7:
            s = (7 - s_len) * '0' + s
        result.append(s)
    result.reverse()
    return int(''.join(result))
def mid_to_url(midint):
    midint = str(midint)[::-1]
    size1 = len(midint) / 7 if len(midint) % 7 == 0 else len(midint) / 7 + 1
    size = int(size1)
    result = []
    for i in range(size):
        s = midint[i * 7: (i + 1) * 7][::-1]
        s = base62_encode(int(s))
        s_len = len(s)
        if i < size - 1 and len(s) < 4:
            s = '0' * (4 - s_len) + s
        result.append(s)
    result.reverse()
    return ''.join(result)

def get_user_info(url,driver):
    driver.get(url)
    user_name = driver.find_element_by_xpath('//h1[@class="username"]').text
    print('55555555')
    print(user_name)
    user_category = driver.find_element_by_xpath('//div[@class="pf_intro"]').text
    print(user_category)
    user_inf = driver.find_elements_by_xpath('//a[@class = "t_link S_txt1"]')
    for it in user_inf:
        u = it.find_element_by_xpath('.//strong').text
        print('999999')
        print(u)

def get_repost(wr,url,driver,q,user_q,mark):

    try:
        data = [weibo_info()] * 2000
        origen_id = url.split('/')[3]
        parent_t = url.split('/')[4]
        parent_m = parent_t.split('?')[0]
        print('parent',parent_m)
        parent_id_ = url_to_mid(parent_m)
        print('parent_id:', parent_id_)
        page = 1
        flag = True
        driver.get(url)
        user_name = driver.find_element_by_xpath('//a[@class="W_f14 W_fb S_txt1"]').text
        weibo_text1= driver.find_element_by_xpath('//div[@class="WB_text W_f14"]')
        weibo_text = weibo_text1.get_attribute('textContent')
        time_info = driver.find_element_by_xpath('//div[@class="WB_from S_txt2"]')
        time_o = time_info.get_attribute('textContent')
        o_pub_time = time_o.split('来')[0]
        print('time_0:',o_pub_time)
        if mark == True:
            write_info(wr,parent_id_,origen_id,'NULL',weibo_text,o_pub_time)

        #print(user_name)
        while flag:
            all_repost = driver.find_elements_by_xpath('//div[@class="list_li S_line1 clearfix"]')
            for item in all_repost:
                #print()
                #print('11111111')
                text = item.find_elements_by_xpath('.//div[@class = "WB_text"]/span')
                for it in text:
                    #print(it.text)
                    test_text = it.text
                    if test_text.find("//@") != -1:
                        print('7890')
                        first_r_name1 = test_text.split('@')[1]
                        #print(first_r_name)
                        first_r_name = first_r_name1.split(':')[0]
                        # if first_r_name == user_name:
                        #     mid = item.get_attribute('mid')
                        #     u_href = item.find_element_by_xpath('.//div[@class = "WB_face W_fl"]/a')
                        #     user_href = u_href.get_attribute('href')
                        #     repost_num = item.find_elements_by_xpath('.//span[@class="line S_line1"]/a')
                        #     for r_item in repost_num:
                        #         # print('666666666')
                        #         # print(r_item.text)
                        #         if r_item.text.find("转发") != -1:
                        #             if len(r_item.text) > 2:
                        #                 weibo_url = user_href + '/' + mid_to_url(mid) + '?type=repost'
                        #                 # print('77777777')
                        #                 # print(weibo_url)
                        #                 q.put(weibo_url)
                        #                 break
                        print('ff:',first_r_name)
                    else:
                        first_r_name = user_name
                        print('gg:',first_r_name)
                    #print('002330')

                    data[i].text = it.text
                    #print('i:',i,',',data[i].text)
                    if it.text.find("//@") != -1 and first_r_name != user_name :
                        continue
                    else:
                        print('2222222')
                        mid = item.get_attribute('mid')
                        #data[i].mid = mid
                        #data[i].id = mid
                        #print('i:',i,',',data[i].mid)
                        #print(item.get_attribute('mid'))
                        #print(item.text)
                        u_href = item.find_element_by_xpath('.//div[@class = "WB_face W_fl"]/a')
                        user_href = u_href.get_attribute('href')
                        pp_time_info = item.find_element_by_xpath('.//div[@class="WB_from S_txt2"]/a')
                        pub_time = pp_time_info.text
                        #print(user_href)
                        user_id = user_href.split('/')[3]
                        #data[i].uid = user_id
                        #print('i:',i,',',data[i].uid)
                        #print(user_href)
                        user_q.put(user_href)
                        parent_id = parent_id_
                        #data[i].parent = parent_id
                        #print('i:',i,',',data[i].parent)
                        repost_num = item.find_elements_by_xpath('.//span[@class="line S_line1"]/a')
                        #print('23234354545:',parent_id)
                        #info_str(mid,user_id,parent_id)
                        write_info(wr,mid,user_id,parent_id,it.text,pub_time)
                        numplus()
                        #print('iiiiiii:',i)
                        for r_item in repost_num:
                            #print('666666666')
                            #print(r_item.text)
                            if r_item.text.find("转发") != -1:
                                if len(r_item.text)>2:
                                    weibo_url  = user_href+'/'+mid_to_url(mid) + '?type=repost'
                                    #print('77777777')
                                    #print(weibo_url)
                                    q.put(weibo_url)
                                    break
                        # get_user_info(user_href, driver)


            a = driver.find_element_by_xpath('//a[@class = "page next S_txt1 S_line1"]')
            ActionChains(driver).move_to_element(a).click().perform()
            page = page + 1
            if page%10==0:
                print('url:::')
                url = driver.current_url
                print(driver.current_url)
            T = random.randint(3,7)
            time.sleep(T)

    except:
        print('page:',page)
        pass

class weibo_info:
    def __init__(self):
        self.id = '',
        self.mid = '',
        self.parent = '',
        self.text = '',
        self.uid = '',
        self.followers = '',
        self.friends = '',
        self.article = '',
        self.name = '',
        self.sex = '',
        self.category='',
        self.time=''
class h:
    data = [weibo_info()] * 2000
def info_str(mid,uid,parent,text,time):
    global data
    data[i].id = mid
    data[i].mid = mid
    data[i].uid = uid
    data[i].parent = parent
    data[i].text = text
    data[i].time = time
def write_info(wr,mid,uid,parent,text,time):
    global data
    wr.writerow([mid, mid,uid,parent,text,time])


class g:
    i = 0
def numplus():
    global i
    i = i +1


if __name__ =="__main__":

    layer_q = Queue()
    user_q = Queue()
    user = '1738378084@qq.com'
    pwd = 'qdw128723'
    url = 'https://weibo.com/7065543812/JiD9LEl5X?type=repost'
    driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://weibo.com/')
    driver.find_element_by_id('loginname').clear()
    driver.find_element_by_id('loginname').send_keys(user)
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_css_selector('.W_btn_a.btn_32px').click()
    cookies = driver.get_cookies()

    with open("cookie.data", "w") as f:
        for cookie in driver.get_cookies():
            # print(cookie)
            f.write(
                str(cookie) + "\n"
            )
    with open("cookie.data", "r") as f:
        lis_lines = f.readlines()

    driver.get('https://weibo.com/')
    driver.delete_all_cookies()
    for line in lis_lines:
        dic_line = eval(line.strip())
        driver.add_cookie(dic_line)
    driver.refresh()

    data = xlrd.open_workbook('weibo_url1.xlsx')
    table = data.sheets()[0]
    i = 0
    article_num = 0
    for Node in range(1,table.nrows):
        url = table.cell_value(Node,0)+'?type=repost'
        file_path = 'D:\python_data\southsea/all/weibo_No'+str(article_num)+'.csv'
        f = open(file_path,'w',encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(["id","mid","uid","parent","text","time"])
        mark = True
        get_repost(writer,url,driver,layer_q,user_q,mark)
        mark = False
        print("layer_q_size::",layer_q.qsize())
        while not layer_q.empty():
            url = layer_q.get()
            print('llll:',url)
            get_repost(writer,url,driver,layer_q,user_q,mark)
            print("layer_q_size::", layer_q.qsize())
        print('i:',user_q.qsize())
        print('over!')
        l = user_q.qsize()
        i = i + 1
        article_num =  article_num + 1
    driver.close()

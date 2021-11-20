import csv
from selenium import webdriver
import time
from bs4 import BeautifulSoup
def get_contract_url(driver,key_word,urls):
    # try:
        num = 40
        while num<73: ###修改可以改变爬取的页数73
            driver.get('https://www.defense.gov/News/Contracts/?Page='+str(num))
            #driver.get('https://www.defense.gov/Newsroom/Contracts/')
            time.sleep(1)
            #href= driver.find_elements_by_xpath('//h3[@class="title"]/a')
            html = driver.page_source
            soup = BeautifulSoup ( html, 'html.parser', from_encoding='utf-8' )  # 解析网页
            div = soup.find ( 'div', {'class', 'feature-template-container'} )
            #print(div)
            href = div.find_all ( 'a')
            #print(href)
            for item in href:
                url = item.get('href')
                print("url:",url)
                urls.append(url)
            num = num + 1
            print(num)
    # except:
    #     print("已完成！")

def get_contract_content(driver,writer,url):
      try:
        driver.get(url)
        time.sleep(1)
        contracr_time = driver.find_element_by_xpath('//h1[@class="maintitle"]').text
        # contracr_time.replace(',',' ')
        print("time:",contracr_time)
        p = driver.find_elements_by_xpath('//div[@class="body"]/p')
        ps=[]
        for item in p:
            #print("item:",item.text)
            ps.append(item.text)

        ps1 = '///'.join ( ps ).strip ()  # 用回车符将列表里的每个元素进行分割
        print ( ps1 )
        try:
            writer.writerow([ps1,contracr_time,url])
        except:
            writer.writerow ( ["[]", contracr_time, url] )
      except:
          print("网络错误")

if __name__ =='__main__':
    driver =webdriver.Chrome()
    driver.maximize_window()
    #key_word = 'nuclear'###修改关键字
    key_word = 'contract'###修改关键字
    url = []
    get_contract_url(driver,key_word,url)
    num = 1
    for item in url:
        path = 'D:\All_Script\Python_deagel/hetong/'+key_word +'.csv'###修改文件路径及文件名
        f = open(path,'a+',encoding='utf8',newline='')
        writer = csv.writer(f)
        if num==1:
            writer.writerow(['text','time','url'])
        get_contract_content(driver,writer,item)
        num = num + 1
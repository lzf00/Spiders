import time
import datetime
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedrive\chromedriver.exe')
def connent_url(url):

    file_path = 'D:\python_data\southsea/all/vcdgf555.csv'
    f = open(file_path, 'w', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(["text", "time"])
    driver.get(url=url)
    try:
        page = 0
        for y in range(1000):

            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all(
                'div', {'class': 'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-1mi0q7o'})
            page += 1
            print('Fetching data on page {}！！！'.format(page))
            try:
                for div in divs:
                    retweet  = div.find_all('svg', {'class':'r-1re7ezh r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-meisx5'})
                    print('retweet::',len(retweet))
                    if(len(retweet)==0):
                        text = div.find(
                        'div', {'class': 'css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'}).get_text()
                        print('text::',text)
                        time2 = div.find(
                            'a', {'class': 'r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao'})
                        time1 = div.find('time').get_text()
                        print('time::',time1)
                        writer.writerow([text,time1])
                    else:
                        continue
            except:
                print('该页面以搜索！！')
            time.sleep(3)
            js = 'window.scrollBy(0,6000)'
            driver.execute_script(js)
    except:
        print('当前数据获取完毕。')
        driver.close()


def Run(key_word):
    connent_url(url='https://twitter.com/search?q='+key_word+'&src=typed_query')


if __name__ == '__main__':
    key_word = 'airpots'
    Run(key_word)
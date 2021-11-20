import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedriver.exe')

def connent_url(url):

        file_path = 'D:\All_Script/navywatcher451.csv'
        f = open(file_path, 'w', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(["text", "time"])
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url=url)
        y = 1

        page = 0
        for y in range(1,1000):
            time.sleep(3)
            html = driver.page_source  #将网页资源给html
            soup = BeautifulSoup(html, 'html.parser')  #解析html
            divs = soup.find_all(
                'div', {'class': 'css-1dbjc4n r-j7yic r-qklmqi r-1adg3ll r-1ny4l3l'})
            page += 1
            print('Fetching data on page {}！！！'.format(page))
            print('datalen::',len(divs))
            try:
                for div in divs:
                    retweet  = div.find_all('svg', {'class':'r-m0bqgq r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-meisx5'})
                    print('retweet::',len(retweet))
                    if(len(retweet)==0):
                        text = div.find(
                        'div', {'class': 'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'}).get_text()
                        print('text::',text)
                        # time2 = div.find(
                        #     'a', {'class': 'r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao'})
                        time1 = div.find('time').get_text()
                        print('time::',time1)
                        writer.writerow([text,time1])
                        print('122343')
                    else:
                        continue
            except:
                print('1111')
            print('789789789')
            js = "window.scrollBy(0,5000)"
            driver.execute_script('window.scrollBy(0,6000)')  #滑动右边进度条
            print('12345')
            time.sleep(2)
            y = y + 1

        print('当前数据获取完毕。')
        driver.close()
def Run():
    connent_url(url='https://twitter.com/navywatcher451')
if __name__ == '__main__':
    Run()
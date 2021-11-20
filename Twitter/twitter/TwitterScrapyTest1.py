import time
import datetime
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome( )

def connent_url(url):

    #file_path = 'D:\All_Script\Twitter/AirAssets.csv'
    # file_path = 'D:\All_Script\Twitter/AirAssets.csv'
    #file_path = 'D:\All_Script\Twitter/WarshipCam.csv'
    #file_path = 'D:\All_Script\Twitter/AircraftSpots.csv'
    #file_path = 'D:\All_Script\Twitter/WarshipCam_US.csv'
    #file_path = 'D:\All_Script\Twitter/WarshipCam.csv'
    file_path = 'D:\All_Script\Twitter/Nick.csv'

    f = open(file_path, 'a+', encoding='utf-8',newline='')
    writer = csv.writer(f)
    writer.writerow(["text", "time"])
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url=url)
    y = 1
    try:
        page = 0
        for y in range(1,3):
            time.sleep(3)
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            divs = soup.find_all( 'div', {'class': 'css-1dbjc4n r-j7yic r-qklmqi r-1adg3ll r-1ny4l3l'})
            page += 1
            print('Fetching data on page {}！！！'.format(page))
            print('datalen::',len(divs))
            try:
                for divw in divs:
                    retweet  = divw.find_all('svg', {'class':'r-m0bqgq r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-bnwqim r-1plcrui r-lrvibr r-meisx5'})
                    print('retweet::',len(retweet))
                    if(len(retweet)==0):
                        print('56566565')
                        text = divw.find('div', {'class':'css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0'}).get_text()
                        text = text.replace("\n","")
                        text = text.replace("\r","")
                        print('text::',text)
                        # time2 = div.find(
                        #     'a', {'class': 'r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao'})
                        time1 = divw.find('time').get_text()
                        print('time::',time1)
                        writer.writerow([text,time1])
                        print('122343')
                    else:
                        continue
            except:
                print('1111')
            print('789789789')
            js = "window.scrollBy(0,5000)"
            driver.execute_script('window.scrollBy(0,6000)')
            print('12345')
            time.sleep(2)
            y = y + 1
    except:
        print('当前数据获取完毕。')
        driver.close()
def Run():
    #connent_url(url='https://twitter.com/AirAssets')
    #connent_url(url='https://twitter.com/MIL_Radar')
    #connent_url(url='https://twitter.com/WarshipCam')
    #connent_url(url='https://twitter.com/AircraftSpots')
    connent_url(url='https://twitter.com/search?q=DDG-59(from%3AWarshipCam)%20until%3A2021-03-02%20since%3A2020-01-01&src=typed_query&f=live')




    #connent_url(url='https://twitter.com/search?f=live&q=USS%20Shiloh%20(from%3Alala_zet)%20until%3A2020-12-31%20since%3A2020-01-01%20-filter%3Areplies&src=typed_query')
if __name__ == '__main__':
    Run()
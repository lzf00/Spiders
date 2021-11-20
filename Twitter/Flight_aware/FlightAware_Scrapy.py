import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedriver.exe')
url = []
url.append('https://zh.flightaware.com/live/airport/PGUA/arrivals')
url.append('https://zh.flightaware.com/live/airport/PGUA/departures')

all_href = []
j = 0
for l in range(0,2):
    driver.get(url=url[l])
    driver.maximize_window()

    time.sleep(2)
    # key_word = 'UAM'
    # sel = driver.find_element_by_xpath('//select[@class="trackSelect"]')
    # Select(sel).select_by_value('airportSearch')
    # time.sleep(2)
    # driver.find_element_by_id('airport').send_keys(key_word)
    # time.sleep(1)
    # driver.find_element_by_xpath('//div[@class="trackSubmit"]/button').click()
    # time.sleep(3)
    tables= driver.find_elements_by_xpath('//table[@class="prettyTable fullWidth"]')

    for item in tables:
        trs = item.find_elements_by_tag_name('tr')
        print('len:',len(trs))
        num = 1
        flag = 0
        for it in trs:
            if(flag<2):
                flag = flag+1
                continue
            else:
                href = it.find_element_by_xpath('.//td[@class="smallrow'+str(num)+'"]/span/a').get_attribute('href')
                all_href.append(href)
                print('href:', all_href[j])
                j = j + 1

                if num==1:
                    num = num + 1
                else:
                    num = num - 1

file_path = 'D:\All_Script\Python_Flightaware/FlightAware_UAM_1.csv'
f = open(file_path, 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(["callsign", "date", "departure", "arrival", "duration"])


for i in range(0,j):
    driver.get(url=all_href[i])
    #driver.maximize_window()
    time.sleep(3)

    driver.find_element_by_xpath ( '//div[@id="footerLanguages"]/a[3]' ).click ()

    # hhhhh = driver.find_element_by_xpath ( '//div[@id="LocaleTopBox"]/a[1]' ).get_attribute('href')
    # print('hhhhhhhhh:::',hhhhh)
    #driver.find_element_by_xpath ( '//div[@id="LocaleTopBox"][1]/a[1]' ).click()

    time.sleep ( 3 )
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    # flight_model = soup.find('div',{'class':'flightPageData'}).get_text()
    # print('flightmodel:',flight_model)
    callsign = all_href[i].split("/")[6].split('-')[0]
    print('callsign:', callsign)
    flights = soup.find_all('div',{'class':'flightPageDataRowTall'})
    print('fight_num:',len(flights))
    for item in flights:
        try:
            date = item.find('div',{'class':'flightPageActivityLogData flightPageActivityLogDate'}).get_text()
            print('date:',date.strip())
            flight_info = item.find_all('div',{'class':'flightPageActivityLogDataPart'})
            flag = 0
            print("len:",len(flight_info))
            for it in flight_info:
                if(flag==0):
                    departure = it.get_text()
                    departure_text = departure.strip()
                    departure_text = departure_text.replace("\n", " ")
                    departure_text = departure_text.replace("\r", " ")
                    print('daparture:',departure_text)
                    flag = flag + 1
                else:
                    arrival = it.get_text()
                    arrival_text = arrival.strip()
                    arrival_text = arrival_text.replace("\n", " ")
                    arrival_text = arrival_text.replace("\r", " ")
                    print('arrival:',arrival_text)
            duration = item.find('div',{'class':'flightPageActivityLogData optional text-right'}).get_text()
            print('duration:',duration.strip())
            print("-----------------------------------------")
            writer.writerow([callsign,date.strip(),departure_text,arrival_text,duration.strip()])
        except:
            print('error！！！')
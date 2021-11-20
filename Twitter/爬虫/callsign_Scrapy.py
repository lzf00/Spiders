import time
import xlrd
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
driver = webdriver.Chrome('D:\chromedriver.exe')
file_path = 'D:\All_Script\Callsign_clean/callsignTomodel.csv'
f = open(file_path, 'w', encoding='utf-8')
writer = csv.writer(f)
writer.writerow(["callsign", "flightmodel"])
data = xlrd.open_workbook('D:\All_Script\Callsign_clean/callsign.xlsx')
table = data.sheets()[0]
for Node in range(1, table.nrows):
    url = 'https://www.radarbox.com/data/flights/'+table.cell_value(Node, 0)
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find_all('div',{'id':'aircraft-info'})
    model = ''
    print('0000000')
    for div in divs:
        print('1122323')
        a = div.find_all('a')
        num = 0
        for it in a:
            text = it.text
            model = text
            print('model:',model)
            num = num + 1
            break
    writer.writerow([table.cell_value(Node, 0), model])
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import requests
import datetime
from time import sleep
import os
import sys
from fake_useragent import UserAgent
import json

# for fast work, use only 3 pages (240 items)
product_dict = {}
for f in os.listdir('page_json'):
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.json' and file_name.split('_')[-1] == sys.argv[1] and int(file_name.split('_')[-2]) <= 3:
        with open('page_json/'+file_name + file_ext, 'r') as inf:
            jsondata = json.load(inf)
            
        try:
            for data in jsondata['data']['GetShopProduct']['data']:
                product_dict[data['product_id']] = data['product_url']
        except:
            pass

for key in product_dict:
    try:
        driver = webdriver.Chrome()
        driver.get(product_dict[key])
        sleep(3)
        soup = BeautifulSoup(driver.page_source, "html5lib")
        filename = key+"_"+str(datetime.date.today())+".html"
        print(filename)
        with open('product_html/'+filename, "w", encoding='utf-8') as file:
            file.write(str(soup.prettify()))
        driver.quit()
        sleep(2)
    except:
        pass
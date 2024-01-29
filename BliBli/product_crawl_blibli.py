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

product_dict = {}
for f in os.listdir('page_html'):
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.html' and file_name.split('_')[-1] == sys.argv[1]:
        with open('page_html/'+file_name + file_ext, 'r') as inf:
            webpage = inf.read()
            
        soup = BeautifulSoup(webpage, features="html5lib")
        getdata = soup.find('pre').text
        jsondata = json.loads(getdata)
        for product in jsondata["data"]["products"]:
            product_dict[product["formattedId"]] = product["pickupPointCode"]

for key in product_dict:
    try:
        url = 'https://www.blibli.com/backend/product-detail/products/'+str(key)+'/_summary?pickupPointCode=' + product_dict[key]
        print("Getting " + url)
        driver=webdriver.Chrome()
        driver.get(url)
        sleep(3)
        soup = BeautifulSoup(driver.page_source, features="html5lib")
        with open('product_html/'+str(key)+'_'+str(datetime.date.today())+'.html', 'w') as f:
            f.write(str(soup.prettify()))
        sleep(2)
        driver.quit()
    except:
        print('Error: ' + key)
        pass
        
        
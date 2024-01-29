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

product_dict = {}
for f in os.listdir('page_html'):
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.html' and file_name.split('_')[-1] == sys.argv[1]:
        with open('page_html/'+file_name + file_ext, 'r') as inf:
            webpage = inf.read()
            
        soup = BeautifulSoup(webpage, features="html5lib")
        try:
            for div in soup.find_all("div", {"class": "product-collection list-product clearfix"}):
                for id in div.find_all("div", {"class": "item"}):
                    product_dict[id.get('data-plu')] = id.find('a')['href']
        except:
            print("Container Div is missing")

for key in product_dict:
    try:
        url = 'https://www.klikindomaret.com' + product_dict[key]
        print("Getting " + url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, features="html5lib")
        with open('product_html/'+str(key)+'_'+str(datetime.date.today())+'.html', 'w') as f:
            f.write(str(soup.prettify()))
    except:
        print("Error: " + product_dict[key])
        pass

        
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


outfile = 'data.csv'
for f in os.listdir('product_html'):
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.html' and file_name.split('_')[-1] == sys.argv[1]:
        with open('product_html/'+file_name + file_ext, 'r', encoding='utf-8') as inf:
            webpage = inf.read()
            
        soup = BeautifulSoup(webpage, features="html5lib")
        
        # To make the project simple, only a certain data is scraped
        data_list = []
   
        divName = soup.find('div', {"id": "main-pdp-container"})   
        try:
            name = divName.find('h1', {"data-testid": "lblPDPDetailProductName"}).text.lstrip().rstrip()
        except:
            name = ''
            print(file_name + ' Name not Found')
            
        try:
            price = divName.find('div', {"data-testid": "lblPDPDetailProductPrice"}).text.lstrip().rstrip().replace('Rp', '')
        except:
            price = ''
            print(file_name + ' Price not Found')
            
        try:
            orprice = divName.find('span', {"data-testid": "lblPDPDetailOriginalPrice"}).text.lstrip().rstrip().replace('Rp', '')
        except:
            orprice = price
            print(file_name + ' Original Price not Found Set Original to Price')
            
        try:
            discount = divName.find('span', {"data-testid": "lblPDPDetailDiscountPercentage"}).text.lstrip().rstrip().replace('%', '')
        except:
            discount = 0
            print(file_name + ' Discount not Found set Discount to 0')
            
        try:
            detail = name.split(' ')[-1].replace(',', '.')
        except:
            detail = ''
            
        try:
            catDiv = divName.find('ol', {"data-testid": "lnkPDPDetailBreadcrumb"}) 
            category = catDiv.find_all('li')[-2].text.replace('\n', '').lstrip().rstrip()
        except:
            category = ''
            print(file_name + ' Category not Found')
            
        try:
            sellDiv = divName.find('a', {"data-testid": "llbPDPFooterShopName"})
            seller = sellDiv.find('h2').text.replace('\n', '').lstrip().rstrip()
            
        except:
            seller = ''
            print(file_name + ' Seller not Found')
            
        
        data_list.append(file_name.split('_')[0])
        data_list.append(name)
        data_list.append(price)
        data_list.append(orprice)
        data_list.append(discount)
        data_list.append(detail)
        data_list.append('Tokopedia')
        data_list.append(category)
        data_list.append(file_name.split('_')[-1])
        data_list.append(seller)
        print(data_list)
        
        
        if not os.path.exists(outfile) or os.stat(outfile).st_size == 0:
            with open(outfile, 'w', newline='', encoding='utf-8') as outf:
                data = csv.writer(outf)
                data.writerow(['id', 'name', 'price', 'originalprice', 'discountPercentage', 'detail', 'platform', 'category', 'scrapedate', 'seller'])          
        
        with open(outfile, 'a', newline='', encoding='utf-8') as outf:
            data = csv.writer(outf)
            data.writerow(data_list)
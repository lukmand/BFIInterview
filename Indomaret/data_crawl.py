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


outfile = 'data.csv'
for f in os.listdir('product_html'):
    file_name, file_ext = os.path.splitext(f)
    if file_ext == '.html' and file_name.split('_')[-1] == sys.argv[1]:
        with open('product_html/'+file_name + file_ext, 'r') as inf:
            webpage = inf.read()
            
        soup = BeautifulSoup(webpage, features="html5lib")
        
        # To make the project simple, only a certain data is scraped
        data_list = []
   
        divName = soup.find('div', {"class": "produk produk-detail non-skeleton hidden"})   
        try:
            name = divName.find('div', {"class": "product-title"}).text.lstrip().rstrip()
        except:
            name = ''
            print(file_name + ' Name not Found')
            
        try:
            price = divName.find('span', {"class": "normal price-final"}).text.lstrip().rstrip()
        except:
            price = ''
            print(file_name + ' Price not Found')
            
        try:
            orprice = divName.find('span', {"class": "strikeout disc-price"}).text.lstrip().rstrip().split(' ')[-1]
        except:
            orprice = price
            print(file_name + ' Original Price not Found Set Original to Price')
            
        try:
            discount = divName.find('span', {"class": "discount"}).text.lstrip().rstrip().split('%')[-1]
        except:
            discount = 0
            print(file_name + ' Discount not Found set Discount to 0')
            
        try:
            detail = name.split(' ')[-1].replace(',', '.')
        except:
            detail = ''
            
        try:
            catDiv = soup.find('div', {"class": "wrp-breadcrumb hidden"}) 
            aDiv = catDiv.find('div', {"class": "breadcrumb"}) 
            category = aDiv.find_all('a')[-1]['href'].split('/')[-1]
        except:
            category = ''
            print(file_name + ' Category not Found')
            
        try:
            seller = divName.find('span', {"class": "typesend-title"}).text.lstrip().rstrip()
        except:
            seller = ''
            print(file_name + ' Seller not Found')
            
        
        data_list.append(file_name.split('_')[0])
        data_list.append(name)
        data_list.append(price)
        data_list.append(orprice)
        data_list.append(discount)
        data_list.append(detail)
        data_list.append('Indomaret')
        data_list.append(category)
        data_list.append(file_name.split('_')[-1])
        data_list.append(seller)
        print(data_list)
        
        
        if not os.path.exists(outfile) or os.stat(outfile).st_size == 0:
            with open(outfile, 'w', newline='') as outf:
                data = csv.writer(outf)
                data.writerow(['id', 'name', 'price', 'originalprice', 'discountPercentage', 'detail', 'platform', 'category', 'scrapedate', 'seller'])          
        else:
            with open(outfile, 'a', newline='') as outf:
                data = csv.writer(outf)
                data.writerow(data_list)
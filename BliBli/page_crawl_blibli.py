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
import urllib.request, json

# Rough and simple work
page = 6
start = 0
inc = 40

for p in range(1, page+1): 
    url = "https://www.blibli.com/backend/search/products?sort=0&page="+str(p)+"&start="+str(start)+"&searchTerm=unilever indonesia official&intent=false&merchantSearch=true&multiCategory=true&category=53400&seller=Official Store&customUrl=&channelId=web&showFacet=false&isMobileBCA=false&isJual=false"
    url = url.replace(" ", "%20")

    driver=webdriver.Chrome()
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, "html5lib")
    filename = "output_"+str(p)+"_"+str(datetime.date.today())+".html"
    print(filename)
    with open('page_html/'+filename, "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))
    sleep(10)
    start += inc

        
        
       

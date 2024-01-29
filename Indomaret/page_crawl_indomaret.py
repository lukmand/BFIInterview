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

url = 'https://www.klikindomaret.com/page/unilever-officialstore'

try:       
    driver = webdriver.Chrome()
    driver.get(url)
    delay = 5
    cnt = 1
    while True:
        soup = BeautifulSoup(driver.page_source, "html5lib")
        filename = "output_"+str(cnt)+"_"+str(datetime.date.today())+".html"
        print(filename)
        try:
            with open('page_html/'+filename, "w") as file:
                file.write(str(soup.prettify()))
        except:
            print("Saving Error")
            driver.quit()
        try:
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'next'))).click()   
            cnt += 1
            url = driver.current_url
        except:
            print("Next Page not Found. Stop Scraping.")
            driver.quit()
            break
    driver.quit()
except:
    print("Webdriver error")
    
        
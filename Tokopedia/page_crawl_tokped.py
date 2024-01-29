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
url_target = 'https://gql.tokopedia.com/graphql/ShopProducts'

header = {'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'X-Version': '0a4217d',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
  'content-type': 'application/json',
  'accept': '*/*',
  'Referer': 'https://www.tokopedia.com/unilever/product',
  'X-Source': 'tokopedia-lite',
  'X-Device': 'default_v3',
  'X-Tkpd-Lite-Service': 'zeus',
  'sec-ch-ua-platform': '"Windows"'
}

page = 75
for p in range(1, page+1):
    try:
        query = f'[{{"operationName":"ShopProducts","variables":{{"source":"shop","sid":"1854168","page":{p},"perPage":80,"etalaseId":"etalase","sort":1,"user_districtId":"2274","user_cityId":"176","user_lat":"","user_long":""}},"query":"query ShopProducts($sid: String\u0021, $source: String, $page: Int, $perPage: Int, $keyword: String, $etalaseId: String, $sort: Int, $user_districtId: String, $user_cityId: String, $user_lat: String, $user_long: String) {{\\n  GetShopProduct(shopID: $sid, source: $source, filter: {{page: $page, perPage: $perPage, fkeyword: $keyword, fmenu: $etalaseId, sort: $sort, user_districtId: $user_districtId, user_cityId: $user_cityId, user_lat: $user_lat, user_long: $user_long}}) {{\\n    status\\n    errors\\n    links {{\\n      prev\\n      next\\n      __typename\\n    }}\\n    data {{\\n      name\\n      product_url\\n      product_id\\n      price {{\\n        text_idr\\n        __typename\\n      }}\\n      primary_image {{\\n        original\\n        thumbnail\\n        resize300\\n        __typename\\n      }}\\n      flags {{\\n        isSold\\n        isPreorder\\n        isWholesale\\n        isWishlist\\n        __typename\\n      }}\\n      campaign {{\\n        discounted_percentage\\n        original_price_fmt\\n        start_date\\n        end_date\\n        __typename\\n      }}\\n      label {{\\n        color_hex\\n        content\\n        __typename\\n      }}\\n      label_groups {{\\n        position\\n        title\\n        type\\n        url\\n        __typename\\n      }}\\n      badge {{\\n        title\\n        image_url\\n        __typename\\n      }}\\n      stats {{\\n        reviewCount\\n        rating\\n        averageRating\\n        __typename\\n      }}\\n      category {{\\n        id\\n        __typename\\n      }}\\n      __typename\\n    }}\\n    __typename\\n  }}\\n}}\\n"}}]'

        response = requests.post(url_target, headers=header, data=query)
        products = response.json()[0]
        
        filename = "output_"+str(p)+"_"+str(datetime.date.today())+".json"
        print(filename)
        with open('page_json/'+filename, "w", encoding="utf-8") as file:
            json.dump(products, file)
        sleep(3)
    except:
        pass

        
       

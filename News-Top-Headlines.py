# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:52:17 2019

@author: joshua.demko
"""

import requests
import json
import http.client
from datetime import datetime

dStr = datetime.today().strftime("%Y-%m-%d-%H-%M")

url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
# print(response.json())

with open('/data/deepobp/data/news/newsapi_top_headlines-'+dStr+'.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

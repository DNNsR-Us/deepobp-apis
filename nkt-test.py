# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:04:34 2019

@author: joshua.demko
"""

import requests
import json
import http.client
from datetime import datetime, timedelta

#----------------------------------------------------------------------------------------------------------

#t = t-2
d = datetime.today() - timedelta(days=2)
# print(d)
dStr = d.strftime("%Y-%m-%d")
# print(dStr)

url = ('https://newsapi.org/v2/everything?'
       'q=technology&'
       'sources=cnn,rueters,engadget,fox-news,the-verge,polygon,Androidpolice.com,9to5mac.com,ign,techcrunch,Dailymail.co.uk,the-next-web,9to5google.com,Seekingalpha.com,&'
       'from='+dStr+'&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
# print(response.json())

with open('/data/deepobp/data/news/newsapi_technology-'+dStr+'.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

#----------------------------------------------------------------------------------------------------------

#t = t-2

url = ('https://api.weather.gov/alerts?'
       'start=2020-01-27T00:00:00-00:00&'
       'limit=500&'
       'cursor=cursor')
response = requests.get(url, verify=False)
print(response.json())

with open('/data/deepobp/code/NWS-alerts.json', 'a+', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

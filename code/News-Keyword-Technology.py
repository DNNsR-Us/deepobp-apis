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
t = datetime.today() - timedelta(days=2)
tStr = t.strftime("%Y-%m-%dT00:00:00-00:00")

url = ('https://newsapi.org/v2/everything?'
       'q=technology&'
       'sources=cnn,rueters,engadget,fox-news,the-verge,polygon,Androidpolice.com,9to5mac.com,ign,techcrunch,Dailymail.co.uk,the-next-web,9to5google.com,Seekingalpha.com,&'
       'from='+tStr+'&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
print(response.json())

with open('/data/deepobp/data/news/newsapi_technology.json', 'a+', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)
    
#----------------------------------------------------------------------------------------------------------
    
#t = t-2

url = ('https://api.weather.gov/alerts?'
       'start='+tStr+'&'
       'limit=500&'
       'cursor=cursor')
response = requests.get(url, verify=False)
print(response.json())

with open('/data/deepobp/data/news/NWS-alerts.json', 'a+', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

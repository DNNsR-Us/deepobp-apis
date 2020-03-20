# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:04:34 2019

@author: joshua.demko
Adapted for covid19 by diana.kriese
"""

import requests
import json
import http.client
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

t = datetime.today()
tStr = t.strftime("%Y-%m-%dT00:00:00-00:00")
# print('tStr is '+tStr)
dStr = t.strftime("%Y-%m-%d")

url = ('https://newsapi.org/v2/everything?'
#       'q=covid19&'
       'q=covid-19&'
       'sources=cnn,rueters,engadget,fox-news,the-verge,polygon,Androidpolice.com,9to5mac.com,ign,techcrunch,Dailymail.co.uk,the-next-web,9to5google.com,Seekingalpha.com,&'
       'from='+tStr+'&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
# print(response.json())

with open('/data/deepobp/data/news/newsapi_covid19-'+dStr+'.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

#----------------------------------------------------------------------------------------------------------
url = ('https://newsapi.org/v2/everything?'
       'q=novel+coronavirus&'
       'sources=cnn,rueters,engadget,fox-news,the-verge,polygon,Androidpolice.com,9to5mac.com,ign,techcrunch,Dailymail.co.uk,the-next-web,9to\
5google.com,Seekingalpha.com,&'
       'from='+tStr+'&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
# print(response.json())

with open('/data/deepobp/data/news/newsapi_novelcv-'+dStr+'.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

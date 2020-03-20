# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 09:04:34 2019

@author: joshua.demko
"""

import requests
import json
import http.client
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

superbowlDate = '2020-02-02'
#t = datetime.fromisoformat(superbowlDate).timestamp() - timedelta(months=1)
# t = datetime(2020, 2, 2) - relativedelta(months=1)
t = datetime(2020, 2, 6)
tStr = t.strftime("%Y-%m-%dT00:00:00-00:00")
print('tStr is '+tStr)

url = ('https://newsapi.org/v2/everything?'
#       'q=superbowl&'
       'q=nfl&'
       'sources=cnn,rueters,engadget,fox-news,the-verge,polygon,Androidpolice.com,9to5mac.com,ign,techcrunch,Dailymail.co.uk,the-next-web,9to5google.com,Seekingalpha.com,&'
       'from='+tStr+'&'
       'pageSize=100&'
       'apiKey=15c5e5b04d4d4404a674174a3b21b365')

response = requests.get(url, verify=False)
print(response.json())

with open('/data/deepobp/data/news/newsapi_nfl.json', 'a+', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:40:40 2019

@author: joshua.demko
"""

import requests
import json
import time
from datetime import date, timedelta
import urllib3

# Suppress Python warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

start = date(1970,1,1)
end = date(1974,12,31)
deltat = (end - start)
dt = timedelta(7)

for i in range(int(deltat.days/7.)):
    
    url = ('https://api.nasa.gov/neo/rest/v1/feed?'
       'start_date='+(start+(i*dt)).isoformat()+'&'
       'end_date='+(start+((i+1.)*dt)).isoformat()+'&'
       'api_key=Ic7fvU2hG8V1DDqe0xhzhBaiH0ZScwjcWmaGe3xY')

    response = requests.get(url, verify=False)
    # print(response.json())

    with open('/data/deepobp/data/NASA/NASA-NEO-19700101.json', 'a+', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

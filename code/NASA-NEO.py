# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:40:40 2019

@author: joshua.demko
"""

import requests
import json
import time
from datetime import datetime, timedelta
import urllib3

# Suppress Python warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

end = datetime.today()
start = end - timedelta(days=7)

start_date = start.isoformat()
end_date = end.isoformat()

dStr = end.strftime("%Y-%m-%d")

url = ('https://api.nasa.gov/neo/rest/v1/feed?'
       'start_date='+start_date+'&'
       'end_date='+end_date+'&'
       'api_key=Ic7fvU2hG8V1DDqe0xhzhBaiH0ZScwjcWmaGe3xY')

response = requests.get(url, verify=False)
# print(response.json())

with open('/data/deepobp/data/NASA/NASA-NEO-'+dStr+'.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)

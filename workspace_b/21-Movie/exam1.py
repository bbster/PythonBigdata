import requests
import json
import datetime as dt
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot

api_key = '23fceb42d2f960f80bbdf3b93ac4b1f1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

session = requests.Session()
session.headers.update({'user_agent' : user_agent, 'referer': None})

url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={date}'

today = dt.datetime.now()
delta = dt.timedelta(days = -1)
yesterday = today + delta
yesterday_str = yesterday.strftime('%Y%m%d')
print(yesterday_str)
print('-'*30)

api_url = url.format(key=api_key, date=yesterday_str)

r = session.get(api_url)

if r.status_code != 200:
    print(['Error'])
    quit()
    
print(r.text)
print('-'*30)

daily_boxoffice_dict = json.loads(r.text)
df = DataFrame(daily_boxoffice_dict['boxOfficeResult'], ['dailyBoxOfficeList'])
print(df)

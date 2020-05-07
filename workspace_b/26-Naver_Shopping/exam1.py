import requests
import urllib
from bs4 import BeautifulSoup as bs
from pandas import DataFrame

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent': user_agent, 'referer':None})

keyword = '카메라'
max_page = 5
base_url = 'https://search.shopping.naver.com/search/all.nhn'
base_param = {'origQuery':keyword, 'pagingIndex':1, 'pagingSize':40,
              'viewType':'list', 'sort':'rel', 'frm':'NVSHPAG', 
              'query':keyword}

data_list = []

for page in range(1, max_page+1) :
    base_param['pagingIndex'] = page
    query = urllib.parse.urlencode(base_param)
    content_url = base_url + '?' + query
    #print(content_url)
    
    r = session.get(content_url)
    if r.status_code != 200 :
        print('[ERROR]')
        continue
    
    soup = bs(r.text, 'html.parser')
    info_list = soup.select('.info')
    #print(info_list)
    
    for info in info_list:
        item_dict = {}
        title_list = info.select('.tit')
        item_dict['상품명'] = title_list[0].text.strip()

        price_list = info.select('.num')        
        price = price_list[0].text.strip()
        price = price.replace(',', '')
        item_dict['가격'] = int(price)
        
        spec_list = info.select('.detail > a')
        for v in spec_list:
            v = v.text.strip()
            tmp = v.split(":")
            
            if len(tmp) == 2 :
                key = tmp[0].strip()
                value = tmp[1].strip()
                item_dict[key] = value
        
        data_list.append(item_dict)
        
#print(data_list)

df = DataFrame(data_list)
print(df)

df.to_excel(keyword + ".xlsx")










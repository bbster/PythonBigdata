import requests
import os
import datetime as dt
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

content_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=020&aid=0003283943'

r = session.get(content_url)

datetime = dt.datetime.now().strftime("%y%m%d_%H%m%s")
dirname = "뉴스기사_%s" %datetime
content_merge = ""

if r.status_code != 200 :
    print('[ERROR]')
    quit()
    
#print(r.text)
    
soup = bs(r.text, 'html.parser')  



article_item = soup.select('#articleBodyContents')[0]
for target in article_item.find_all('script') : target.extract()
for target in article_item.find_all('a') : target.extract()
for target in article_item.find_all('span') : target.extract()
for target in article_item.find_all('div') : target.extract()
for target in article_item.find_all('br') : target.replace_with('\n')
article_str = article_item.text.strip()


    
    
    
    
    
    
    
    
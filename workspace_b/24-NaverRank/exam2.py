import requests
from bs4 import BeautifulSoup as bs
from pandas import DataFrame

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

session = requests.Session()
session.headers.update({'user_agent' : user_agent, 'referer': None})

content_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=014&aid=0004417717'

r = session.get(content_url)

if r.status_code != 200:
    print('Error')
    quit()

soup = bs(r.text, 'html.parser')
#news = soup.find_all('div', class_='_article_body_contents')

main_content = soup.select('#articleBodyContents')[0]
for target in main_content.find_all('script') : target.extract()
for target in main_content.find_all('a') : target.extract()
for target in main_content.find_all('span') : target.extract()
for target in main_content.find_all('div') : target.extract()
for target in main_content.find_all('br') : target.replace_with('\n')
article = main_content.text.strip()
print(article)

with open('네이버 뉴스.txt', 'w', encoding='utf-8') as f:
    f.write(article)
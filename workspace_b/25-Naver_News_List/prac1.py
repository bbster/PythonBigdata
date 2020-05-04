import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

content_url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=101&oid=020&aid=0003283943'

r = session.get(content_url)

if r.status_code != 200 :
    print('[ERROR]')
    quit()
    
#print(r.text)
    
soup = bs(r.text, 'html.parser')  

main_content = soup.select('#articleBodyContents')[0]
for target in main_content.find_all('script') : target.extract()
for target in main_content.find_all('a') : target.extract()
for target in main_content.find_all('span') : target.extract()
for target in main_content.find_all('div') : target.extract()
for target in main_content.find_all('br') : target.replace_with('\n')
article = main_content.text.strip()
print(article)
    
with open('네이버뉴스.txt', 'w', encoding='utf-8') as f:
    f.write(article)
    
    
    
    
    
    
    
    
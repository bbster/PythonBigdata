import requests
import os
import datetime as dt
from bs4 import BeautifulSoup as bs
from selenium import webdriver

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
session = requests.Session()
session.headers.update({'User-agent':user_agent, 'referer':None})

driver = webdriver.Chrome('/bigdata1_leejichan/python/workspace_b/chromedriver')
driver.implicitly_wait(3)
driver.get('https://shopping.naver.com/')
driver.find_element_bay_name('query').send_keys('카메라')


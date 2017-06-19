# naver_realtime_search_keyword.py
"""
네이버 실시간 검색어 crawling
"""
import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')
tag_list = soup.select('.PM_CL_realtimeKeyword_rolling_base .ah_k')

for idx, tag in enumerate(tag_list, 1):
    print(idx, tag.text)

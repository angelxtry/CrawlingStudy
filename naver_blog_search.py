
from collections import OrderedDict
from itertools import count
import requests
from bs4 import BeautifulSoup


url = 'https://search.naver.com/search.naver'
params = {
    'where': 'post',
    'query': 'AskDjango',
    'start': 1,
}

response = requests.get(url, params=params)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
tag_list = soup.select('.sh_blog_title')

print(response.request.url)
print(html)
# print(html.encode('cp949', 'ignore'))

for tag in tag_list:
    print(tag)
    print(tag['href'], tag.text)

from bs4 import BeautifulSoup
import requests
response = requests.get("http://news.naver.com/main/home.nhn")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('a[href*=sectionList.nhn]'):
    print(tag.text.strip())

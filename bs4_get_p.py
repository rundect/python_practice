
import requests
from bs4 import BeautifulSoup
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')

html = list(soup.children)[2]
print(html)

body = list(html.children)[3]
print(list(body.children))

p = list(body.children)[1]
print(p.get_text())

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('p')[0].get_text())
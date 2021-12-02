import requests as req
from bs4 import BeautifulSoup

res = req.get('https://stepik.org/media/attachments/lesson/209723/3.html')

soup = BeautifulSoup(res.text, 'html.parser')

print(sum(int(td.text) for td in soup.find_all('td')))
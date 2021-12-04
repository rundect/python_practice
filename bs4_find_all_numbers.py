
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html').read().decode('utf-8')
s = str(html)

total = 0
soup = BeautifulSoup(html, 'html.parser')
for a in soup.find_all('td'):
    total += int((a.get_text()))
print(total)

from urllib.request import urlopen

html = urlopen('https://ru.wikipedia.org/wiki/Python').read().decode('utf-8')
s = str(html)
list_of_refs = []
pos = s.find('<a href=')
while pos != -1:
    posquote = s.find('"', pos + 9)
    href = s[pos + 9:posquote]
    print(href)
    list_of_refs.append(href)
    pos = s.find('<a href=', pos + 1)
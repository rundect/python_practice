import requests, collections, re
res = requests.get(' https://stepik.org/media/attachments/lesson/209719/2.html').text
print(*collections.Counter(re.findall(r'<code>(.*?)</code>', res)).most_common())

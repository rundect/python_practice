import requests
res = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html').text
print('Python' if res.count('Python') > res.count('C++') else 'C++')

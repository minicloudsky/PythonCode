import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get('https://www.douban.com/misc/captcha?id=IGeyA35cpFGVaA7TTbQH0w2A:en&size=s',headers = header,timeout=50)
with open('f.jpg','wb') as f:
    f.write(r.content)
    f.close()
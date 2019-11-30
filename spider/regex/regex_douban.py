import requests
import re
r = requests.get('https://book.douban.com/')
pattern = re.compile('class="author">(.*?)</span>.*?class="year">(.*?)</span>.*?class="publisher">(.*?)</span>.*?class="abstract">(.*?)</p>',re.S)
results = re.findall(pattern,r.text)
for result in results:
    for i in result:
        print(i.strip())
# print(results)
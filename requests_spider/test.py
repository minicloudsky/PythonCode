#coding: utf-8
import requests
s = requests.Session()
r = requests.get('https://www.baidu.com')
print(r.headers)
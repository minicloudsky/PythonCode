# coding: utf-8
import time
import requests
head = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}

r = requests.get("http://www.baidu.com",headers = head)
s = r.encoding
f = open("1.txt",'r+')
f.write(str(s))
f.close()


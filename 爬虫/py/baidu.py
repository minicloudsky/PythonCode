# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import requests
start_url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E9%80%9A%E5%A4%A9%E7%8B%84%E4%BB%81%E6%9D%B0&ct=201326592&ic=0&lm=-1&width=&height=&v=flip"
r = requests.get(start_url)
print(r.status_code)

reg = "http://www.(.*?).jpg"
reg = re.compile(reg)
url = re.findall(reg,r.text)
list = []
for i in url:
        s = "http://www."+str(i)+".jpg"
        s.encode(s,"utf-8")
for i in list:
        print(i)
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
def getPageUrl(page_url):
	req = requests.get(page_url,headers = header)
	txt = r.text()
	url = re.findall(reg,txt)
	for i in url:
		print(i)


def downloadPic(url):
        req = requests.get(url,headers=header)
        with open('1.jpg','ab') as f:
                f.write(img.content)
                f.close()
if __name__ =='__main__':
        



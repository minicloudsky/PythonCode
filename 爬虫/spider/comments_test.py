# coding: utf-8
import requests
import re
from urllib.parse import quote
import os
import codecs
from pandas import DataFrame
from lxml import etree
header = {'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



if __name__ == '__main__':
    url = 'https://movie.douban.com/review/9168758/'
    r = requests.get(url,headers = header)
    # print(r.text)
    img = re.findall(re.compile('<img src="(.+?).jpg"'),r.text)
    image = [i +".jpg" for i in img]
    print(image)
    for i in image:
        r = requests.get(i,headers = header)
        with open(r,'wb') as f:
            f.write(r.content)

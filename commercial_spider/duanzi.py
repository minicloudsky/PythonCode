from lxml import etree
import requests
from selenium import webdriver
header = {'User-Agent':''
                       ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
r = requests.get('http://duanziwang.com/',headers = header)
selector = etree.HTML(r.text)
text = selector.xpath('//*[@id="910"]/div[2]/')
print(text)

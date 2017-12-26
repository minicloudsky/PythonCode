#coding: utf-8
from selenium import webdriver
import requests
import re
import codecs
from bs4 import BeautifulSoup
import time
import os
url = 'https://weibo.cn/'
username = ''
pwd = ''
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginName"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="loginAction"]').click()
time.sleep(2)
list = []
for i in range(1,34):
    list.append('https://weibo.cn/actorleeminho?page={}'.format(i))
big_img_url = []
regex = '<a href="http://weibo.cn/mblog/pic/(.+?)"'
reg = re.compile('src="(.+?)" alt="图片加载中..."')
regex = re.compile(regex)
image = []
for i in list:
    response = driver.get(i)
    time.sleep(1)
    img = re.findall(regex,driver.page_source)
    for i in img:
        big_img_url.append('http://weibo.cn/mblog/pic/'+i)
print("一共%s张图片".format(len(big_img_url)))
for i in big_img_url:
    try:
        driver.get(i)
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/a').click()
        image.append(driver.current_url)
    except:
        pass
if not (os.path.exists("D:\\liminhao")):
    os.mkdir("D:\\liminhao")
count = 0
for i in image:
    print("正在下载%s张".format(count))
    r = requests.get(i,headers = header)
    with codecs.open("D:\\liminhao\\"+str(count)+".jpg",'wb',encoding='utf-8') as f:
        f.write(r.content)









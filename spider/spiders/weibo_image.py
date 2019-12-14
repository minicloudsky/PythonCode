#coding: utf-8
from selenium import webdriver
import requests
import re
import codecs
import random
from bs4 import BeautifulSoup
import time
import os
# 起始url
url = 'https://weibo.cn/'
# 输入新浪微博手机号或邮箱
username = '15716302402'
# 输入新浪微博账号密码
pwd = 'jyw83139200..'
user_id = '1909018271'
# options = webdriver.ChromeOptions()
# 进入浏览器设置
# 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
# options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)
#  Chrome/63.0.3239.84 Safari/537.36"')


def Weibo_Image(user_id):
    header = {'Host':'weibo.cn','Upgrade-Insecure-Requests':'1','User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="loginName"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="loginAction"]').click()
    time.sleep(3)
    list = []
    for i in range(1,50):
        list.append('https://weibo.cn/{}?page={}'.format(user_id,i))
    big_img_url = []
    regex = '<a href="http://weibo.cn/mblog/pic/(.+?)"'
    reg = re.compile('src="(.+?)" alt="图片加载中..."')
    regex = re.compile(regex)
    image = []
    for i in list:
        response = driver.get(i)
        time.sleep(3)
        img = re.findall(regex,driver.page_source)
        for i in img:
            big_img_url.append('http://weibo.cn/mblog/pic/'+i)
    print("一共{}张图片".format(len(big_img_url)))
    if not (os.path.exists("D:\\" + user_id)):
        os.mkdir("D:\\" + user_id)
    count = 0
    for i in big_img_url:
        try:
            driver.get(i)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[3]/a').click()
            print("正在下载第{}张".format(count))
            r = requests.get(driver.current_url, headers=header,timeout=5)
            with open("D:\\" + user_id + "\\" + str(count) + ".jpg", 'wb') as f:
                f.write(r.content)
            count += 1
        except TimeoutError:
            pass


if __name__ == '__main__':
    user_id = '1909018271'
    Weibo_Image(user_id)










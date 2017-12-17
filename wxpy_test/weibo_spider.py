#coding: utf-8
import codecs
import time
import random
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://weibo.com/')
time.sleep(6)
username = ''
pwd = ''
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click()
while True:
    time.sleep(2)
    text = '最新会员电影免费看^_^,请亲们及时保存到百度网盘即可观看哦。\r\n'
    f = codecs.open("E:\\wechat\\movie.txt", 'r', encoding='utf-8').readlines()
    for i in f:
        text += i
    driver.get('https://weibo.com/u/5710928238/home?leftnav=1#1513515573373')
    driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys(text)
    time.sleep(random.randrange(1,5))
    driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
    time.sleep(random.randrange(100,200))
    file = codecs.open("E:\\wechat\\movie.txt", 'r', encoding='utf-8').readlines()
    if file ==f:
        print("电影未更新，无需发微博")
        time.sleep(random.randrange(300,400))
    else:
        print("即将发微博")
        continue



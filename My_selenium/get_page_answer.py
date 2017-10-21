#coding: utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import os
import requests
from lxml import etree
import time
def login(driver):
    login_url = 'https://www.zhihu.com/#signin'
    # 点击使用密码登录
    driver.maximize_window()
    driver.get(login_url)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
    user = ''
    pwd = ''
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys(user)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys(pwd)
    time.sleep(8)
    # 点击登录按钮
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()
    time.sleep(3)
    return driver
    print(driver.current_url)
url = 'https://www.zhihu.com/people/vajiajia/answers'
driver = webdriver.Chrome()
driver = login(driver)
driver.get(url)
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[3]/button').click()
# text = driver.find_element_by_xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[1]/div/span').text
# print(text)
# print(driver.page_source)
reg = ''


xp = '//*[@id="ProfileMain"]/div[1]/ul/li[3]/a/span'
ask = driver.find_element_by_xpath(xp).text
print(ask)














# driver.get(url)
# logo = '<img class="Avatar Avatar--large UserAvatar-inner" width="160" height="160" src="https://(.+?).jpg"'
# logo_url = re.findall(re.compile(logo),driver.page_source)
# print(logo_url)
# driver.get("https://www.zhihu.com/people/vajiajia/following?page=4")
# regex = '<meta itemprop="zhihu:voteupCount" content="(.+?)"'
# regex = re.compile(regex)
# like = re.findall(regex,driver.page_source)
# like = like[0]
# username = re.findall(re.compile('<span class="ProfileHeader-name">(.+?)</span>'),driver.page_source)
# username = username[0]
# thank = re.findall(re.compile('<!-- react-text: 2544 -->(.+?)<!-- /react-text -->'),driver.page_source)
# # thank = thank[0]
# collect =re.findall(re.compile('<!-- react-text: 2546 -->(.+?)<!-- /react-text -->'),driver.page_source)
# # collect = collect[0]
# follower = driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[2]/div/a[2]/div[2]/text()')
# print(like)
# print(username)
# print(thank)
# print(collect)
# print(follower)

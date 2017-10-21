#coding: utf-8
import selenium
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
first_url = 'http://www.baidu.com'
print('now access %s' %(first_url))
dr.get(first_url)
time.sleep(1)
second_url = 'http://www.news.baidu.com'
print("now access %s "%(second_url))
dr.get(second_url)
time.sleep(1)
print("back to %s" %(first_url))
dr.back()
time.sleep(1)
print("forward to %s" %(second_url))
dr.forward()
time.sleep(1)
dr.quit()

#coding: utf-8
import requests
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://weibo.com/')
time.sleep(8)
driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("1")
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys("")
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys("")
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
time.sleep(2)
print(driver.current_url)
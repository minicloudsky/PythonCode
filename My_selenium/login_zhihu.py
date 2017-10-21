#coding: utf-8
from selenium import webdriver
from time import sleep
url = 'https://www.zhihu.com/#signin'
# 点击使用密码登录
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
user = ''
pwd = ''
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys(user)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys(pwd)
sleep(10)
# 点击登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()
sleep(5)
print(driver.current_url)
print(driver.page_source)
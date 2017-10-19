#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = 'https://weibo.com/'
login_url = '//*[@id="weibo_top_public"]/div/div/div[3]/div[2]/ul/li[3]/a'
input_xpath = './/*[@id="layer_15083299373991"]/div[2]/div[3]/div[3]/div[1]/input'
pwd_xpath = './/*[@id="layer_15083299373991"]/div[2]/div[3]/div[3]/div[2]/input'
login_btn = './/*[@id="layer_15083299373991"]/div[2]/div[3]/div[3]/div[6]/a'
driver = webdriver.Chrome()
driver.get(url)
driver.set_window_size(1000,1000)
time.sleep(5)
driver.find_element_by_xpath(login_url).click()
print('已点击登录链接')
time.sleep(5)
driver.find_element_by_name('username').send_keys("")
print('已经输入账号')
driver.find_element_by_name('password').send_keys("")
print('已经输入密码')
driver.find_element_by_xpath(login_btn).click()
print('已经点击登录')
time.sleep(5)
print(driver.current_url)

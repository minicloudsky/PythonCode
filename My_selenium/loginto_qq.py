#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
url = 'https://i.qq.com/'
switch = '//*[@id="switcher_plogin"]'
driver = webdriver.Chrome()
driver.get(url)
driver.switch_to_frame('login_frame')
driver.find_element_by_xpath(switch).click()
time.sleep(5)
user = '//*[@id="u"]'
pwd = '//*[@id="p"]'
submit = '//*[@id="login_button"]'
qq = '37'
password = ''
driver.find_element_by_xpath(user).send_keys(qq)
driver.find_element_by_xpath(pwd).send_keys(password)
driver.find_element_by_xpath(submit).click()
print(driver.current_url)
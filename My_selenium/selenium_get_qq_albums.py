#coding:utf-8
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
#登录qq
def login_qq(driver):
    url = 'https://i.qq.com/'
    switch = '//*[@id="switcher_plogin"]'
    driver.get(url)
    driver.switch_to_frame('login_frame')
    driver.find_element_by_xpath(switch).click()
    time.sleep(3)
    user = '//*[@id="u"]'
    pwd = '//*[@id="p"]'
    submit = '//*[@id="login_button"]'
    qq = '3'
    password = ''
    driver.find_element_by_xpath(user).send_keys(qq)
    driver.find_element_by_xpath(pwd).send_keys(password)
    driver.find_element_by_xpath(submit).click()
    time.sleep(3)
#进入相册
def enter_album(driver):
    # 点击主页的相册链接
    driver.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[3]/a').click()
    time.sleep(2)
    driver.switch_to.frame(0)
    time.sleep(2)
    # 切换到相册框架
    album = '//*[@id="js-album-list-class"]/div[1]/div[2]/ul/li[1]/div/div[1]/a'
    driver.find_element_by_xpath(album).click()
    # 点击第一张图片
    # photo1 = '//*[@id="js-module-container"]/div[1]/div[3]/div[1]/ul/li[1]/div/div[1]/a'
    # driver.find_element_by_xpath(photo1).click()
if __name__ == '__main__':
    driver = webdriver.Chrome()
    login_qq(driver)
    enter_album(driver)
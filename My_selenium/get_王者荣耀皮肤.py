#coding: utf-8
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests
import time
url = 'http://pvp.qq.com/'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
# driver.find_element_by_xpath('//*[@id="header"]/div[1]/ul/li[2]/a').click()
# print(driver.page_source)
# print(driver.current_window_handle)
moveElement = driver.find_element_by_xpath('//a[@title="游戏资料"]')
ActionChains(driver).move_to_element(moveElement).perform()
driver.find_element_by_xpath('//a[@title="游戏壁纸"]').click()
# print(driver.current_window_handle)
# print(driver.window_handles)
all_h = driver.window_handles
driver.switch_to_window(all_h[1])
time.sleep(3)
if not os.path.exists("D:\\王者荣耀"):
    os.mkdir("D:\\王者荣耀")
page_num = 0
while page_num<=12:
    soup = BeautifulSoup(driver.page_source,'html.parser')
    Lists = soup.find_all('div',{'class':'p_newhero_item'})
    titleLists = []
    herfLists = []
    for item in Lists:
        sub_soup = BeautifulSoup(str(item),'html.parser')
        titleList = sub_soup.find('h4')
        titleLists.append(titleList.text)
        linklist = sub_soup.find('li',{'class':'sProImgL6'})
        soup = BeautifulSoup(str(linklist),'html.parser')
        a = soup.find('a')
        herfLists.append(a['href'])
    for i in range(len(titleLists)):
        url = herfLists[i]
        r = requests.get(url).content
        path = titleLists[i] + '.jpg'
        try:
            with open(path,'wb') as f:
                f.write(r)
                print('保存成功%d.jpg' %titleLists[i])
        except:
            print('保存失败')
    driver.find_element_by_xpath('//a[@class="downpage"]').click()
    time.sleep(3)
    page_num +=1
driver.close()
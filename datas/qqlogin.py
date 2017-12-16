#coding: utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
url = " https://qzone.qq.com"
driver = webdriver.Chrome()
driver.set_window_position(20,40)
driver.set_window_size(1100,1100)
# 打开登录页面
driver.get(url)
#登录表单在页面的框架中，所以要切换到该框架
driver.switch_to_frame("login_frame")
# 通过使用选择器选择到表单元素进行模拟和点击按钮提交
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
# input your qq number
driver.find_element_by_id('u').send_keys('3013568147')
driver.find_element_by_id('p').clear()
# input psssword
driver.find_element_by_id('p').send_keys('appijyw231870t;;')
driver.find_element_by_id('login_button').click()
time.sleep(5)
print("登录成功")
#相册xpath
xpath = '//*[@id="menuContainer"]/div/ul/li[3]/a'
# driver.find_element_by_xpath(xpath).click()
time.sleep(5)
# 具体某个相册的xpath
photo_xpath = '//*[@id="js-album-list-class"]/div[1]/div[2]/ul/li[1]/div/div[2]/div/div/a'
# time.sleep(5)
# driver.find_element_by_xpath(photo_xpath).click()
print(driver.current_url)
# print(driver.page_source)
print("即将自动发说说")
saying_xpath = '//*[@id="$1_substitutor_content"]'
driver.find_element_by_xpath(saying_xpath).send_keys(" Hello,I am controled by automate machine")
saying_send_xpath = '//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]'
driver.find_element_by_xpath(saying_send_xpath).click()
print("saying send successfully")
like = '//*[@id="fct_1659531644_311_5_1508323928_0_1"]/div[3]/div[1]/p/a[3]/i'
# driver.find_element_by_xpath(like).click()
print("like successfully")




#coding:utf-8
from selenium import webdriver
url = 'https://v.qq.com'
driver = webdriver.Chrome()
driver.get(url)
driver.set_window_size(1000,1000)
input_box= '//*[@id="keywords"]'
driver.find_element_by_xpath(input_box).send_keys("通天狄仁杰")
driver.find_element_by_xpath('//*[@id="searchForm"]/div/button/span').click()
print(driver.current_url)
#coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
url = "http://www.icourse163.org/"
driver = webdriver.Chrome()
driver.set_window_position(20,40)
driver.set_window_size(1100,1100)
driver.get(url)
time.sleep(3)
login_btn = 'm-index-person-loginBtn'
driver.find_element_by_id('auto-id-1508330775659').click()
qq_class = 'f-icon j-slink qq u-icon-qq'
driver.find_element_by_xpath(qq_class).click()

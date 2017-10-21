#coding: utf-8
from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('send_keys.html')
driver.get(file_path)
driver.find_element_by_id('A').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('A').send_keys(Keys.CONTROL,'x')
time.sleep(1)
driver.find_element_by_id('B').send_keys(Keys.CONTROL,'v')
time.sleep(1)
driver.find_element_by_id('A').send_keys('waitr','-','webdriver',Keys.SPACE,'is',Keys.SPACE,'better')
time.sleep(2)
driver.quit()

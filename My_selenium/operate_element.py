#coding: utf-8
from selenium import webdriver
import time
import os
if 'HTTP_PROXY' in os.environ: del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
file_path = 'file:///' +os.path.abspath('element.html')
driver.get(file_path)
driver.find_element_by_link_text('Link1').click()
time.sleep(1)
driver.find_element_by_link_text('Link1').click()
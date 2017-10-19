#coding: utf-8
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
url = "https://www.baidu.com"
#调用环境变量指定的PhantomJs浏览器创建浏览器对象
driver = webdriver.PhantomJS()
driver.get(url)
data = driver.find_element_by_id("wrapper").text
# print(data)
print(driver.title)
# driver.save_screenshot("baidu.png")
# driver.find_element_by_id("kw").send_keys(u"长城")
# driver.find_element_by_id("su").click()
# time.sleep(5)
# driver.save_screenshot("长城.png")
# print(driver.page_source)
# print(driver)
#全选搜索框内容
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("itcast")
# time.sleep(3)
# driver.save_screenshot("itcast.png")
# print(driver.current_url)
#ctrl +a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# ctrl+ x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
# 输入框重新输入内容
driver.find_element_by_id("su").send_keys("itcast")
# 模拟Enter回车键
driver.find_element_by_id("su").send_keys(Keys.RETURN)
# clear 输入框内容
driver.find_element_by_id("kw").clear()
time.sleep(4)
driver.save_screenshot("itcast.png")
driver.close()
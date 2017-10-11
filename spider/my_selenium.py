from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
assert "百度" in driver.title
print(driver.title)
elem = driver.find_element_by_name("wd")
elem.send_keys("zhihu")
elem.send_keys(Keys.RETURN)
print(driver.page_source)
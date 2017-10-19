#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS()
import selenium
# 假设有如下输入框
#  <input type = "text" name = "user-name id = "passwd-id"/>
# 获取id标签值
# element = driver.find_element_by_id("passwd-id")
# 获取 name 标签值
# element = driver.find_element_by_name("user-name")
chrome = selenium.webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
chrome.add_cookie("""q_c1=f625095eb0664c8fa22d2c16e29f4235|1506771832000|1506771832000; d_c0="AAACJBC6dAyPTs36aiC5urxd80qME08pwns=|1506771833"; _zap=b98afb6d-0ed0-4ad9-b348-8080a9f2247f; infinity_uid="2|1:0|10:1507277797|12:infinity_uid|24:NzU3OTU3NzcxODgxNjE5NDU2|ce52f55e2140a3e8468c73a382e97d0453b0035383331bd1c95e0d170b8ec093"; r_cap_id="YTJhNzllZGU2NTM5NDI0ZGIwNTYwNjM0NDkzNjM3ODk=|1508203954|921eb29a954923566bee75962cff8b5cfe8adf73"; cap_id="NGM5MWY5YmQ3NzBhNDc2N2I2ZGY5OWY4Yjg0YWUwOTA=|1508203954|864cd298b179cbbb44c76bf5e4bf5f4f2abd13f8"; z_c0=Mi4xY0M5eUFnQUFBQUFBQUFJa0VMcDBEQmNBQUFCaEFsVk4zLW9NV2dDeWE5bnZON2dPUTNJQ19ndXE5amdWcWRaWEdn|1508203999|af79c25ab523b573fcaf34a11d6ad8a04d512f9b; __utma=51854390.1629764455.1508304368.1508304368.1508304368.1; __utmz=51854390.1508304368.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20160105=1^3=entry_date=20160105=1; aliyungf_tc=AQAAANXUzQnELg0AYJhY3gynNt3GMSFC; _xsrf=a7291116-026a-43c4-bf42-2ad624a4e8fe""")
chrome.get("https://zhihu.com")
search = chrome.find_element_by_id("Popover-46406-66052-toggle")
search.send_keys("军事")
search.screenshot("junshi.png")
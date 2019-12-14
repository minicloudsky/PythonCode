from selenium import webdriver
from random import choice
import time
import re
url = 'https://weibo.com/'
username = ''
password = ''

# chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('test-type')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


list = [""" #随手赚钱# """, """ #掌赚宝-手机赚钱# """, """ #微博赚钱季# """, """ #躺着赚钱,卧床不起# """,
""" #宝妈赚钱# """, """ #学生赚钱# """]
text = """ 投吧问卷调查，就是在网上做问卷调查，手机电脑都可以做，注册个账号就可以了，不需要投入一分钱，每天有时间在网站上回答一些特别简单的问卷调查，满10元就可以支付宝提现哦，一天150-200左右，感兴趣的朋友可以来试试。http://www.votebar.com/r.aspx?r=54082904119156"""

result = []
for i in range(1):
    result.append(choice(list))

message = "".join(set(result))
message = message + text
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get(url)
time.sleep(15)
driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
time.sleep(2)
# login
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(5)
for i in range(230):
	driver.find_element_by_xpath('//*[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a').click()
	time.sleep(2)
	driver.get('https://weibo.com/5710928238/profile?profile_ftype=1&is_all=1#_0')
	time.sleep(2)

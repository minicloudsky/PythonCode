from selenium import webdriver
from random import choice
import time
import re
url = 'https://weibo.com/'
username = '15716302402'
password = 'jyw83139200..'

# chrome option
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('test-type')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


list = [""" #随手赚钱# """, """ #掌赚宝-手机赚钱# """, """ #微博赚钱季# """, """ #躺着赚钱,卧床不起# """,
""" #宝妈赚钱# """, """ #学生赚钱# """]
text = """ 投吧问卷调查，就是在网上做问卷，回答一些问题，手机电脑都可以做，注册个账号就可以了，不需要投入一分钱，每天有时间在网站上回答一些简单的问卷调查，满10元就可以支付宝提现哦，一天150-200左右，感兴趣的朋友可以来试试。http://www.votebar.com/r.aspx?r=54082904119156"""

result = []
for i in range(1):
    result.append(choice(list))

message = "".join(set(result))
message = message + text
driver = webdriver.Chrome()
driver.get(url)
time.sleep(15)
driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
time.sleep(2)
# login
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(5)
regex = re.compile(r"""<a target="_blank" class="S_txt1" href=".*?" title=".*?">(.+?)</a>""")
hot_topic = re.findall(regex,driver.page_source)
print(hot_topic)
topic = []
for i in range(2):
    topic.append(choice(hot_topic))
text = "".join(set(topic))
text += message
print(text)
# send text
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys(text)
time.sleep(3)
driver.find_element_by_name('pic1').send_keys("D:\\pycharm\\PythonCode\\commercial_spider\\votebar\\1.png")
time.sleep(3)
driver.find_element_by_name('pic1').send_keys("D:\\pycharm\\PythonCode\\commercial_spider\\votebar\\2.png")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
print(driver.current_url)


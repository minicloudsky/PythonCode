from selenium import webdriver
from random import choice,randint
import time
import re
url = 'https://weibo.com/'
username = '15716302402'
password = 'jyw83139200..'
image = randint(1,650)
list = [""" #随手赚钱# """, """ #掌赚宝-手机赚钱# """, """ #微博赚钱季# """, """ #躺着赚钱,卧床不起# """,
""" #宝妈赚钱# """, """ #学生赚钱# """]
text = """ #王思聪# #支付宝# 王思聪发一亿支付宝大红包，打开支付宝首页搜索 4338455,瓜分王思聪1亿红包，先到先得."""

result = []
for i in range(1):
    result.append(choice(list))

message = "".join(set(result))
message = message + text
driver = webdriver.Chrome()
driver.get(url)
time.sleep(30)
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
#driver.find_element_by_name('pic1').send_keys("D:\\pycharm\\PythonCode\\commercial_spider\\votebar\\1.png")
#time.sleep(3)
driver.find_element_by_name('pic1').send_keys("D:\\image\\{}.jpeg".format(str(image)))
driver.find_element_by_name('pic1').send_keys("D:\\pycharm\\PythonCode\\commercial_spider\\votebar\\alipay.png")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
print(driver.current_url)
time.sleep(3)
driver.close()


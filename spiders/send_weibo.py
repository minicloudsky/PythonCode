from selenium import webdriver

url = 'https://weibo.com/'
username = ''
password = ''
text = """#随手赚钱# #掌赚宝-手机赚钱# #微博赚钱季# #躺着赚钱,卧床不起# 
#随手赚钱# 投吧问卷调查，就是在网上做问卷调查，手机电脑都可以做，注册个账号就可以了，每天有时间的时候点点，回答一些特别简单的问题，
满10元就可以支付宝提现哦，一天150-200左右，感兴趣的朋友可以来试试。http://www.votebar.com/r.aspx?r=54082904119156
"""
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_id('loginname').send_keys(username)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(password)
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[2]/textarea').send_keys(text)
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="v6_pl_content_publishertop"]/div/div[3]/div[1]/a').click()
print(driver.current_url)
# coding: utf-8
from requests import Session
from time import sleep
req = Session()
req.headers.clear() 
chromePath = r'D:\Software\chromedriver.exe'
wd = webdriver.Chrome(executable_path= chromePath) 
zhihuLogInUrl = 'https://www.zhihu.com/signin'
wd.get(zhihuLogInUrl)
wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys('username') 
wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys('password')
sleep(10) #手动输入验证码 
wd.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').submit() 
sleep(10)#等待Cookies加载
cookies = wd.get_cookies()
for cookie in cookies:
    req.cookies.set(cookie['name'],cookie['value'])

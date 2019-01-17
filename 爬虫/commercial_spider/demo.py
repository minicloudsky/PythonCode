from selenium import webdriver
import pytesseract
import time
import re
import requests
from PIL import Image
from bs4 import BeautifulSoup
username = '15716302402'
password = 'htc123456'
driver = webdriver.Chrome()
driver.get('http://www.yundama.com/')
driver.find_element_by_xpath('//*[@id="verifyImg"]').click()
soup = BeautifulSoup(driver.page_source,'lxml')
text = soup.find_all(name='img')
captcha_id = soup.find_all(attrs={'id':'verifyImg'})[0].attrs['src']
captcha = 'http://www.yundama.com{}'.format(captcha_id)
r = requests.get(captcha,timeout = 50)
with open("captcha.png",'wb') as f:
    f.write(r.content)
text = pytesseract.image_to_string(Image.open('captcha.png'))
print(text)
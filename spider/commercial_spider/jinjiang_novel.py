import requests
from lxml import etree
import re
import time
from selenium import webdriver
novel = []
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
driver = webdriver.Chrome()
for i in range(1,77):
    response = driver.get('http://www.jjwxc.net/onebook.php?novelid=2315424&chapterid={}'.format(str(i)))
    time.sleep(3)
    print(driver.page_source)
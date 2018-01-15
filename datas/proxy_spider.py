#coding: utf-8
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('----proxy-server=http://182.88.255.110:8123')
chrome = webdriver.Chrome(chrome_options=chrome_options)
url = 'http://ip.chinaz.com/getip.aspx'
votebar = 'http://www.votebar.com/r.aspx?r=54082904119156'
chrome.get(url)
print(chrome.page_source)
chrome.get(votebar)


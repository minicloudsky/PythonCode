# coding: utf-8
from bs4 import BeautifulSoup
import requests
def captcha(captcha_url):
    s =1
def zhihuLogin():
    session = requests.Session()
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

    url = "https://www.zhihu.com/#signin"
    html = session.get(url,headers = headers).text
    bs = BeautifulSoup(html,'lxml')
    _xsrf = bs.find("input",attrs={"name":"_xsrf"}).get("value")
    print(_xsrf)
    captcha_url = " "
if __name__ == '__main__':
    zhihuLogin()
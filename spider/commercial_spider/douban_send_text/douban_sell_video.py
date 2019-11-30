import time
from selenium import webdriver
import re
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from urllib.parse import urlencode,quote
import requests
username = '15716302402'
password = 'jyw83139200..'
class Douban():

    def __init__(self, username, password,keyword, title, content):
        self.group = []
        self.username = username
        self.password = password
        self.keyword = keyword
        self.title = title
        self.content = content
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.douban.com/")
        self.login()
        self.get_keyword_group()

    def login(self):
        sleep(30)

    def get_keyword_group(self):
        for key in self.keyword:
            self.group = self.get_group(key)
            self.send_all()

    def get_group(self,key):
        self.browser.get("https://www.douban.com/search?cat=1019&q={}".format(quote(key)))
        self.browser.find_element_by_class_name('inp-btn').click()
        self.browser.implicitly_wait(5)
        try:
            self.browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[5]/a').click()
            self.browser.implicitly_wait(2)
        except:
            print("error")
            pass
        self.browser.implicitly_wait(2)
        try:
            for i in range(5):
                self.browser.find_element_by_class_name('result-list-ft').click()
                self.browser.implicitly_wait(5)
        except NoSuchElementException:
            pass
        regex = """href="https://www.douban.com/link2/(.+?)\""""
        temp_group = re.findall(re.compile(regex),self.browser.page_source)
        for i in temp_group:
            self.group.append("https://www.douban.com/link2/{}".format(i))
        print("一共有{}个小组".format(len(self.group)))
        self.group = list(set(self.group))
        return self.group
        # print(self.group)


    def send_all(self):
        for url in self.group:
            self.send_per_group(url)

    def send_per_group(self,url):
        # print(url)
        self.browser.get(url)
        self.browser.implicitly_wait(2)
        # 查找加入小组按钮
        try:
            self.browser.find_element_by_class_name('group-misc').click()
            self.browser.implicitly_wait(3)
        except NoSuchElementException :
            print("找不到加入小组按钮")
            pass
        # 查找发言链接
        try:
            self.browser.find_element_by_class_name('bns').click()
            self.browser.implicitly_wait(3)
        except NoSuchElementException:
            print("找不到发言按钮")
            pass
        # 发帖
        try:
            self.browser.find_element_by_class_name('group-editor-input').send_keys(self.title)
        except NoSuchElementException:
            print("定位标题位置出错")
            pass
        # try:
        #     self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/div/span/span').send_keys(self.content)
        # except NoSuchElementException:
        #     print("send text error")
        #     pass
        try:
            self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div').send_keys(self.title)
            self.browser.find_element_by_xpath('//*[@id="nav-top-actions"]/div/div/a[2]').click()
            sleep(2)
            print("发帖成功")
        except NoSuchElementException:
            print("send image error")
            pass


if __name__ == '__main__':
    keyword = ["洛阳","洛阳兼职"]
    title = """【高薪诚聘】诚聘销售人员若干名，要求24-35岁，高中及以上学历，月均4500-6000，福利好，社保齐全，女士优先。

诚聘管理人员若干名，要求24-35岁，高中及以上学历，有良好沟通能力，月均8000-12000。福利好，社保齐全。

诚聘文员助理3人，要求女性，22-35，月薪3500-5000。社保齐全。
地址：涧西区九都路珠江路口。
有意者微信同电话：15236161092"""
    content = """"【高薪诚聘】诚聘销售人员若干名，要求24-35岁，高中及以上学历，月均4500-6000，福利好，社保齐全，女士优先。

诚聘管理人员若干名，要求24-35岁，高中及以上学历，有良好沟通能力，月均8000-12000。福利好，社保齐全。

诚聘文员助理3人，要求女性，22-35，月薪3500-5000。社保齐全。
地址：涧西区九都路珠江路口。
有意者微信同电话：15236161092"""
    for key in keyword:
        douban = Douban(username, password, keyword, title, content)
        douban.browser.close()

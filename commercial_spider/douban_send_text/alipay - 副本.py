from selenium import webdriver
import re
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from urllib.parse import urlencode,quote
import requests
username = ''
password = ''
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
        self.browser.find_element_by_xpath('//*[@id="form_email"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="form_password"]').send_keys(self.password)
        regex = '<img id="captcha_image" src="(.+?)" alt="captcha"'
        captcha = ''
        try:
            captcha = re.findall(regex, self.browser.page_source)
            captcha = captcha[0]
            r = requests.get(captcha,headers = self.header,timeout=50)
            print(len(r.content))
            with open('captcha.jpg','wb') as f:
                f.write(r.content)
                f.close()
        except:
            print("cann't find captcha")
            pass
        self.browser.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click()
        self.browser.implicitly_wait(2)
        # sleep(15)

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
            # self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[1]/span[1]/span/input').send_keys("D:\\Software\\pycharm\\PythonCode\\commercial_spider\\douban_send_text\\ad.png")
            sleep(3)
            # for i in range(1,5):
            #     self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[1]/span[1]/span/input').send_keys("D:\\Software\\pycharm\\PythonCode\\commercial_spider\\douban_send_text\\{}.png".format(i))
            #     sleep(3)
            self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[1]/span[1]/span/input').send_keys("D:\\pycharm\\PythonCode\\commercial_spider\\douban_send_text\\alipay.png")
            sleep(3)
            self.browser.find_element_by_xpath('//*[@id="nav-top-actions"]/div/div/a[2]').click()
            sleep(2)
            print("发帖成功")
        except NoSuchElementException:
            print("send image error")
            pass


if __name__ == '__main__':
    keyword = ["微信群","兼职","赚钱","支付宝","兼职赚钱","宝妈","宝妈赚钱","大学生兼职"]
    title = "王思聪发一亿支付宝大红包，打开支付宝首页搜索 4338455,瓜分王思聪1亿红包，先到先得. ​​​​"
    content = "this is content"
    for key in keyword:
        douban = Douban(username, password, keyword, title, content)
        douban.browser.close()

from selenium import webdriver
import re
from selenium.common.exceptions import NoSuchElementException
from time import sleep

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
        self.browser = webdriver.Chrome()
        self.browser.get("https://www.douban.com/")
        self.login()
        self.get_group()
        self.send_all()

    def login(self):
        self.browser.find_element_by_xpath('//*[@id="form_email"]').send_keys(self.username)
        self.browser.find_element_by_xpath('//*[@id="form_password"]').send_keys(self.password)
        self.browser.find_element_by_xpath('//*[@id="lzform"]/fieldset/div[3]/input').click()
        self.browser.implicitly_wait(2)
        sleep(15)

    def get_group(self):
        self.browser.find_element_by_xpath('//*[@id="inp-query"]').send_keys(keyword)
        self.browser.find_element_by_class_name('inp-btn').click()
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[5]/a').click()
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
        self.group = set(self.group)
        # print(self.group)


    def send_all(self):
        for url in self.group:
            self.parse_group(url)

    def parse_group(self,url):
        print(url)
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
            self.browser.find_element_by_xpath('//*[@id="group-editor-root"]/div/div[2]/div[2]/div/div[1]/span[1]/span/input').send_keys("D:\\Software\\pycharm\\PythonCode\\commercial_spider\\douban_send_text\\votebar.jpg")
            sleep(3)
            self.browser.find_element_by_xpath('//*[@id="nav-top-actions"]/div/div/a[2]').click()
            sleep(2)
            print("发帖成功")
        except NoSuchElementException:
            print("send image error")
            pass


if __name__ == '__main__':
    keyword = ["大学生","赚钱","微信","微信群","兼职","兼职赚钱"]
    title = "投吧问卷调查，一天150-200左右http://www.votebar.com/r.aspx?r=54082904119156"
    content = "this is content"
    for key in keyword:
        douban = Douban(username, password, keyword, title, content)
        douban.browser.close()

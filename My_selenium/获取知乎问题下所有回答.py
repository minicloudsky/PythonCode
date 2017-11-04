#coding: utf-8
# written by 瞻彼淇奥
# win10+pycharm +python3.54
from selenium import webdriver
import time
import re
import os
from bs4 import BeautifulSoup
import requests
from lxml import etree
import codecs
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
class zhihu_User():
    def __init__(self,page_num,question_id,username,password,path):
        self.question_id  = question_id
        self.question_url = 'https://www.zhihu.com/question/'+str(self.question_id)+'/answers/created'
        self.username = username
        self.password = password
        self.path = path
        self.page_num = page_num
        self.answer = []
        self.image_list = []
        self.avatar = []
        self.driver = webdriver.Chrome()
        self.login(self.driver)
        self.title = ""
        self.get_title()
        self.all_question_url = self.generate_url()
        print("%s 一共有 %s 页网页 " %(self.title,self.page_num))
        self.get_answer()
        self.driver.close()
        self.write_answer()
        self.download_image()
        self.download_avatar()
    # 登录到知乎
    def login(self,driver):
        login_url = 'https://www.zhihu.com/#signin'
        # 点击使用密码登录
        driver.get(login_url)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys(self.username)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys(self.password)
        # wait for the user to click capacha
        time.sleep(8)
        # 点击登录按钮
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()
        time.sleep(3)
        print(driver.current_url)
        print("登录知乎成功")
    # 获取问题的标题
    def get_title(self):
        self.driver.get(self.question_url)
        title = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1').text
        self.title = title
        print(title)
        if not os.path.exists(self.path+"\\"+self.title):
            os.mkdir(self.path+"\\"+self.title)
    # 生成每个回答的xpath
    def generate_xpath(self):
        list = []
        for i in range(1,21):
            list.append('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div['+str(i)+']/div/div[2]/div[1]')
        return list
    # 生成每一页回答对应的url
    def generate_url(self):
        list = []
        for i in range(1,self.page_num+1):
            list.append("https://www.zhihu.com/question/"+str(self.question_id)+'/answers/created?page='+str(i))
        print("生成每一页链接成功")
        return list
    # 获取回答和图片，其中image是每个回答里的图片，avatar是每一页的用户头像
    def get_answer(self):
        page = 0
        answers = self.all_question_url
        xpaths = self.generate_xpath()
        img_regex = 'data-original="(.+?)"'
        img_regex = re.compile(img_regex)
        image = []
        avatar = "https:(.+?).jpg"
        avatar  = re.compile(avatar)
        for answer in answers:
            print("正在获取第 %s 页" %(page))
            self.driver.get(answer)
            time.sleep(3)
            image = re.findall(img_regex,self.driver.page_source)
            for i in image:
                self.image_list.append(i)
            tmp_url = re.findall(avatar,self.driver.page_source)
            for i in tmp_url:
                self.avatar.append("https:"+i+".jpg")
            for xpath in xpaths:
                try:
                    tmp_answer = self.driver.find_element_by_xpath(xpath).text
                    self.answer.append(tmp_answer)
                except :
                    pass
            page+=1
        self.image_list = set(self.image_list)
        self.avatar = set(self.avatar)
        print("一共有 %s 张 图片" %(len(self.image_list)))
        print("一共有 %s 张头像" %(len(self.avatar)))
    # 把所有回答写入txt文件
    def write_answer(self):
        if not os.path.exists(self.path+"\\"+self.title+"\\"):
            os.mkdir(self.path+"\\"+self.title+"\\")
        string  = ""+self.title+"\r\n"
        paths = self.path + "\\" + self.title + ""
        for i in self.answer:
            string += i
            string += "\r\n"
        try:
            with codecs.open(paths+"\\answer.txt",'w',
                                 encoding='utf-8') as f:
                f.write(string)
                f.close()
            print("答案写入文件成功")
        except IOError:
            print("写入文件失败")
    # 下载回答里的图片
    def download_image(self):
        if not os.path.exists(self.path+"\\"+self.title+"\\"+"data-original"):
            os.mkdir(self.path+"\\"+self.title+"\\"+"data-original")
        count =1
        for i in self.image_list:
            img = i[-4:]
            if img == 'jpeg':
                img = ".jpeg"

            try:
                r = requests.get(i, headers=header, timeout=60)
                print("正在下载第 %s 张图片" % (count))
                with codecs.open(self.path+"\\"+self.title+"\\"+"data-original"+"\\"+str(count)+img,'wb') as f:
                    f.write(r.content)
                count += 1
            except:
                pass
    # 下载头像
    def download_avatar(self):
        if not os.path.exists(self.path + "\\" + self.title + "\\" + "avatar"):
            os.mkdir(self.path + "\\" + self.title + "\\" + "avatar")
        count = 1

        for i in self.avatar:
            try:
                r = requests.get(i, headers=header,timeout = 60)
                with codecs.open(self.path + "\\" + self.title + "\\" + "avatar" + "\\" + str(count) +".jpg","wb") as f:
                    f.write(r.content)
                print("正在下载第 %s 张头像 " %(count))
                count += 1
            except:
                pass
if __name__ == '__main__':
    # 要爬取的问题id，看一下浏览器的url，比如该问题url是https://www.zhihu.com/question/30850162/answers/created，
    # 就在下面输入30850162，记得程序运行后要记得点击下程序打开的浏览器页面上知乎的验证码哦^_^
    question_id = '30850162'
    # 你的用户名
    username = ''
    # 你的知乎密码
    password = ''
    # 存储路径
    path = "D:\\zhihu"
    # 先点击知乎问题下面的按照时间排序，然后下拉页面到最后，有个1,2,3把总页数写到这里，其实，主要还是我selenium定位找不到这个数字。。。
    page_num = 207
    zhihu = zhihu_User(page_num,question_id, username, password, path)




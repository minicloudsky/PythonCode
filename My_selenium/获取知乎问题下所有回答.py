#coding: utf-8
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

    def get_title(self):
        self.driver.get(self.question_url)
        title = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1').text
        self.title = title
        print(title)
        if not os.path.exists(self.path+"\\"+self.title):
            os.mkdir(self.path+"\\"+self.title)
    def generate_xpath(self):
        list = []
        for i in range(1,21):
            list.append('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div['+str(i)+']/div/div[2]/div[1]')
        return list

    def generate_url(self):
        list = []
        for i in range(1,self.page_num+1):
            list.append("https://www.zhihu.com/question/"+str(self.question_id)+'/answers/created?page='+str(i))
        print("生成每一页链接成功")
        return list
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
    def download_image(self):
        if not os.path.exists(self.path+"\\"+self.title+"\\"+"data-original"):
            os.mkdir(self.path+"\\"+self.title+"\\"+"data-original")
        count =1
        for i in self.image_list:
            img = i[-4:]
            if img == 'jpeg':
                img = ".jpeg"
            r = requests.get(i,headers = header,timeout = 60)
            print("正在下载第 %s 张图片" %(count))
            try:
                with codecs.open(self.path+"\\"+self.title+"\\"+"data-original"+"\\"+str(count)+img,'wb') as f:
                    f.write(r.content)
                count += 1
            except:
                pass
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
    # 要爬取的问题
    question_id = '43551423'
    # 你的用户名
    username = '15716302402'
    # 你的知乎密码
    password = 'jyw831392'
    # 存储路径
    path = "D:\\zhihu"
    page_num = 481
    zhihu = zhihu_User(page_num,question_id, username, password, path)




#coding: utf-8
# win10+python3.5
# written by 瞻彼淇奥
from selenium import webdriver
import time
import re
import os
from bs4 import BeautifulSoup
import requests
from lxml import etree
import codecs
class zhihu_User():
    def __init__(self,user_id,username,password,path):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.path = path
        self.all_answer_url = []
        self.all_question_title = ''
        self.logo_url = ''
        self.header_name = ''
        self.like = ''
        self.ask = ''
        self.follower = ''
        self.following = ''
        self.thank_collect = ''
        self.profile = ''
        self.description = ''
        self.location = ''
        self.driver = webdriver.Chrome()
        # self.driver.set_window_size(500,500)
        # 登录
        #self.login(self.driver)
        self.get_user_info()
        self.get_user_logo()
        # 回答页的总数
        self.page_answer = self.generate_answer_url()
        self.question_answer_url = self.get_page_answer()
        self.question_answer_dist = {}
        self.get_each_answer()
        self.write_question_answer()
        self.driver.close()
    def login(self,driver):
        login_url = 'https://www.zhihu.com/#signin'
        # 点击使用密码登录
        # driver.maximize_window()
        driver.get(login_url)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/span').click()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys(self.username)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys(self.password)
        # wait for the user to click capacha
        time.sleep(8)
        # 点击登录按钮
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()
        time.sleep(3)
        # print(driver.current_url)
        print("登录知乎成功")
    #获取用户的回答页总数
    def get_total_num(self):
        url = 'https://www.zhihu.com/people/'+str(self.user_id)+'/answers'
        # print(url)
        self.driver.get(url)
        ans_xp = '//*[@id="ProfileMain"]/div[1]/ul/li[2]/a'
        self.driver.find_element_by_xpath(ans_xp).click()
        time.sleep(2)
        number = 0
        regex = '<button class="Button PaginationButton Button--plain" type="button">(.+?)</button>'
        number = re.findall(re.compile(regex),self.driver.page_source)
        print(number)
        # 判断用户的回答是否为多页，如果只有一页的话返回1
        if len(number) >=2:
            number = number[-1]
        else:
            number = 1
        print(self.header_name+"一共有%s页回答" %(number))
        return number

    # 生成用户主页的回答页链接
    def generate_answer_url(self):
        number = int(self.get_total_num())
        list = []
        for i in range(1, number + 1):
            list.append('https://www.zhihu.com/people/' + self.user_id + '/answers?page=' + str(i))
        return list
    # 获取每一页的回答链接
    def get_page_answer(self):
        question = 'content="https://www.zhihu.com/question/(.+?)"'
        question = re.compile(question)
        temp = []
        question_url = []
        count = 1
        print("正在抓取每一页的链接")
        for i in self.page_answer:
            self.driver.get(i)
            # 等待两秒，否则可能会由于网络延迟，导致页面没加载完，后面就找不到链接了
            time.sleep(2)
            temp = re.findall(question,self.driver.page_source)
            for tmp in temp:
                if len(tmp)>8:
                    question_url.append("https://www.zhihu.com/question/"+tmp)
            count+=1
        print(self.header_name+"一共有 %s 个回答" %(len(question_url)))
        return question_url

    # 获取每一个答案
    def get_each_answer(self):
        count = 1
        reg = 'data-original="https://(.+?)"'
        reg = re.compile(reg)
        list = []
        for url in self.question_answer_url:
            print("正在抓取" + self.header_name + "的 %s  个回答" % (count))
            self.driver.get(url)
            time.sleep(1.5)
            soup = BeautifulSoup(self.driver.page_source,'lxml')
            title = soup.h1.text
            # tmp = url + "\r\n"
            tmp = ""
            title = tmp + title
            try:
                answer = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[2]/div[1]/div[2]/div/div/div[2]/div[1]').text
                self.question_answer_dist[title] = answer
            except Exception:
                pass
            tmp_list = re.findall(reg,self.driver.page_source)
            tmp_list = set(tmp_list)
            for i in tmp_list:
                list.append("https://"+i)
            count +=1
        print(list)
        print(self.header_name + "回答中一共有 %s 张图片,即将开始下载" %len(list))
        list = set(list)
        if not os.path.exists(self.path+"\\"+self.header_name+"\\image"):
            os.mkdir(self.path+"\\"+self.header_name+"\\image")
        count = 0
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'}
        for i in list:
            try:
                r = requests.get(i,headers = header)
                img = i[-4:]
                if img == 'jpeg':
                    img = ".jpeg"
                with codecs.open(self.path+"\\"+self.header_name+"\\image\\"+str(count)+img,'wb') as f:
                    f.write(r.content)
                count+=1
                print("第%s张图片下载成功" %count)
            except IOError:
                print("亲，很抱歉图片保存失败了")

    def write_question_answer(self):
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        string = ""
        for Key,Value in self.question_answer_dist.items():
            string+=Key
            string+="\r\n\r\n\r\n"
            string+=Value
            string+="\r\n\r\n"
        try:
            with codecs.open(path+"\\"+str(self.header_name)+"\\"+self.header_name+"_answer.txt",'w',encoding='utf-8') as f:
                f.write(string)
            f.close()
        except IOError:
            print("写入文件失败")
    # 获取用户信息
    def get_user_info(self):
        self.driver.get('https://www.zhihu.com/people/'+str(self.user_id)+'/answers')
        try:
            xp  = '//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[1]/h1/span[1]'
            self.header_name = self.driver.find_element_by_xpath(xp).text
            if not os.path.exists(path + "\\" + self.header_name):
                os.mkdir(path + "\\" + self.header_name)
            xp = 'voteupCount" content="(.+?)"'
            tmp = re.findall(re.compile(xp),self.driver.page_source)
            self.like = tmp[0]
            self.thank = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]').text
            tmp = '//*[@id="ProfileMain"]/div[1]/ul/li[3]/a/span'
            self.ask = self.driver.find_element_by_xpath(tmp).text
            tmp = re.findall(re.compile('关注了</div><div class="NumberBoard-value">(.+?)</div>'),self.driver.page_source)
            self.following = tmp[0]
            tmp = re.findall(re.compile('关注者</div><div class="NumberBoard-value">(.+?)</div>'),self.driver.page_source)
            self.follower = tmp[0]
            tmp = re.findall(re.compile('<span class="RichText ProfileHeader-headline">(.+?)</span>'),self.driver.page_source)
            self.profile = tmp[0]
            # 点击查看信息按钮，加载出个人信息
            self.driver.find_element_by_xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[3]/button').click()
            self.location = self.driver.find_element_by_xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[1]/div/span').text
            self.description = self.driver.find_element_by_xpath('//*[@id="ProfileHeader"]/div/div[2]/div/div[2]/div[2]/span/div/div[2]/div').text
            tmp = self.driver.find_element_by_class_name('Profile-sideColumnItemValue').text
            self.thank_collect = tmp
            self.thank_collect.strip()
            info = ""
            info+=self.header_name+"\r\n"+"signature: "+self.profile+"\r\n"+"个人描述: "+self.description+"\r\n"
            info+="获得"+str(self.like)+"次赞同"+"\r\n"
            info+="提问了"+str(self.ask)+"个问题"
            info+="关注了"+str(self.following)+"个用户"+"\r\n"
            info+="有"+str(self.follower)+"个关注者"+"\r\n"
            info+=self.thank_collect+"\r\n"+"\r\n"
            info+=self.location

        except Exception:
            pass
        try:
            with codecs.open(self.path+"\\"+self.header_name+"\\info.txt",'wb',encoding='utf-8') as f:
                f.write(info)
            f.close()
        except:
            IOError
            print("写入信息失败")
        print(self.header_name)
        #print(self.profile)
        print("个人描述: "+self.description)
        print("获得 %s 次赞同" %(self.like))
        print("提问了 %s 个问题" %self.ask)
        print("关注了 %s 个用户" %(self.following))
        print("有 %s 个关注者" %(self.follower))
        print(" %s " %(self.thank_collect))
        print(self.location)
    # 获取头像
    def get_user_logo(self):
        print("正在保存 %s 的头像" %self.header_name)
        self.driver.get('https://www.zhihu.com/people/'+str(self.user_id)+'/answers')
        logo = '<img class="Avatar Avatar--large UserAvatar-inner" width="160" height="160" src="https://(.+?).jpg"'
        self.logo_url = re.findall(re.compile(logo), self.driver.page_source)
        self.logo_url= "https://"+self.logo_url[0]+".jpg"
        print(self.header_name+"的头像url为: "+self.logo_url)
        r = requests.get(self.logo_url,timeout = 60)
        try:
            with open(self.path+"\\"+self.header_name+"\\"+"logo.jpg",'wb') as f:
                f.write(r.content)
        except IOError:
            print("保存头像失败")
    # 下载所有回答中的图片
        
if __name__ == '__main__':
    # 要爬取的用户id，比如我的是vajiajia
    user_id = 'li-xing-6-47'
    # 你的用户名
    username = ''
    # 你的知乎密码
    password = ''
    # 存储路径
    path = "D:\\zhihu"
    zhihu = zhihu_User(user_id,username,password,path)






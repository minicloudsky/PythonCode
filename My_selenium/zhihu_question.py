#coding: utf-8
# written by 瞻彼淇奥
# win10+pycharm +python3.54
from selenium import webdriver
from selenium.common import exceptions
import time
import re
import os
import requests
import codecs
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}


class zhihu_User():
    def __init__(self,question_id,path,pagenum):
        self.question_id  = question_id
        self.question_url = 'https://www.zhihu.com/question/'+str(self.question_id)+'/answers/created'
        self.path = path
        self.page_num = pagenum
        self.answer = []
        self.image_list = []
        self.driver = webdriver.Chrome()
        self.title = ""
        self.get_title()
        self.all_question_url = self.generate_url()
        print("%s 一共有 %s 页网页 " %(self.title,self.page_num))
        self.get_answer()
        self.driver.quit()
        self.write_answer()
        print(self.question_id)
        self.download_image()

    def get_title(self):
        self.driver.get(self.question_url)
        title = ""
        try:
            title = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div[1]/div[2]/div[1]/div[1]/h1').text
        except Exception:
            title = "question"
        illegal_file_path = ['\\', '/', ':', '*', '?', '\"', '<', '>', '|']
        temp = ""
        for i in title:
            if i in illegal_file_path:
                continue
            temp += i
        self.title = temp
        print(title)
        if not os.path.exists(self.path+"\\"+self.title[:-1]):
            os.mkdir(self.path+"\\"+self.title[:-1])
        # try:
        #     self.driver.get('https://www.zhihu.com/question/{}/answers/created'.format(self.question_id))
        #     time.sleep(2)
        #     raw_page = self.driver.find_element_by_xpath('//*[@id="QuestionAnswers-answers"]/div/div/div[1]/h4/span/text()[1]').text
        #     self.page_num = int(re.findall(r"\d+",raw_page)[0])/20+1
        #     print("一共 {} 页".format(self.page_num))
        # except exceptions.NoSuchElementException:
        #     pass
        #     self.page_num = 16
        print(self.page_num)
    # 生成每个回答的 xpath

    def generate_xpath(self):
        list = []
        for i in range(1,21):
            list.append('//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div['+str(i)+']/div/div[2]/div[1]')
        return list

    def generate_url(self):
        list = []
        for i in range(1,self.page_num+1):
            list.append("https://www.zhihu.com/question/"+str(self.question_id)+'/answers/created?page='+str(i))
        print(" 生成每一页链接成功 ")
        return list

    def get_answer(self):
        page = 0
        answers = self.all_question_url
        xpaths = self.generate_xpath()
        img_regex = 'data-original="(.+?)"'
        img_regex = re.compile(img_regex)
        for answer in answers:
            self.driver.get(answer)
            time.sleep(4)
            image = re.findall(img_regex,self.driver.page_source)
            for i in image:
                self.image_list.append(i)
            for xpath in xpaths:
                try:
                    tmp_answer = self.driver.find_element_by_xpath(xpath).text
                    self.answer.append(tmp_answer)
                except :
                    pass
            page+=1
        print(" 获取页面成功")
        self.image_list = set(self.image_list)
        print(" 一共有 %s 张 图片 " %(len(self.image_list)))
        self.driver.close()

    def write_answer(self):
        if not os.path.exists(self.path+"\\"+self.title[:-1]+"\\"):
            os.mkdir(self.path+"\\"+self.title[:-1]+"\\")
        string  = ""+self.title+"\r\n"
        paths = self.path + "\\" + self.title[:-1] + ""
        for i in self.answer:
            string += i
            string += "\r\n"
        try:
            with codecs.open(paths + "\\answer.txt",'w',encoding='utf-8') as f:
                f.write(string)
                f.close()
            print(" 答案写入文件成功 ")
        except IOError:
            print(" 写入文件失败 ")
        img_url = ""
        for img in self.image_list:
            img_url += img
            img_url += "\r\n"
        try:
            with codecs.open(paths + "\\img_url.txt",'w',encoding='utf-8') as f:
                f.write(img_url)
                f.close()
            print(" 图片链接写入文件成功 ")
        except IOError:
            print(" 写入文件失败 ")

    def download_image(self):
        list = self.image_list
        for i in list:
            if i[:4]!='http':
                self.image_list.remove(i)

        if not os.path.exists(self.path+"\\"+self.title[:-1]+"\\"+"data-original"):
            os.mkdir(self.path+"\\"+self.title[:-1]+"\\"+"data-original")
        count = 1
        print("download image {}".format(self.question_id))
        for i in self.image_list:
            img = i[-4:]
            if img == 'jpeg':
                img = ".jpeg"
            try:
                r = requests.get(i, headers=header, timeout=4)
                # print(" 正在下载第 %s 张图片 " % (count))
                with codecs.open(self.path+"\\"+self.title[:-1]+"\\"+"data-original"+"\\"+str(count)+img,'wb') as f:
                    f.write(r.content)
                count += 1
            except :
                pass
        print("finish image")


def download(id,path,pagenum):
    question_id = id
    path = path
    zhihu = zhihu_User(question_id, path,pagenum)


if __name__ == '__main__':
    # file save path
    path = "D:\\zhihu"
    # queue = ['22052038','27006591']
    #download('22052038', path,116 )
    #download('276648130',path,658)
    download('301141036',path,32)
    download('277065947',path,180)
    download('276648130',path,658)
    download('23684594',path,535)
    download('39930303',path,260)
    download('301141036',path,33)
# coding: utf-8
import requests
import re
import os
import codecs
from lxml import etree
header = {'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
class DoubanMovie:
    def __init__(self,movie_id,movie_page,comments_path):
        self.movie_id = movie_id
        self.movie_index = 'https://movie.douban.com/subject/'+str(self.movie_id)
        self.all_comments = []
        self.movie_page = movie_page
        self.path = comments_path
        self.movie_name = ""
        self.movie_degree = 0
        self.watched = 0
        self.want_watch = 0
        self.evaluate_person = 0
        self.nation = ""
        self.director = ""
        self.play_time = ""
        self.movie_type = ""
        self.short_comment_person_num = 0
        self.movie_time = 0
        self.better_than =""
        self.response = requests.get(self.movie_index,headers = header,timeout=50)
        self.content = self.response.content.decode('utf-8')
        self.get_movie_name()
        self.get_movie_degree()
        self.get_want_watch()
        self.get_watched_num()
        self.get_short_comment_person_num()
        self.get_movie_type()
        self.get_play_time()
        self.get_movie_time()
        self.get_director()
        # self.get_movie_nation()
        self.get_evaluate_person()
        self.comments()
    #获取短评论人数
    def get_short_comment_person_num(self):
        xpath = '//*[@id="comments-section"]/div[1]/h2/span/a/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.short_comment_person_num = content[0]
        self.all_comments.append(self.movie_name + "的短评人数:" + str(self.short_comment_person_num) + "\n")
        print(self.movie_name + "短评数:" + str(self.short_comment_person_num))
    def get_movie_type(self):
        xpath = '//*[@id="info"]/span[5]/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.movie_type = content[0]
        self.all_comments.append(self.movie_name + "电影类型:" + str(self.movie_type) + "\n")
        print(self.movie_name + "电影类型:" + str(self.movie_type))
    def get_play_time(self):
        xpath = '//*[@id="content"]/h1/span[2]/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.play_time = content[0]
        self.all_comments.append(self.play_time + "的开播时间:" + str(self.play_time) + "\n")
        print(self.movie_name + "开播时间:" + str(self.play_time))
    def get_director(self):
        xpath = '//*[@id="info"]/span[1]/span[2]/a/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.director = content[0]
        self.all_comments.append(self.movie_name + "的导演:" + str(self.director) + "\n")
        print(self.movie_name + "导演:" + str(self.director))
    """
    def get_movie_nation(self):
        xpath = '//*[@id="info"]/br[5]/text()'
        req = requests.get(self.movie_index, headers=header)
        selector = etree.HTML(req.text)
        content = selector.xpath(xpath)
        print(content)
        # if content[0]!='':
        #     self.nation = content[0]
        # self.all_comments.append(self.movie_name + "的国家为:" + str(self.nation) + "\n")
        # print(self.movie_name + "国籍为:" + str(self.nation))
    """
    #获取评价人数
    def get_evaluate_person(self):
        xpath = '//*[@id="content"]/div[2]/div[1]/section/header/h2/span/a/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.evaluate_person = content[0]
        self.all_comments.append(self.movie_name + "的豆瓣影评人数:" + str(self.evaluate_person) + "\n")
        print(self.movie_name + "影评人数:" + str(self.evaluate_person))
    #获取看过的人数
    def get_watched_num(self):
        xpath = '//*[@id="subject-others-interests"]/div/a[1]/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.watched = content[0]
        self.all_comments.append(self.movie_name  + str(self.watched)+"\n")
        print(self.movie_name + str(self.watched))
    #获取想看人数
    def get_want_watch(self):
        xpath = '//*[@id="subject-others-interests"]/div/a[2]/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.want_watch = content[0]
        self.all_comments.append(self.movie_name  + str(self.want_watch)+"\n")
        print(self.movie_name  + str(self.want_watch))
    #获取电影名
    def get_movie_name(self):
        xpath = '//*[@id="content"]/h1/span[1]/text()'
        selector  = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.all_comments.append(content[0]+"\n")
        self.movie_name = content[0]+" "
        print(self.movie_name)
    #获取该电影豆瓣评分
    def get_movie_degree(self):
        xpath = '//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.movie_degree = content[0]
        self.all_comments.append(self.movie_name+"的豆瓣评分:"+str(self.movie_degree)+"\n")
        print(self.movie_name+"的豆瓣评分:"+str(self.movie_degree))
        x = []
        count =5
        for i in range(1,6):
            x.append('//*[@id="interest_sectl"]/div[1]/div[3]/div['+str(i)+']/span[2]/text()')
        for i in x:
            selector = etree.HTML(self.content)
            content = selector.xpath(i)
            counts = content[0]
            list = ['很差','较差','还行','推荐','力荐']
            self.all_comments.append(self.movie_name+" "+str(count+1)+"星评价("+list[count-1]+"):" +str(counts)+"\n")
            count = count-1
            print(str(self.movie_name+" "+str(count+1)+"星评价("+list[count-1]+"):" +str(counts)))
    def get_movie_time(self):
        xpath = '//*[@id="info"]/span[11]/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.all_comments.append(content[0] + "\n")
        self.movie_time = content[0] + " "
        print(self.movie_name+" 片长: "+content[0])
    def get_better_than(self):
        xpath = '//*[@id="interest_sectl"]/div[2]/a/text()'
        selector = etree.HTML(self.content)
        content = selector.xpath(xpath)
        self.all_comments.append(content[0] + "\n")
        self.better_than = content[0] + " "
        print(self.movie_name + " 好于 " + content[0])
    #获取所有评论
    def comments(self):
        page_url = self.getPageUrl()
        count =1
        for page in page_url:
            self.get_page_comments(page)
            print("正在获取第 %s 页的评论" %count)
            count = count+20
        print("获取评论成功，正在写入文件")
        print(self.all_comments)
        self.all_comments = set(self.all_comments)
        self.write_comments()
    # 生成该电影每一页的url
    def getPageUrl(self):
        list = []
        for i in range(1,self.movie_page+1,20):
            list.append("https://movie.douban.com/subject/"+str(self.movie_id)+"/comments?start="+str(i)+"&limit=20&sort=new_score&status=P")
        return list
    # 生成xpath，得到每一页的评论
    def getXpath(self):
        list = []
        for i in range(1,21):
            list.append('//*[@id="comments"]/div['+str(i)+']/div[2]/p/text()')
        return list
    # 获取每一页的评论
    def get_page_comments(self,url):
        xpath = self.getXpath()
        try:
            response = requests.get(url,headers = header,timeout=40)
        except:
            pass
        text = response.content.decode('utf-8')
        for xpaths in xpath:
            selector = etree.HTML(text)
            content = selector.xpath(xpaths)
            for con in content:
                self.all_comments.append(con)
    def write_comments(self):
        f = codecs.open(self.path + "douban_comments.txt", 'r+', 'utf-8')
        f.write("")
        f.close()
        comment = ""
        for i in self.all_comments:
            comment = comment+i
        try:
            f = codecs.open(self.path+"douban_comments.txt",'a+','utf-8')
            for li in self.all_comments:
                f.write(li)
                f.flush()
            f.close()
            print("write done")
        except:
            print("写入评论失败")
            raise IOError

if __name__ == '__main__':
    movie_id = "26425068"
    movie_page = 20000
    comments_path = "D:\\"
    douban = DoubanMovie(movie_id,movie_page,comments_path)
    #'//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()'
    #'//*[@id="comments"]/div[1]/div[2]/p/text()'
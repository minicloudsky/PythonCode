# coding: utf-8
import requests
import re
from urllib.parse import quote
import os
import codecs
from pandas import DataFrame
from lxml import etree
header = {'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


class DoubanMovie:
    def __init__(self, movie_id , comments_path):
        self.movie_id = movie_id
        self.movie_index = 'https://movie.douban.com/subject/'+str(self.movie_id)
        self.all_comments = []
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
        self.short_comment_data = {}
        self.short_comment = []
        # 觉得短评有用的投票数量
        self.votes = []
        self.long_comments = []
        self.short_comment_num = 0
        self.long_comments_num = 0
        self.long_comments_id = []
        self.long_img_url = []
        # 长评论支持和反对的人数
        self.long_approve = []
        self.long_against = []
        self.movie_time = 0
        self.better_than =""
        self.response = requests.get(self.movie_index,headers = header,timeout=50)
        self.content = self.response.content.decode('utf-8')
        self.get_movie_name()
        self.get_movie_degree()
        self.get_want_watch()
        self.get_watched_num()
        self.get_movie_type()
        self.get_play_time()
        self.get_movie_time()
        self.get_director()
        self.get_short_comment_person_num()
        self.get_long_comments_num()
        self.get_short_comments()
        self.get_long_comments()
        self.save_data()

    #获取短评论人数
    def get_short_comment_person_num(self):
        r = requests.get('https://movie.douban.com/subject/{}/comments?status=P'.format(self.movie_id),
                         headers = header,timeout = 50)
        selector = etree.HTML(r.text)
        content = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/ul/li[1]/span/text()')[0]
        data = re.split('\(',content)[1]
        data = re.split('\)',content)[0]
        data = re.split('\(',data)[1]
        self.short_comment_num = int(data)
        print("短评论数量为:{}".format(self.short_comment_num))
    # 获取长评论数
    def get_long_comments_num(self):
        r = requests.get('https://movie.douban.com/subject/{}/reviews'.format(self.movie_id),headers = header,timeout = 50)
        selector = etree.HTML(r.text)
        content = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[5]/text()')[0]
        data = re.findall('(共(.+?)条)',content)
        self.long_comments_num = int(data[0][1])
        print("长评论数量为: {}".format(self.long_comments_num))
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

    # 获取该电影豆瓣评分
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

    def get_short_comments(self):
        print("获取短评论")
        url = []
        for i in range(0,self.short_comment_num+20,20):
            url.append('https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(self.movie_id,i))
        xpath =['//*[@id="comments"]/div[{}]/div[2]/p/span/text()'.format(i) for i in range(1,21)]
        votes_xpath = []
        for i in range(1, 21):
            votes_xpath.append("""//*[@id="comments"]/div[{}]/div[2]/h3/span[1]/span/text()""".format(i))
        for u in url:
            r = requests.get(u,headers = header,timeout = 50)
            for x in xpath:
                selector = etree.HTML(r.text)
                try:
                    self.short_comment.append(selector.xpath(x)[0])
                except IndexError:
                    print("short comments xpath Error")
                    pass
            for votes in votes_xpath:
                selector = etree.HTML(r.text)
                try:
                    self.votes.append(selector.xpath(votes)[0])
                except IndexError:
                    print("shorts comments xpath Error")
                    pass
            print(u+"页获取完成")

    def get_long_comments(self):
        print("获取长评论")
        r = requests.get('https://movie.douban.com/subject/{}/reviews'.format(self.movie_id),headers = header,timeout = 50)
        selector = etree.HTML(r.text)
        total = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/span[5]/text()')
        data = re.findall('(共(.+?)条)',total[0])[0][1]
        self.long_comments_num = int(data)
        long_comments_url = []
        for i in range(0,self.long_comments_num+20,20):
            long_comments_url.append('https://movie.douban.com/subject/{}/reviews?start={}'.format(self.movie_id, i))
        for url in long_comments_url:
            r = requests.get(url, headers=header, timeout=50)
            data = re.findall(re.compile(r'href="https://movie.douban.com/review/(.+?)/"'),r.text)
            for i in data:
                if i not in self.long_comments_id and i!='best':
                    self.long_comments_id.append(i)
            # print(self.long_comments_id)
        for i in self.long_comments_id:
            r = requests.get('https://movie.douban.com/review/{}/'.format(i), headers=header, timeout=50)
            content = re.findall(re.compile('<p>(.+?)</p>'), r.text)
            s = ' '.join(content)
            s = re.sub('<.+?>','',s)
            s = re.sub('</.+?>','',s)
            self.long_comments.append(s)
            img = re.findall(re.compile('<img src="(.+?).jpg"'), r.text)
            image = [i + ".jpg" for i in img]
            self.long_img_url = [i for i in image]
        print("长评论获取完成")

    def save_data(self):
        if not os.path.exists(self.path+"\\{}".format(self.movie_name)):
            os.mkdir(self.path+"\\{}".format(self.movie_name))
            os.mkdir(self.path+"\\{}".format(self.movie_name)+"\\img")
        str = ''
        for i in self.short_comment:
            str += i
        with open(self.path+"\\{}".format(self.movie_name) + "\\short_comments.txt", 'w', encoding='utf-8') as f:
            f.write(str)
        f.close()
        s = ' '.join(self.long_comments)
        with open(self.path+"\\{}".format(self.movie_name) + "\\long_comments.txt", 'w', encoding='utf-8') as f:
            f.write(s)
        f.close()
        self.short_comment_data = {'short_comments': self.short_comment,'short_comments_votes' : self.votes,'long_comments':self.long_comments}
        frame = DataFrame(self.short_comment_data)
        frame.to_excel(self.path+"\\{}".format(self.movie_name) + '\\' + self.movie_name + '.xls', index=True)
        print("下载长评论文章配图,一共有 {} 张图片".format(len(self.long_img_url)))
        count = 0
        for url in self.long_img_url:
            r = requests.get(url,headers=header,timeout=50)
            with open(self.path+"\\{}".format(self.movie_name)+"\\img\\{}".format(str(count)+".jpg"),'wb') as f:
                f.write(r.content)
            count+=1

if __name__ == '__main__':
    # url = 'https://movie.douban.com/subject_search?search_text='
    movie_id = "25716096"
    comments_path = "D:"
    douban = DoubanMovie(movie_id, comments_path)


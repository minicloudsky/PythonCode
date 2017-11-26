#coding: utf-8
import requests
import json
import os
import codecs
import time
from urllib.parse import quote
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=rank&page_limit=20&page_start=0'
r = requests.get(url)
data = r.json()
class Douban_Movie():
    def __init__(self,path):
        self.base_url = 'https://movie.douban.com/j/search_subjects?type=tv&tag='
        self.sort = ['recommend','time','rank']
        self.movie_type = ['热门','美剧','英剧','韩剧','日剧','国产剧','港剧','日本动画','综艺', '纪录片']
        self.path = path
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.data = {}
        self.cover = []
        self.url = []
        self.is_new = []
        self.movie_title = []
        self.rate = []
        self.get_json()
    def get_url(self,tag,sort,page_limit,page_start):
        url = 'https://movie.douban.com/j/search_subjects?type=tv&tag='+quote(tag)+'&sort='+quote(sort)+'&page_limit='\
              +str(page_limit)+'&page_start='+str(page_start)
        return url
    def input(self):
        tag = int(input("请输入电影电视剧类型:热门(1)美剧(2)英剧(3)韩剧(4)日剧(5)国产剧(6)港剧(7)日本动画(8)综艺(9)纪录片(10)\n"))
        sort = int(input("请输入排序方式: 按热度排序(1)按时间排序(2)按评价排序(3)\n"))
        tag = self.movie_type[tag-1]
        sort = self.sort[sort-1]
        page_limit = int(input("请输入电视剧数量:\n"))
        page_start = int(input("请输入开始页:\n"))
        url = self.get_url(tag,sort,page_limit,page_start)
        return url
    def get_json(self):
        url = self.input()
        print(url)
        r = requests.get(url,headers = header)
        self.data = r.json()
        with open(self.path+"\\_豆瓣电影.json",'w',encoding='utf-8') as f:
            json.dump(self.data,f,ensure_ascii=False)
        for value in self.data.values():
            for key in value:
                self.cover.append(key['cover'])
                self.url.append(key['url'])
                self.movie_title.append(key['title'])
                self.is_new.append(key['is_new'])
                self.rate.append(key['rate'])
        print("一共有: "+str(len(self.movie_title)))
        self.download_cover()
    def download_cover(self):
        if not os.path.exists(self.path+"\\cover"):
            os.mkdir(self.path+"\\cover")
        count = 0
        for i in self.cover:
            r = requests.get(i,headers = header)
            print("正在下载第 %s 张cover" %(count))
            with codecs.open(self.path+"\\cover\\"+self.movie_title[count]+".jpg",'wb') as f:
                f.write(r.content)
            count+=1

if __name__ == '__main__':
    path = "D:\\douban"
    douban = Douban_Movie(path)



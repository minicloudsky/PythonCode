#coding: utf-8
import requests
import os
import sys
from pandas import DataFrame
from urllib.parse import quote
import pymongo
from pymongo import MongoClient
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
        self.user_type = ''
        self.user_sort = ''
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        self.data_list = {}
        self.title = []
        self.id = []
        self.url = []
        self.rate = []
        self.cover = []
        self.is_new = []
        self.playable = []
        self.json = None
        self.data = {}
        self.get_json()
        self.download_cover()
    def generate_url(self,tag,sort,page_limit,page_start):
        url_list = []
        for i in range(20,page_limit+20,20):
            url = 'https://movie.douban.com/j/search_subjects?type=tv&tag='+ quote(tag) + '&sort=' + quote(
                sort) + '&page_limit=20'+ '&page_start=' + str(i-20)
            url_list.append(url)
        # print(url_list)
        return url_list
    def get_url(self):
        tag = int(input("请输入电影电视剧类型:热门(1)美剧(2)英剧(3)韩剧(4)日剧(5)国产剧(6)港剧(7)日本动画(8)综艺(9)纪录片(10)\n"))
        sort = int(input("请输入排序方式: 按热度排序(1)按时间排序(2)按评价排序(3)\n"))
        tag = self.movie_type[tag-1]
        sort = self.sort[sort-1]
        self.user_type = tag
        self.user_sort = sort
        page_limit = int(input("请输入电视剧数量(电视剧数量应该小于等于500):\n"))
        page_start = int(input("请输入开始页:\n"))
        url = self.generate_url(tag,sort,page_limit,page_start)
        return url
    def get_json(self):
        urls = self.get_url()
        count = 0
        for url in urls:
            try:
                print("capturing %s page" %(count))
                count+=1
                r  =requests.get(url,headers = header,timeout = 50)
            except:
                pass
            data = r.json()
            self.json = r.json()
            try:
                douban = MongoClient('localhost', 27017)
                douban_db = douban['HelloWorld']
                # 连接douban_movie这个表，如果不存在则自动创建
                douban_set = douban_db.uk_tv
                douban_set.insert(self.json)
                douban_set.save(self.json)
                print("成功存入数据库")
            except EnvironmentError:
                print("存入数据库失败")
                pass
            dict = data.values()
            list = []
            for i in dict:
                for j in i:
                    list.append(j)
            for i in list:
                self.title.append(i['title'])
                self.url.append(i['url'])
                self.playable.append(i['playable'])
                self.rate.append(i['rate'])
                self.cover.append(i['cover'])
                self.id.append(i['id'])
                self.is_new.append(i['is_new'])
        print("已经获取完所有你选择的豆瓣电影数据,正在写入csv文件")
        self.data = {'title':self.title,'id': self.id,'rate':self.rate,'cover':self.cover,
                     'url':self.url,'is_new':self.is_new,'playable':self.playable}
        frame = DataFrame(self.data)
        frame.to_csv(self.path + '\\' + self.user_type + self.user_sort + '.csv',index=True)

    def download_cover(self):
        choice = int(input("你要下载刚才获取的电影封面图吗?(1 : 下载，0 : 不用下载)\n"))
        if choice ==0:
            sys.exit()
        if not  os.path.exists(self.path+"\\"+self.user_type+"_" + self.user_sort+"_"+"cover"):
            os.mkdir(self.path+"\\"+self.user_type+"_" + self.user_sort+"_"+"cover")
        count =0
        for i in self.cover:
            try:
                print("downloading %s " %(count))
                r = requests.get(i,headers = header,timeout = 50)
                with open(self.path+"\\"+self.user_type+"_" + self.user_sort+"_"+"cover"+"\\"+str(count)+i[-4:],'wb') as f:
                    f.write(r.content)
                count+=1
            except:
                print("download error")
                pass

if __name__ == '__main__':
    path = "D:\\"
    print("豆瓣电影数据默认保存在D:盘哦")
    douban = Douban_Movie(path)



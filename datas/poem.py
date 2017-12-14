#coding: utf-8
import requests
import os
import json
import time
from pymongo import MongoClient
from lxml import etree
import random
from pandas import DataFrame
from bs4 import BeautifulSoup
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

def title_xp():
    xpath = []
    for i in range(2,22,2):
        xpath.append("/html/body/div[2]/div[1]/div[{}]/div[1]/p[1]/a/b/text()".format(i))
    return xpath
def dynasty_xp():
    xpath = []
    for i in range(2,22,2):
        xpath.append('/html/body/div[2]/div[1]/div[{}]/div[1]/p[2]/a[1]/text()'.format(i))
    return xpath
def author_xp():
    xpath = []
    for i in range(2,22,2):
        xpath.append('/html/body/div[2]/div[1]/div[{}]/div[1]/p[2]/a[2]/text()'.format(i))
    return xpath
def starts(start):
    titles = title_xp()
    dynastys = dynasty_xp()
    authors = author_xp()
    title_data = []
    dynasty_data = []
    author_data = []
    content_data = []
    tag_data = []
    url = []
    count = 1
    for i in range(start,start+100):
        url.append("http://www.gushiwen.org/default_{}.aspx".format(i))
    for i in url:
        try:
            r = requests.get(i,headers = ua,timeout = 50)
        except:
            pass
        for title in titles:
            selector = etree.HTML(r.text)
            content = selector.xpath(title)
            title_data.append(content[0])
        for dynasty in dynastys:
            selector = etree.HTML(r.text)
            content = selector.xpath(dynasty)
            dynasty_data.append(content[0])
        for author in authors:
            selector = etree.HTML(r.text)
            content = selector.xpath(author)
            author_data.append(content[0])
        soup = BeautifulSoup(r.text,'lxml')
        contents = soup.find_all("div","contson")
        for content in contents:
            content_data.append(content.text.strip())
        tags = soup.find_all("div","tag")
        for tag in tags:
            tag_data.append(tag.text.strip())
        print(i)
    dumpdata(title_data,dynasty_data,author_data,content_data,tag_data,start)

def dumpdata(title,dynasty,author,content,tag,start):
    dict = {}
    dict['title'] = title
    dict['dynasty'] =dynasty
    dict['author'] = author
    dict['content'] = content
    dict['tag'] = tag
    client = MongoClient('localhost',27017)
    poem_db = client["poetry"]
    poem_set = poem_db.poems
    poem_set.insert(dict)
    poem_set.save(dict)
    print("成功存入MongoDB")
    data = {'title':title,'dynasty':dynasty,'author':author,'content':content,'tag':tag}
    frame = DataFrame(data)
    frame.to_excel(path+"\\"+"poem"+str(start)+"_"+str(start+200)+".xls",index=True)
    dynasty = dynasty.clear()
    dynasty = []
    tag = tag.clear()
    tag = []
    content = content.clear()
    content = []
    author =author.clear()
    author = []
    title = title.clear()
    title = []
    data = data.clear()
    dict = []
    print(str(start)+"finished")
if __name__ == '__main__':
    path ="D:\\poetry"
    page = 500000
    for i in range(46500,page,100):
    	starts(i)



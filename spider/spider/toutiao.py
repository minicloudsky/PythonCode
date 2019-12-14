#coding: utf-8
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests
import json
import re
import os
from bs4 import BeautifulSoup
#获取头条街拍首页
def get_page_index(offset,keyword):
    data = {
        'offset': 40,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
    }
    url = 'http://www.toutiao.com/search_content/?' +urlencode(data)
    print(url)
    try:
        response = requests.get(url)
        # print(response.status_code)
        if(response.status_code==200):
            return response.text
        return None
    except RequestException:
        print("Error")
        return None
def parse_page_index(html):
    data = json.loads(html)
    print("data:")
    print(data)
    if data and 'data'in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
#获取详细页
def get_page_detail(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
    except RequestException:
        print("请求详情页失败",url)
        return None
def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    # print(title)
    images_pattern = re.compile('http:\/\/pb3.pstatp.com\/origin\/(.*?)"',re.S)
    result = re.search(images_pattern,html)
    print("result")
    print(result)
    if result:
        #print(result.group(1))
        try:
            data = json.loads(result.group(1))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                return {
                    'title' : title,
                    'url': url,
                    'images' : images
                }
        except json.JSONDecodeError:
            pass

def get_img(url):
    url_txt = []
    for li in url:
        response = requests.get(li)
        soup = BeautifulSoup(response.text,'lxml')
        title = soup.title
        reg = '<title>(.+?)</title>'
        reg = re.compile(reg)
        title = re.findall(reg,response.text)
        title = title[0]
        print(title)
        if not os.path.exists("D:\\toutiao\\"+title) :
            os.mkdir("D:\\toutiao\\"+title)
        path = "D:\\toutiao\\"+title
        regex = '"url":"(.*?)"'
        image = re.findall(regex,response.text)
        print("image")
        print(image)

def get_article_url(html):
    reg = '"article_url": "(.*?)"'
    reg = re.compile(reg)
    article_url = re.findall(reg,html)
    return article_url

if __name__ == '__main__':
    html = get_page_index(0, '街拍')
    list = get_article_url(html)
    img = get_img(list)
    # for url in parse_page_index(html):
    #     html = get_page_detail(url)
    #     if html:
    #         result = parse_page_detail(html,url)
    #         print(result)
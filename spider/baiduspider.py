# -*- coding: utf-8 -*-
import re
import urllib
import requests
import os
import time
reg = "https://ss1.bdstatic.com/(.+?).jpg"
reg = re.compile(reg)
header = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
          }
path = str(os.getcwd())+"\\picture\\"
if not os.path.exists(path):
    os.mkdir(path)
print("您即将下载的图片将被保存在:"+path+"目录。")
#生成搜索链接
def getKeyUrl(keyword,page):
    url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    req_url = []
    for i in range(0,20*page,20):
        req_url.append(url+urllib.request.quote(keyword)+ "&pn="+str(i)+"&gsm=50&ct=&ic=0&lm=-1&width=0&height=0")        
    return req_url
#获取每一页的图片链接
def getPageUrl(page_url):
	req = requests.get(page_url,headers = header)
	txt = req.text
	url = re.findall(reg,txt)
	urls = []
	for i in url:
		urls.append("https://ss1.bdstatic.com/"+str(i)+".jpg")
	return set(urls)

def download(req_url):
    count = 0
    img_number = 0
    img_url = []
    for i in req_url:
        page_url = getPageUrl(i)
        img_num = len(page_url)
        print("第 %s 页一共有 %s 张图片" %(count,page_num))
        print("正在获取图片链接")
        for url in page_url:
            print("正在获取第 %s 张图片链接" %img_number)
            print(url)
            #downloadPic(url,img_number)
            img_number+=1
            img_url.append(url)
        count +=1
    flag = 0
    total = len(img_url)
    img_url = set(img_url)
    print("一共有 %s 张图片" %total)
    for i in img_url:
        print("正在下载第 %s 张图片" %flag)
        downloadPic(i,flag)
        flag = flag+1

def downloadPic(url,img_number):
    req = requests.get(url,headers = header)
    try:
        req = requests.get(url,headers = header,timeout=20)
        string = path + str(img_number) + '.jpg'
        print("正在下载: "+url)
        fp = open(string,'wb')
        fp.write(req.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print ('当前图片无法下载')
        pass
if __name__ =='__main__':
    start = time.time()
    keyword = str(input("请输入要搜索的百度图片关键字:"))
    page_num = int(input("请输入要下载的图片页数:"))
    req_url = getKeyUrl(keyword,page_num)
    list = getPageUrl(req_url[0])
    download(req_url)
    end = time.time()
    cost = str(end-start)
    print("图片下载结束，一共用了 %s 秒，5秒后程序将自动退出" %cost)
    time.sleep(5)



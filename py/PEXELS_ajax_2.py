#coding:utf-8
import re
import requests
import os
import time
import threading
class pexels():
    def __init__(self,keyword,page_num,path):
        self.keyword  = keyword
        self.page_num = page_num
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }
        self.path = path +"\\pexels_picture\\"+self.keyword
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.js_urls = []
        self.download()
    #控制下载
    def download(self):
        js_url = self.get_js()
        print("%s 的js文件获取成功" %(self.keyword))
        img_url = []
        for i in js_url:
            temp = self.get_img_url_list(i)
            for li in temp:
                img_url.append(li)
        print("%s 类型的图片一共有 %s 张" %(self.keyword,len(img_url)))
        img_url = set(img_url)
        img_number = 1
        count =1
        for li in img_url:
            if(count%2!=0):
                self.downloadPic(li,img_number)
                print("正在下载 %s 的第 %s 张图片" %(self.keyword,img_number))
            img_number +=1
            count+=1
    """获取网站ajax异步加载的JavaScript代码，
    这些代码异步加载从而实现下拉即可加载图片,所以得到了js文件也就得到了
    所有的图片链接"""
    def get_js(self):
        list = []
        for i in range(1,self.page_num+1):
            list.append("https://www.pexels.com/search/"+str(self.keyword)+"/?page="+str(i)+"&seed=2017-09-08+22%3A19%3A08++0000&format=js&seed=2017-09-08%2022:19:08%20+0000")
        return list
    #获取每一页js中的图片链接
    def get_img_url_list(self,js_url):
        regex ='https://images.pexels.com/photos/\d+/pexels-photo-\d+.jpeg?'
        reg = re.compile(regex)
        req = requests.get(js_url,headers = self.header)
        text = req.text
        list = re.findall(reg,text)
        return list
    #下载每一张图片
    def downloadPic(self,url,count):
        print("downloading :"+url)
        try:
            req = requests.get(url,headers = self.header,timeout=100)
            f = open(self.path+"\\"+str(count)+ ".jpg", 'wb')
            f.write(req.content)
            f.close()
        except:
            print("下载失败")
            pass
    #调用每个keyword对应的页面
def download_keyword(key,page,path):
    img = pexels(key,page,path)
#开启多线程，加速下载
def start_thread(key,page,path):
    t = threading.Thread(target=download_keyword,args=(key,page,path))
    t.start()
#从js文件中提取出图片类型的关键词
def get_pexels_pic_type():
    js_type = []
    img_type = []
    for i in range(1,10):
        js_type.append("https://www.pexels.com/popular-searches/?page="+str(i)+"&format=js&seed=298640966")
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
    for i in js_type:
        r = requests.get(i,headers = header)
        text = str(r.text)
        reg = r'img alt=\\"(.+?)\\"'
        reg = re.compile(reg)
        list = re.findall(reg,text)
        for i in list:
            img_type.append(i)
        count = 1
    for i in img_type:
        print(i+" ",end="")
        if count%10==0:
            print()
        count +=1
    print("")
    print("pexels 图片网站一共有以上英文所示的 %s 种类型图片" %(len(img_type)))
    return img_type
if __name__ == '__main__':
    start = time.time()
    print("正在抓取pexels网站的图片分类")
    keyword = get_pexels_pic_type()
    page_num = int(input("请输入要下载的页数:"))
    path = str(os.getcwd())
    print("图片将被保存在 %s" %(path))
    for i in keyword:
        start_thread(i,page_num,path)
    end = time.time()
    print("一共耗费 %s s" %(str(end-start)))

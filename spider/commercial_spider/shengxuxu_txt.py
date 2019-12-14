from lxml.html import etree
import requests
import re
from bs4 import BeautifulSoup
class Darker():
    def __init__(self,book_id):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        self.book_id = book_id
        self.pagenum = 1
        self.page_url = []
        self.book = ""
        self.book_name = ""
        self.author = ''
        self.update_time = ''
        self.get_info()
        self.getbook()

    def get_info(self):
        r = requests.get("http://www.shengxuxu.com/{}".format(self.book_id),headers= self.header,timeout = 50)
        self.book_name = re.findall(re.compile("<h1>(.+?)</h1>"),r.text)[0]
        selector = etree.HTML(r.text)
        self.author = selector.xpath('/html/body/section/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/a/text()')[0]
        regex = re.compile("""<li>最新：<a href="/.+?/read_(.+?).html" """)
        self.pagenum = int(re.findall(regex,r.text)[0])
        self.page_url = ["http://www.shengxuxu.com/{}/read_{}.html".format(self.book_id,i) for i in range(1,self.pagenum+1)]
        selector = etree.HTML(r.text)
        self.update_time = selector.xpath('/html/body/section/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[7]/text()')[0]
        print("{}{}".format(self.book_name,self.update_time))

    def getbook(self):
        for url in self.page_url:
            r = requests.get(url,headers = self.header,timeout = 50)
            selector = etree.HTML(r.text)
            content = selector.xpath('//*[@id="chaptercontent"]/text()')
            str = ""
            for i in content:
                str+=i
            str = str.replace('.LA，最快更新死亡通知单：暗黑者最新章节！','')
            self.book = self.book + str
            print("正在获取{}".format(url))
        with open("{}_{}_{}.txt".format(self.book_name,self.author,self.update_time),'w') as f:
            f.write(self.book)
        print("{}下载完成".format(self.book_name))
if __name__ == '__main__':
    darker = Darker(67742)
    darker.get_info()
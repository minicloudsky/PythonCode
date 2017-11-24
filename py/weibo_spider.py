# coding: utf-8
import requests
import re
import time
from bs4 import BeautifulSoup
from lxml import etree
class WeiboSpider():
    def __init__(self,user_page,header):
        self.user_page = user_page
        self.header = header
        get_user_albumurl()

    def get_user_albumurl(self):
        req = req.get()


if __name__ =='__main__':
    user_page = 'http://weibo.com/u/5710928238?is_all=1'
    header = {
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;',
            'Connection':'keep-alive',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
            'Cookie':'UM_distinctid=15e55d2720c9e4-062dc9bb161658-1781c36-15f900-15e55d2720d440; SINAGLOBAL=5524135812679.519.1504678408903; un=15716302402; wvr=6; UOR=www.baidu.com,vdisk.weibo.com,baike.baidu.com; _s_tentry=photo.weibo.com; Apache=6850031578667.351.1504924196028; ULV=1504924196077:7:7:7:6850031578667.351.1504924196028:1504921743398; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; SSOLoginState=1504924199; SCF=Agn6gFdTJwv1EBLs4PKhpKMcAJhMB6w_jwJPmWsfO7hpZ6YuMjaOG4zb6s6Nt6YaES81uM3751UES6Y-x_YpyYM.; SUB=_2A250tyJ3DeRhGeNJ6lIY8ibOyDSIHXVXxRS_rDV8PUJbmtAKLXbTkW-SGsnxYjRyY2pf5jTF3Rd1RxHP9g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI_MoT_RiN9oSa8YM-JLfj5JpX5o2p5NHD95QfS0271KzReoeRWs4Dqcj7i--4iK.4iKyhi--Xi-zRiKyWi--RiKy2iKn4i--Ni-2ci-iFi--Ni-2ci-iFIsyQ; SUHB=02MvJyMH7J0bON; ALF=1536460198; TC-Page-G0=1bbd8b9d418fd852a6ba73de929b3d0c; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=b2423472d8aef313d052f5591c93cb75; wb_cusLike_5710928238=N'}
    r = requests.get(user_page,headers = header)
    #reg = "href="/p/(.*?)/photos?from=page_(.+?)""
    #reg = re.compile(reg)
    #album_url = re.findall(reg,r.text)
    soup = BeautifulSoup(r.text,'lxml')
    print(soup.title)
    print(soup.head)
    print(r.status_code)
    print()
    
    
   
					

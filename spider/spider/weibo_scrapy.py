# -*- coding: utf-8 -*-
#author:wanghuan  https://github.com/RobortHuan/python-web-spider
#thanks 语亮 http://www.jianshu.com/p/7c5a4d7545ca
import re
import string
import os
import importlib,sys
import urllib
import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
importlib.reload(sys)
#sys.setdefautencoding('utf-8')
if(len(sys.argv)>=2):
    user_id=(int)(sys.argv[1])
else:
    user_id=(int)(input(u"请输入用户id"))
cookie={ 'Cookie':'UM_distinctid=15e55d2720c9e4-062dc9bb161658-1781c36-15f900-15e55d2720d440; SINAGLOBAL=5524135812679.519.1504678408903; un=15716302402; wvr=6; UOR=www.baidu.com,vdisk.weibo.com,baike.baidu.com; _s_tentry=photo.weibo.com; Apache=6850031578667.351.1504924196028; ULV=1504924196077:7:7:7:6850031578667.351.1504924196028:1504921743398; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; SSOLoginState=1504924199; SCF=Agn6gFdTJwv1EBLs4PKhpKMcAJhMB6w_jwJPmWsfO7hpZ6YuMjaOG4zb6s6Nt6YaES81uM3751UES6Y-x_YpyYM.; SUB=_2A250tyJ3DeRhGeNJ6lIY8ibOyDSIHXVXxRS_rDV8PUJbmtAKLXbTkW-SGsnxYjRyY2pf5jTF3Rd1RxHP9g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI_MoT_RiN9oSa8YM-JLfj5JpX5o2p5NHD95QfS0271KzReoeRWs4Dqcj7i--4iK.4iKyhi--Xi-zRiKyWi--RiKy2iKn4i--Ni-2ci-iFi--Ni-2ci-iFIsyQ; SUHB=02MvJyMH7J0bON; ALF=1536460198; TC-Page-G0=1bbd8b9d418fd852a6ba73de929b3d0c; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; YF-V5-G0=b2423472d8aef313d052f5591c93cb75; wb_cusLike_5710928238=N'}
url='http://weibo.cn/u/%d?filter=1&page=1'%user_id
html = requests.get(url, cookies = cookie).content   #content返回str类型
selector = etree.HTML(html)
pageNum=(int)(selector.xpath(u'//input[@name="mp"]')[0].attrib['value'])
print(pageNum)
result=""
urllist_set=set()
word_count=1
image_count=1
print(u'爬虫准备就绪...')
for page in range(1,pageNum+1):
    url='http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page)
    lxml=requests.get(url,cookies=cookie).content
    selector=etree.HTML(lxml)
    content=selector.xpath('//span[@class="ctt"]')
    for each in content:
        text=each.xpath('string(.)')
        if word_count>=4:
            text="%d:"%(word_count-3)+text+"\n\n"
        else:
            text=text+"\n\n"
        result=result+text
        word_count+=1
    soup=BeautifulSoup(lxml,"lxml")
    urllist=soup.find_all('a',href=re.compile(r'^http://weibo.cn/mblog/oripic',re.I))
    first=0
    for imgurl in urllist:
        urllist_set.add(requests.get(imgurl['href'],cookies=cookie).url)
        image_count+=1
fo=open(u"/Users/wanghuan/AppData/Local/Programs/Python/Python35/爬虫/%s"%user_id,"w" ,encoding='utf-8', errors='ignore')
fo.write(result)
word_path=os.getcwd()+'%d'%user_id
print(u"文字微博爬取完毕")
fo.close()
link=""
if not  os.path.exists("D:\\spider"):
    os.mkdir("D:\\spider")
fo2=open("D:\\spider\\%s_imageurls"%user_id,"w")
for eachlink in urllist_set:
    link=link+eachlink+"\n"
fo2.write(link)
print(u'图片链接爬取完毕')
fo2.close()
if not urllist_set:
    print(u'图片不存在')
else:
    image_path=os.getcwd()+'\weibopicture'
    if os.path.exists(image_path) is False:
        os.mkdir(image_path)
    x=1
    for imgurl in urllist_set:
        temp=image_path+'/%s.jpg'%x
        print(u'正在下载第%s张图片'%x)
        try:
            urllib.request.urlretrieve(urllib.request.urlopen(imgurl).geturl(),temp)
        except:
            print(u'图片下载失败：%s'%imgurl)
        x+=1
print(u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path))
print(u'原创微博图片爬取完毕，共%d张，保存路径%s'%(image_count-1,image_path))
import requests
import urllib2
from lxml import etree
import os
import time
import re
from multiprocessing.dummy import  Pool


def tosave(texta):
    f = open('weibo.txt', 'a')
    f.write(texta + '\n')
    f.close()


def getHtml(url, cook):
    html = requests.get(url, cookies=cook).content
    selector = etree.HTML(html)
    return selector


def getContent(htm, xpathStr):
    selector = htm
    content = selector.xpath(xpathStr)  
    return content


# download images of each group
def getDownImg(cons, page,x):
    fn = '%s' % page + '__%s' % x
    pa = os.path.dirname(__file__) + '/' + username
    # check and create folder
    if not os.path.exists(pa):
        os.mkdir(pa)
    fl = pa + '/%s.jpg' % fn

    r = requests.get(cons)
    with open(fl, "wb") as code:
        code.write(r.content)

# download homepage images
def getDownImgHomepage(cons, page):
    x = 0
    for each in cons:
        print each
        fn = '%s' % page + '%s' % x +'000'
        pa = os.path.dirname(__file__) + '/' + username
        # check and create folder
        if not os.path.exists(pa):
            os.mkdir(pa)
        fl = pa + '/%s.jpg' % fn
        url = each.replace('wap180', 'large')
        r = requests.get(url)
        with open(fl, "wb") as code:
            code.write(r.content)
        x += 1


cook = {"Cookie": "xxxxx"} #insert your cookies
username = '' #'insert the username' 
url0 = 'http://weibo.cn/u/' + username
print url0
# xpath of each page
xp1 = '//*[@class="ib"]/@src'  # homepage
xp2 = '//*[@class="c"]//div[1]//@href'  # homepage
xp3 = '//*[@class="c"]//a[2]//@href'  # group picture page
xp4 = '/html/body/img//@src'  # origin picture page

# get N pages' images
for page in range(1, 50):
    # page = 1
    url = url0 + '?page=' + '%s' % page
    print url
    htm0 = getHtml(url, cook)
    cons1 = getContent(htm0, xp1)  # images' href on homepage
    getDownImgHomepage(cons1, page) #download homepages imgs
    cons2 = getContent(htm0, xp2)  # group images' url on homepage
    x = 0
    for cons in cons2:
        if 'picAll' in cons:
            htm1 = getHtml(cons, cook)  # open group images' page
            cons3 = getContent(htm1, xp3)  # get group pictures original pages
            for piccons in cons3:
            	list = piccons.split('=')
                list2 = list[2].split('&')
                pidID = list2[0]
                picurl = 'http://ww1.sinaimg.cn/large/' + pidID + '.jpg'
                print picurl
                getDownImg(picurl, page, x)
                x += 1
        time.sleep(0.01)
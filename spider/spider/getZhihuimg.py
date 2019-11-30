# -*- coding: utf-8 -*-
import urllib
import re
import requests
import urllib2
#获取图片链接
def getImgUrl(url,regex):
    request = urllib.urlopen(url)
    html = request.read()
    reg = re.compile(regex)
    url = re.findall(reg,html)
    img_add = []
    for li in url:
        if len(li) ==60:
            img_add.append(li+".jpg")
    return img_add
# 下载图片
def downloadImg(url):
    count =0
    for li in url:
        count = count+1
        print "正在下载第 %s 张图片 " %(count)
        urllib.urlretrieve(li,'E:\\img\\%s.jpg' %(count))
if __name__ =='__main__':
    url = "https://www.zhihu.com/question/43551423"
    regex = r'data-actualsrc="(.+?).jpg"'
    img_url = getImgUrl(url,regex)
    downloadImg(img_url)
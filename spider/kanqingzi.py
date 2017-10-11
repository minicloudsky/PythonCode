# coding: utf-8
import requests
import re
import codecs
from lxml import etree
#url = "https://weibo.com/p/1003061526449335/follow?relate=fans&from=100306&wvr=6&mod=headfans&current=fans#place"
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

def getUrl():
    url = []
    for i in range(1,298553):
        url.append('https://weibo.com/p/1003061526449335/follow?relate=fans&page='+str(i)+'#Pl_Official_HisRelation__60')
        return url
def getXpath():
    xpath = []
    for i in range(1,22):
        xpath.append('//*[@id="Pl_Official_HisRelation__60"]/div/div/div/div[2]/div[1]/ul/li['+str(i)+"]/dl/dt/a/img/text()")
    return xpath
if __name__ == '__main__':
    url = "https://weibo.com/p/1003061526449335/follow?relate=fans&page=2#Pl_Official_HisRelation__60"
    r = requests.get(url,headers = header)
    print(r.text.encode('gb2312'))





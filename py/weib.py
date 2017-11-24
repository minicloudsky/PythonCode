# coding: utf-8
import re
import urllib
import requests
from bs4 import BeautifulSoup
url = "http://weibo.com/kanqingzi1368?refer_flag=1001030101_&is_all=1"

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
          'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Cookie':'UM_distinctid=15e55d2720c9e4-062dc9bb161658-1781c36-15f900-15e55d2720d440; SINAGLOBAL=5524135812679.519.1504678408903; UOR=www.baidu.com,vdisk.weibo.com,www.baidu.com; un=15716302402; wvr=6; SSOLoginState=1504864871; SCF=Agn6gFdTJwv1EBLs4PKhpKMcAJhMB6w_jwJPmWsfO7hpzh9sBx0OrzI2pqi0RXh4LbflGRq3SUKEr_s5iuWR99E.; SUB=_2A250tho3DeRhGeNJ6lIY8ibOyDSIHXVXwgz_rDV8PUNbmtAKLUb6kW-FEhibuslfrkN0ovnO8OmMPv6ZGg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI_MoT_RiN9oSa8YM-JLfj5JpX5KzhUgL.Fo-NeK54eonEe0n2dJLoI05LxK.L1K.L12eLxKBLBonL122LxKnL12BL1h.LxKMLBKqLB.zLxKMLBKqLB.iQIsnt; SUHB=0S7C7UoY93M2LT; ALF=1536400870; _s_tentry=-; Apache=2297086661336.767.1504864886672; ULV=1504864886701:5:5:5:2297086661336.767.1504864886672:1504861940777'}
req = requests.get(url,headers = header)
reg = "(.+?).jpg"
reg = re.compile(reg)
print(req.status_code)
print(req.apparent_coding)
req.encode = "utf-8"
print(req.text)
list = re.findall(reg,req.text)
print(list)


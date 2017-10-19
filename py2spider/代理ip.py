#coding: utf-8
import BeautifulSoup
import requests
import lxml
import random
import requests
try:
    r = requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://175.170.127.58:1205/"})
    print r.status_code
except:
    print 'connect failed'
else:
    print 'success'

# coding: utf-8
import random
import urllib2
import urllib
url = "http://www.itcast.cn"

ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; ) Apple.... ",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0)... ",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X.... ",
    "Mozilla/5.0 (Macintosh; Intel Mac OS... "
]
# response = urllib2.urlopen("http://www.baidu.com")
# html = response.read()
# print html
# request = urllib2.Request(url)
# response = urllib2.urlopen(request)
# html = response.read()
# print html

# user_agent = random.choice(ua_list)
# request = urllib2.Request(url)
# request.get_header("User-Agent")
# response = urllib2.urlopen(request)
# html = response.read()
# print html
# word = {'wd':"贾亚武"}
# print urllib.urlencode(word)
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
formdata = {
    'start':'0',
    'limit':'10'
}
header = {"User-Agent": "Mozilla...."}
data = urllib.urlencode(formdata)
request = urllib2.Request(url,data,headers=header)
response = urllib2.urlopen(url)
print response.read()
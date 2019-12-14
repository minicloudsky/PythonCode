#coding: utf-8
import urllib
import urllib2
import cookielib

# 1. 构建一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()

# 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

# 3. 通过 build_opener() 来构建opener
opener = urllib2.build_opener(cookie_handler)

# 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

# 5. 需要登录的账户和密码
data = {"email":"mr_mao_hacker@163.com", "password":"alaxxxxxime"}

# 6. 通过urlencode()转码
postdata = urllib.urlencode(data)

# 7. 构建Request请求对象，包含需要发送的用户名和密码
request = urllib2.Request("http://www.renren.com/PLogin.do", data = postdata)

# 8. 通过opener发送这个请求，并获取登录后的Cookie值，
opener.open(request)

# 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = opener.open("http://www.renren.com/410043129/profile")

# 10. 打印响应内容
print response.read()
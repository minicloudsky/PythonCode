#coding: utf-8
import urllib.request
import urllib.error
import socket
import urllib.parse
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# post method
# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data = data)
# print(response.read())
# try:
#     response= urllib.request.urlopen('http://www.httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print("TIME OUT")

# response = urllib.request.urlopen('https://www.python.org')
# # print(type(response))
# # print(response.status)
# print(response.getheaders())
# print(response.getheader('server'))

url = 'http://www.httpbin.org/post'
headers = {
'Host':'httpbin.org',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
}
dict = {
    'name':'Cloudsky'
}
data = bytes(urllib.parse.urlencode(dict),encoding='utf-8')
req = urllib.request.Request(url = url,
        data=data,headers=headers,method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
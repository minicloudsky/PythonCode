from urllib import request,parse

url = 'http://httpbin.org/post'
dict = {
    'name':'LittleCloudsky'
}
data = bytes(parse.urlencode(dict),encoding='utf-8')
req = request.Request(url=url,data=data,method='POST')
req.add_header('User-Agent','Mozilia/4.0(compatible;MSIE 5.5;Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
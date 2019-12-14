import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http':'http://117.87.176.180:9000',
    'http':'http://115.223.194.99:9000'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())
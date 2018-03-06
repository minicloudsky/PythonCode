from urllib.parse import urlparse,urljoin,urlencode

# result = urlparse('http://www.baidu.com/index.html;user=5#comment')
# print(type(result),result)
# result = urlparse('www.baidu.com/index.html;user=5#comment',scheme='https')
# print(result)
# result = urlparse('http://www.baidu.com/index.html;user=5#comment',scheme='https')
# print(result)

# result = urlparse('http://www.baidu.com/index.html;user=5#comment',allow_fragments=False)
# urljoin以后面的链接为基准，后面没有的加上，有的不变
print(urljoin('http://www.baidu.com','aaa.html'))

url = 'https://www.baidu.com'
params = {
    "name":"jia",
    'key':'value'
}
end_url = url +urlencode(params)
print(end_url)

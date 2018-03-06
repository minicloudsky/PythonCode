import requests

# response  = requests.get("http://httpbin.org/get")
# print(response.headers)
# data = {
#     'name':'cloudsky',
#     'age':20,
# }
#
# response = requests.post("http://httpbin.org/post",data=data)
# print(response.json())
# requests.put("http://httpbin.org/put")

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
# response = requests.get("https://github.com/favicon.ico")
# print(type(response.text))
# with open('favicon.ico','wb') as f:
#     f.write(response.content)

response = requests.get('https://www.zhihu.com/explore',headers = headers)
print(response.text)
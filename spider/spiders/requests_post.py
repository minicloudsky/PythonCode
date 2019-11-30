import requests

data = {'name':'cloudsky','age':'22'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url = 'http://httpbin.org/post'

# response = requests.post(url,headers = headers,data=data)
# print(response.json())
# response = requests.get("https://www.jianshu.com")
# exit() if not response.status_code == requests.codes.ok else print('Requests Successfully')
#
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response,headers)
# print(type(response.cookies),response.cookies)
# print(type(response.history),response.history)

# files = {'files':open('favicon.ico','rb')}
# response = requests.post('http://httpbin.org/post',data=files)
# print(response.text)

# # 获取cookies
# response = requests.get('https://wwww.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+' = '+value)

# 会话维持
# requests.get('http://httpbin.org/cookies/set/number/1234567')
# response = requests.get('http://httpbin.org/cookies')
# print(response.text)

# 模拟会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/121434')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)

response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
# 添加证书
response = requests.get('https://www.12306.cn',cert=('/path/server.crt','path/key'))
print(response.status_code)
import requests
from requests.exceptions import ReadTimeout
from requests.auth import HTTPBasicAuth
# proxies = {
#     'http':'https://127.0.0.1:2352',
#     'https':'https://232.34.33.22:66',
# }
# response = requests.get('https:www.taobao.com',proxies=proxies)
# shadowsocks proxies
# pip install 'requests[socks]
# proxies = {
#     'http':'socks5://127.0.0.1:2352',
#     'https':'socks5://232.34.33.22:66',
# }
# response = requests.get('https:www.taobao.com',proxies=proxies)
# 超时设置
# try:
#     response = requests.get('http://www.google.com',timeout=1)
#     print(response.status_code)
# except ReadTimeout:
#     print("Timeout")

# 认证设置
r = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
print(r.status_code)

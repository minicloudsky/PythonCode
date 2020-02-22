import requests

r = requests.get('http://127.0.0.1:5000/login', auth=('magigo', '123456'))
print(r.text)
# token = r.text
# r = requests.get('http://127.0.0.1/test1', params={'token': token})
# print(r.text)

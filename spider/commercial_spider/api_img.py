import os
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
url = []
img_url = []
# url = 'https://gank.io/api/data/%E7%A6%8F%E5%88%A9/9/1'
for i in range(1,110):
    for page in range(1,9):
        url.append('https://gank.io/api/data/%E7%A6%8F%E5%88%A9/'+str(i)+'/'+str(page))
print("url: {}".format(len(url)))
for i in url:
    r = requests.get(i,headers = header)
    data = r.json()
    for url in data["results"]:
        img_url.append(url["url"])
img_url = list(set(img_url))
print("total img {}".format(len(img_url)))
count = 0
if not os.path.exists("D:\\image"):
    os.mkdir("D:\\image")
flag = 'jpg'
for i in img_url:
    if i[-3]=='jpg':
        flag='.jpg'
    else:
        flag='.jpeg'
    try:
        r = requests.get(i,headers = header)
        with open("D:\\image\\"+str(count)+flag,'wb') as f:
            f.write(r.content)
        f.close()
        print("finish {}".format(count))
        count+=1
    except:
        pass
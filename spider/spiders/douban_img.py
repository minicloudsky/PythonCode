import requests
import re
import os
header = {
    'Referer':'https://movie.douban.com/celebrity/1312846/photos/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Upgrade-Insecure-Requests':1,
}

def generate_url(page,user_id):
    list = []
    count = 0
    for i in range(page-30):
        list.append('https://movie.douban.com/celebrity/{}/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(user_id,count))
        count+=30
    return list
def getpage(user_id):
    r = requests.get('https://movie.douban.com/celebrity/{}'.format(user_id),headers = header)
    regex = re.compile(r'target="_self">全部(.+?)张</a>')
    page = re.findall(regex,r.text)
    if len(page)!=0:
        page = int(page[0])
    else:
        page = 5
    print("{} 一共 {} 张图片".format(user_id,page))
    return page
def getimage(page,user_id,path):
    pageurl = generate_url(page,user_id)
    count = 0
    if not os.path.exists(path):
        os.mkdir(path)
    regex = re.compile(r'src="(.*?).jpg" ')
    for url in pageurl:
        response = requests.get(url,headers = header)
        temp_url = re.findall(regex, response.text)
        for i in temp_url:
            try:
                r = requests.get(i+".jpg",headers = header,timeout=2)
                with open(path+"\\"+str(count)+".jpg",'wb') as f:
                    f.write(r.content)
            except ConnectionError:
                pass
            count+=1
            print("{}.jpg finished".format(count))
            if count==page-1:
            	break
        if count==page-1:
            	break
    print("finish download")


if __name__ == '__main__':
    user_id = ['1312846','1316204','1217486','3026210250','wanglidan']
    path = "E:\\data"
    for i in user_id:
        path = path + "\\" + str(i)
        page = getpage(i)
        getimage(page,i,path)


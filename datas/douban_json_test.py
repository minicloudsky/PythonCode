import requests
import json
from pandas import DataFrame
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

url  = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=rank&page_limit=20&page_start=0'

r = requests.get(url,headers = header)
data = r.json()
dict = data.values()
list = []
for i in dict:
    for j in i:
        list.append(j)
key = list[0].keys()
url = []
playable = []
is_new = []
rate = []
title = []
cover = []
id = []
for i in  list:
    url.append(i['url'])
    playable.append(i['playable'])
    is_new.append(i['is_new'])
    rate.append(i['rate'])
    title.append(i['title'])
    cover.append(i['cover'])
    id.append(i['id'])

data = {'title':title,'url':url,'palyable:':playable,'cover':cover,'id':id,'is_new':is_new}

frame = DataFrame(data)
frame.to_csv('douban_data.csv',index=True)



# coding=utf-8
from urllib.parse import urlencode, quote
import oss2
from oss_config.config import ACCESS_KEY_SECRET, ACCESS_KEY_ID
from itertools import islice
import codecs
import datetime

auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
# Endpoint以杭州为例，其它Region请按实际情况填写。
bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'plus-books')
# 上传文件
uploadfile = bucket.put_object_from_file("07_综合案例一：手写数字识别.ipynb",
                                         "D:\\07_综合案例一：手写数字识别.ipynb")
# <yourLocalFile>由本地文件路径加文件名包括后缀组成，例如/users/local/myfile.txt
# bucket.get_object_to_file('<yourObjectName>', '<yourLocalFile>')
base_url = 'https://plus-books.oss-cn-shenzhen.aliyuncs.com/'
full_file = []
for b in islice(oss2.ObjectIterator(bucket), 1000):
    file_name = b.key.replace(" ","").strip().split("/")
    print(file_name)
    if len(file_name) > 1:
        file_name = file_name[-1]
    else:
        file_name = file_name[0]
    full_file.append({'filename': file_name, 'url': base_url + quote(b.key)})

file_path = 'D:\\blog-backup\\yawuplus.github.io\\blog\source\\book\\index.md'
txt = """
---
title: book
date: {}
categories:
tags:
---
""".format(datetime.datetime.now())
for book in full_file:
    txt += "[{}]({})\r\n".format(book['filename'], book['url'])
with codecs.open(file_path, 'w', encoding='utf-8') as f:
    f.write(txt)

#coding: utf-8
import codecs
f = 'douban_api.py'
f = codecs.open(f,'r',encoding='utf-8')
s = ""

for i in range(103):
    s = s+f.__next__()+"  \n"
print(s)
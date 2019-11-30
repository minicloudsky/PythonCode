import re
#
html = '''<div class="tt"><div class="ttc"><span class="txt"><a href="/song?id=308353"><b title="钟无艳">钟<div class="soil">榀</div>无艳</b></a><span data-res-id="308353" data-res-action="mv" title="播放mv" class="mv">MV</span></span></div></div>'''
# result = re.search('<div class="(.*?)">.*?<a href="(.*?)".*?<b title="(.*?)"',html)
# print(result.group(1),result.group(2),result.group(3))
# result = re.findall('title="(.*?)"',html)
# print(result)

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
# 替换字符串中每一个匹配的子串后返回替换后的字符串
# content = re.sub('\d+','',content)
# content = re.sub('\d+','Replacement',content)
# print(content)
# print(285/820)
html = re.sub('<div.*?>|</div>','',html)
# print(html)
results = re.findall('<||.*?>(.*?)</li>',html,re.S)
# print(results)
content = '''Hello strings Hello 1234567 World_This 
is a Regex Demo Extra strings'''
pattern  = re.compile('Hello.*Demo',re.S)
result = re.match(pattern,content)
result = re.match('Hello.*Demo',content,re.S)
print(result)

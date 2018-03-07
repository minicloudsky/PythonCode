"""
bs4
推荐用lxml解析库，必要使用html.parser
标签选择筛选功能弱但是速度快
建议使用find(),find_all()查询一个或者多个结果
对css选择器熟悉建议用select()
记住常用获取属性和文本值的方法
"""


html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list_small" id="list-2" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))
# find by attributes
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))
# print(soup.find_all(class_='element'))
# print(soup.find_all(text='Foo'))
# find(name,attrs,recursive,text,**kwargs)
# print(soup.find('ul'))
# print(type(soup.find('ul')))
# print(soup.find('page'))
# find_parents()  返回所有祖先节点  find_parent() 返回直接父节点
# print(soup.next_sibling)

# css selector
# class selector
# print(soup.select('.panel-heading'))
# print(soup.select('.panel-body'))
# id selector
# 直接选择标签
# print(soup.select('ul li'))
# 用id选择
# print(soup.select('#list-2,element'))
# print(type(soup.select('ul')[0]))

# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取内容
for li in soup.select('li'):
    print(li.get_text())

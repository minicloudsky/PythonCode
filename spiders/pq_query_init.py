from pyquery import PyQuery
html = '''
<div>
    <ul>
        <li class="item-0">first item><li>
        <li class="item-1"><a href="link3.html"><span class="bold">
        third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
print('hello')
# 三种初始化方法
doc = PyQuery(html)
print(doc('li'))
docs = PyQuery(url='http://wwww.baidu.com')
# print(doc('head'))
docss = PyQuery(filename='demo.html')
# print(docss['head'])

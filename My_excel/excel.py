from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import pandas as pd
import xlrd
import numpy as np
import codecs
# df = pd.read_excel("china.xls")
def write_html(country):
    data = xlrd.open_workbook("D:\\douban\\"+country+".xls")
    table = data.sheet_by_index(0)
    url = []
    title = []
    movie = """<!-- contact.html -->
{% extends "base.html" %}
{% load staticfiles %}
<meta charset="UTF-8">
{% load staticfiles %}
{% block title %} 伊人影视 {% endblock %}
{% block content %}
    <center>
        <h2 style="font-family: 'PingFang SC';font-size: 30px;">伊人影视</h2>
        <nav style="font-size: 30px;text-decoration: none;" role="navigation" class="AppHeader-nav" data-reactid="13">
            <a  href="/movie"  target="_self">热门</a>
            <a  href="/usa"  target="_self">美剧</a>
            <a   href="/uk" target="_self">英剧</a>
            <a   href="/sk" target="_self">韩剧</a>
            <a   href="/japan" target="_self">日剧</a>
            <a   href="/cn" target="_self">国产剧</a>
            <a   href="/hk" target="_self">港剧</a>
            <a   href="/japan_cartoon" target="_self">日本动画</a>
            <a   href="/multi" target="_self">综艺</a>
            <a   href="/doc" target="_self">纪录片</a>
        </nav>
    </center>
    <center>"""




    html = """"""
    for i  in range(1,200):
        url.append(table.cell(i,7).value)
    for i in range(1,200):
        title.append(table.cell(i,6).value)
    for i in range(103):
        html += ' <a href="'+ url[i] +  '" target="_blank"><img border="2" hpace="100" vspace="10" alt="" src="{%' + 'static  "'+country+'/'+ str(i)+'.jpg" %}"  title="'+ title[i]+'">'+ ' </a>'

    movie = movie+html
    movie = movie+"""
    </center>
    <center> <a href="/" target="_self">回到首页</a></center>
{% endblock %}"""
    with codecs.open("D:\\"+country+".html",'w',encoding='utf-8') as f:
        f.write(movie)

if __name__ == '__main__':
    country = ['cn','doc','hk','hot','japan','japan_cartoon','multi','sk','uk','usa']
    for i in country:
        write_html(i)
from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
import pandas as pd
import xlrd
import numpy as np
# df = pd.read_excel("china.xls")
def write_html(country):
    data = xlrd.open_workbook("D:\\douban\\"+country+".xls")
    table = data.sheet_by_index(0)
    url = []
    title = []
    html = """"""
    for i  in range(1,200):
        url.append(table.cell(i,7).value)
    for i in range(1,200):
        title.append(table.cell(i,6).value)
    for i in range(15):
        html += ' <div class="box"><a href="'+ url[i] +  '" target="_blank"><img src="{%' + 'static  "'+country+'/'+ str(i)+'.jpg" %}"  title="{'+ title[i]+'}">'+ ' </a></div>'
    with open("D:\\"+country+".txt",'w',encoding='utf-8') as f:
        f.write(html)
    src = """"""
    for i in range(16,101):
        src+= '{ "src": "'+str(i)+'.jpg" },'
    with open("D:\\"+country+"_src.txt",'w',encoding='utf-8') as f:
        f.write(src)
if __name__ == '__main__':
    country = ['cn','doc','hk','hot','japan','japan_cartoon','multi','sk','uk','usa']
    for i in country:
        write_html(i)
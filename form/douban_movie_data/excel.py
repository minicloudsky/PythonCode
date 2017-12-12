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
    img = []
    html = """"""
    for i  in range(1,200):
        url.append(table.cell(i,7).value)
    for i in range(1,200):
        title.append(table.cell(i,6).value)
    for i in range(1,200):
        img.append(table.cell(i,1).value)
    img_url = ""
    for i in range(50):
        img_url+=' <div class="box"><a href="'+url[i]+'" target="_self"><img src="'+img[i]+'.jpg" alt="" title="'+title[i]+'"></a></div>'
    src = ""
    for i in range(35,120):
        src+='{ "src": "'+img[i]+'" },'
    html  = html+"""{% load staticfiles %}
<!doctype html>
<html lang="zh">
	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>伊人影视</title>
	<style>
* { margin: 0; }
.jq22-container { margin-top: 50px; }
#div1 { margin: auto; position: relative; }
.box { float: left; padding: 10px; border: 1px solid #ccc; background: #f7f7f7; box-shadow: 0 0 8px #ccc; }
.box:hover { box-shadow: 0 0 10px #999; }
.box img { width: 240px; }
        a{
            text-decoration: none;
        }
        a:hover{
            text-decoration: none;
            color: orange;
        }
</style>
	<!--[if IE]>
		<script src="http://libs.baidu.com/html5shiv/3.7/html5shiv.min.js"></script>
	<![endif]-->
	</head>
	<body>
          <center>
        <h1 style="font-family: 'PingFang SC';font-size: 40px;font-style: normal;color: deepskyblue">伊人影视</h1>
        <nav style="font-size: 30px;text-decoration: none;color: " role="navigation" class="AppHeader-nav" data-reactid="13">
            <a  href="/movie"   target="_self" title="热门">热门</a>
            <a  href="/usa"  target="_self" title="美剧">美剧</a>
            <a   href="/uk" target="_self" title="英剧">英剧</a>
            <a   href="/sk" target="_self" title="韩剧">韩剧</a>
            <a   href="/japan" target="_self" 日剧>日剧</a>
            <a   href="/cn" target="_self" title="国产剧">国产剧</a>
            <a   href="/hk" target="_self" title="港剧">港剧</a>
            <a   href="/japan_cartoon" target="_self" title="日本动画">日本动画</a>
            <a   href="/multi" target="_self" title="综艺">综艺</a>
            <a   href="/doc" target="_self" title="纪录片">纪录片</a>
            <a href="/" target="_self" title="回首页">回首页</a>
        </nav>
    </center>
<div class="jq22-container">
      <div class="jq22-content bgcolor-3">
    <div id="div1">"""+img_url+"""
        </div>
  </div>
    </div>
<script src="http://www.jq22.com/jquery/1.7.2/jquery.min.js"></script>
<script src={% static "js/jquery.waterfall.js" %}></script>
<script>
	$("#div1").waterfall({
	    itemClass: ".box",
	    minColCount: 2,
	    spacingHeight: 10,
	    resizeable: true,
	    ajaxCallback: function(success, end) {
	        var data = {"data": ["""+src+"""
	        ]};
	       var str = "";
	       //先用AAA做占位符，然后把AAA替换成图片的url
	        var templ = '<div class="box" style="opacity:0;filter:alpha(opacity=0);"><div class="pic"><img src="AAA" /></div></div>';
	        for(var i = 0; i < data.data.length; i++) {
	            str += templ.replace("AAA", data.data[i].src);
	        }
	        $(str).appendTo($("#div1"));
	        success();
	        end();
	    }
	});
	</script>
</body>
</html>"""
    with codecs.open("D:\\"+country+".html",'w',encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    country = ['cn','doc','hk','hot','japan','japan_cartoon','multi','sk','uk','usa']
    for i in country:
        write_html(i)
import os
import codecs
start = """<!DOCTYPE html>
<html>
<head>
	<title>	
"""
pre = """</title>
	<style type="text/css" media="screen">
	img{
    border:1px solid #C6E2FF;
}	
	</style>
</head>
<body>"""
middle = """
<div class="img">"""
img = []
end = """</div>
</body>
</html>"""
html_name = ""
path ="D:\\zhihu"
img_path = []
count = 0
name_list = os.listdir(path)
for i in os.listdir(path):
    img_path.append(path+"\\"+i+"\\img_url.txt")

for i in img_path:
    html = start
    html +=str(name_list[count])
    html+=pre
    html +="""<center><h3 style="color: skyblue;font-size: 30px;"">{}?</h3></center>""".format(str(name_list[count]))
    html+=middle
    file = open(i,'r')
    while 1:
        line = file.readline()
        html +="""<a href="{}" target="_blank" ><img src="{}" width="300" height="300" border="2"></a>""".format(line,line)
        if not line:
            break
    file.close()
    html += end
    with codecs.open("D:\\html\\"+str(name_list[count])+".html",'w+',encoding='utf-8') as f:
        f.write(html)
    count +=1
    f.close()

main_html = """<!DOCTYPE html>
<html>
<head>
	<title>知乎有趣的问题下的图片 (ฅ´ω`ฅ)	</title>
		<style>
	a:hover{
	color:#A8A8A8;
	}
	a{
		text-decoration:none;
		color: black;
	}
#list1 li:nth-of-type(odd){ background:#87CEFA;}奇数行 
#list1 li:nth-of-type(even){ background:#F08080;}偶数行 
#list2 li:nth-child(4n+1){ background:#00ccff;}从第一行开始算起 每隔4个（包含第四个）使用此样式 
#list00000 li:nth-child(4n+2){background:#090;}从第二行开始算起 每隔4个（包含第四个）使用次样式 
#list00000 li:nth-child(4n+3){background:#009;}从第三行开始算起 每隔4个（包含第四个）使用次样式 
#list00000 li:nth-child(4n+4){background:#990;}从第四行开始算起 每隔4个（包含第四个）使用次样式 
</style> 
<body>
<center><h3 style="color: #F08080;font-size: 30px;">知乎上，一些有趣的回答下的图片汇总\(^o^)/</h3></center>
<div style="align: center;">
<ul id="list1">
"""
for i in name_list:
    main_html+= """<li><a  style="color: black;font-size: 25px;"  href="zhihu/{}.html\" title="{}\" target="_blank">{}?</a></li><br>""".format(i,i,i)
main_html += """</ul></div></body></html>"""

with codecs.open("D:\\html\\zhihu.html",'w',encoding='utf-8') as f:
    f.write(main_html)








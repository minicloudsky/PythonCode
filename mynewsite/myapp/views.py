#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404
# Create your views here.
from myapp.models import Product
def about(request):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About Myself</title>
</head>
<body>
<h2>xiaojiajia</h2>
</body>
</html>
    '''
    return HttpResponse(html)

def listing(request):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>手机列表</title>
</head>
<body>
<h2></h2>
<hr>
<table width = 400 border = 1,bgcolor = '#ccffcc'>
{}
</table>
</body>
</html>
    '''
    products  = Product.objects.all()
    tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
    for p in products:
        tags = tags+'<tr><td>{}</td>'.format(p.name)
        tags = tags+'<td>{}</td>'.format(p.price)
        tags = tags+'<td>{}</td></tr>'.format(p.sku)
    return HttpResponse(html.format(tags))

def disp_listing(request,sku):
    html  ='''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{}</title>
</head>
<body>
<h2>{}</h2>
<hr>
<table width = 400 border = 1 bgcolor = '#ccffcc'>
{}
</table>
</body>
</html>'''
    try:
        p = Product.objects.get(sku =sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(p.sku)
    tags = tags + '<tr><td>产品名称</td><td>{}</td></tr>'.format(p.name)
    tags = tags + '<tr><td>二手售价</td><td>{}</td></tr>'.format(p.price)
    tags = tags + '<tr><td>库存数量</td><td>{}</td></tr>'.format(p.sku)
    return HttpResponse(html.format(p.name,p.name,tags))


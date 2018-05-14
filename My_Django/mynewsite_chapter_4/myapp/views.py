#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse,Http404
import random
from myapp.models import Product
from django.template.loader import get_template
def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def listing(request):
    products  = Product.objects.all()
    template = get_template('list.html')
    html = template.render({'products':products})
    return HttpResponse(html)

def disp_detail(request,sku):
    try:
        p = Product.objects.get(sku =sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    template = get_template('disp.html')
    html = template.render({'product': p})
    return HttpResponse(html)

def welcome(request):
    slogan = [
        '专心敲代码，天道自酬勤'
        'I will climb',
        'I will run',
        'I will soar'
    ]
    template = get_template('welcome.html')
    html = template.render({'slogan': random.choice(slogan)})
    return HttpResponse(html)

def index(request):
    slogan = [
        '专心敲代码，天道自酬勤'
        'I will climb',
        'I will run',
        'I will soar'
    ]
    template = get_template('index.html')
    html = template.render({'quote': random.choice(slogan)})
    return HttpResponse(html)

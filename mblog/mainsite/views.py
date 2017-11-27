# -*- coding: utf-8 -*-
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    posts_list = list()
    for post in posts:
        posts_list.append(post.title)
    now = datetime.now()
    # locals()函数会把当前内存中收到的所有局部变量使用字典类型打包起来
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug= slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        # 发生例外找不到时候，重定向到首页
        return redirect('/')

def showabout(request):
    author = "I am 瞻彼淇奥"
    template = get_template('about.html')
    try:
        html = template.render(locals())
        return HttpResponse(html)
    except:
        return redirect('/')
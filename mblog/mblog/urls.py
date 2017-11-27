# -*- coding: utf-8 -*-
"""mblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from mainsite.views import homepage, showpost,showabout

urlpatterns = [
    # '^'表示字符串开头，'$' 匹配字符串结尾,两个字符连接在一起是指当有用户浏览网址没有加上任何字符串时候(即根网址),就去调用
    # homepage函数,
    url(r'^$', homepage),
    # 把 post/ 开头的网址后面的字符串都找出来,当做第二个参数传送给showpost参数
    # showpost在import的地方要记得导入,同时到views.py中新建这个函数来处理接收到的参数
    url(r'^post/(\w+)$', showpost),
    url(r'^admin/', include(admin.site.urls)),
    # about page
    url(r'^$',homepage)
]

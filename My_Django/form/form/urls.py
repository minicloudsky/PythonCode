"""form URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from mysite import views
import django_markdown
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    # 前面接收数字，后面接收文字
    url(r'^(\d+)/(\w+)/$',views.index),
    url(r'^about/$',views.about),
    url(r'^list/$',views.listing),
    url(r'^get/$',views.get),
    # post method
    url(r'^post/$', views.post),
    # contact
    url(r'^contact/$',views.contact),
    # 配置伊人电影的url
    url(r'^movie/$',views.movie),
    url(r'^cn/$',views.cn),
    url(r'^doc/$',views.doc),
    url(r'^hk/$',views.hk),
    url(r'^japan_cartoon/$',views.japan_cartoon),
    url(r'^japan/$',views.japan),
    url(r'^multi/$',views.multi),
    url(r'^sk/$',views.uk),
    url(r'^usa/$',views.usa),
    url(r'^uk/$',views.uk),
    # 配置博客文章的url
    url(r'^passage/$',views.passage),
    url(r'^article/(\w+)$', views.showpassage),
]

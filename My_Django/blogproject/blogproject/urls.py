"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
# 整个工程项目的URL配置文件
from django.conf.urls import url,include
from django.contrib import admin
from blog.feeds import AllPostRssFeed
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 引入blog和comments的url配置
    url(r'', include('blog.urls')),
    url(r'',include('comments.urls')),
    url(r'^all/rss/$',AllPostRssFeed(),name='rss'),
    url(r'^search/',include('haystack.urls')),
    url(r'users/',include('users.urls')),
    url(r'^users/',include('django.contrib.auth.urls')),
]

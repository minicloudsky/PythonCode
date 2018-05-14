# blog应用相关的url配置
from django.conf.urls import url
from . import views
# 告诉 Django 这个 urls.py 模块是属于 blog 应用的，
# 这种技术叫做视图函数命名空间
app_name = 'blog'
urlpatterns = [
    # views.IndexView.as_view()把视图类转换成视图函数
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagView.as_view(),name='tag'),
    # url(r'^search/$',views.search,name='search'),
    url(r'^about/$',views.About,name='about'),
    url(r'^contact/$',views.Contact,name='contact'),
    url(r'^all/$', views.PostAllView.as_view(), name='allpassage'),
]
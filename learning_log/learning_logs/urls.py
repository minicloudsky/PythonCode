"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
urlpatterns = [
    # main page
    url(r'^$',views.index,name='index'),
    # 显示所有的主题
    url(r'^topics/$',views.topics),
#  特定主体的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]

from django.shortcuts import render,render_to_response,HttpResponse
from .models import Topic
# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render_to_response('index.html')
    # return HttpResponse('hhhhhh')

def topics(request):
    # 显示所有的主题
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    #return render(request,'topics.html',context)
    return render_to_response('topics.html',locals())
    # return HttpResponse("mytopics")
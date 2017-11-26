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

def topic(request,topic_id):
    """显示单个主体及其所有的条目"""
    topic = Topic.objects.get(id = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topics': topic,'entries': entries}
    return render(request,'learning_logs/topic.html',context)

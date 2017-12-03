from mysite import models
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Mood,Post
# Create your views here.


def index(request, pid=None, del_pass = None):
    template = get_template('index.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_date')[:30]
    moods = models.Mood.objects.all()
    nickname = None
    content = None
    pwd = None
    usermood = None
    message = None
    try:
        nickname = request.GET.get('nickname')
        pwd = request.GET.get('pwd')
        content = request.GET.get('content')
        usermood = request.GET.get('mood')
    except:
        message = '如果要发帖必须填写每一个字段'
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id = pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = '数据删除成功'
            else:
                message = '密码错误'
    elif nickname!=None:
        mood = models.Mood.objects.get(status= usermood)
        post = models.Post.objects.create(mood =mood,nickname = nickname,
                                          del_pass = pwd,message = content)
        post.save()
        message = '成功存储，请记得你的编辑密码[{}]，信息需要审核后即可显示.'.format(pwd)
    html = template.render(locals())
    return HttpResponse(html)


def about(request):
    template = get_template('about.html')
    username = None
    age = None
    try:
        username = request.GET['username']
        age = request.GET['age']
    except:
        pass
    if username!=None:
        person = models.Person.objects.create(name = username,age = int(age))
        person.save()
    html = template.render(locals())
    return HttpResponse(html)


def add(request,a,b):
    c = int(a)+ int(b)
    return HttpResponse(str(c))





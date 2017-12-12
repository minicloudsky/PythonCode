from mysite import models,forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
# Create your views here.
# home page
def index(request, pid=None, del_pass = None):
    template = get_template('index.html')
    posts = models.Post.objects.filter(enabled= True).order_by('-pub_date')[:30]
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
    except :
        pass
        # nickname = None
        # message = '如果要发帖必须填写每一个字段...'
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
    now = time.ctime()
    html = template.render(locals())
    return HttpResponse(html)
# 浏览页面
def listing(request):
    template = get_template('listing.html')
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_date')[:150]
    moods = models.Mood.objects.all()
    html = template.render(locals())
    return HttpResponse(html)
# 发帖页面
def get(request):
    template = get_template('get.html')
    moods = models.Mood.objects.all()
    message = '如果要发布信息，那么每一个字段都要填...'
    html = template.render(locals())
    return HttpResponse(html)
# 用post请求来发帖，主要为了验证CSRF
@csrf_protect
def post(request):
    if request.method =='POST':
        message = '用的是post请求'
    template = get_template('post.html')
    moods = models.Mood.objects.all()
    message = '如果要发帖，那么要填写每一个字段...'
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)
# 用post请求向管理员写信
def contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = '感谢您的来信'
            user_name = form.cleaned_data['user_name']
            user_city = form.cleaned_data['user_city']
            user_school = form.cleaned_data['user_school']
            user_email = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            letter = models.Letter.objects.create(username = user_name, city = user_city,
                school = user_school, email = user_email, content = user_message)
            letter.save()
        else:
            message = '请检查您输入的信息是否正确'
    else:
        form = forms.ContactForm()
    template = get_template('contact.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)

# 以下几个函数，并不传输数据，只是为了渲染伊人电影的模板
def movie(request):
    template = get_template('movie.html')
    html = template.render(locals())
    return HttpResponse(html)

def cn(request):
    template = get_template('cn.html')
    html = template.render(locals())
    return HttpResponse(html)
def doc(request):
    template = get_template('doc.html')
    html = template.render(locals())
    return HttpResponse(html)
def hk(request):
    template = get_template('hk.html')
    html = template.render(locals())
    return HttpResponse(html)
def japan(request):
    template = get_template('japan.html')
    html = template.render(locals())
    return HttpResponse(html)
def japan_cartoon(request):
    template = get_template('japan_cartoon.html')
    html = template.render(locals())
    return HttpResponse(html)
def multi(request):
    template = get_template('multi.html')
    html = template.render(locals())
    return HttpResponse(html)
def sk(request):
    template = get_template('sk')
    html = template.render(locals())
    return HttpResponse(html)
def uk(request):
    template = get_template('uk.html')
    html = template.render(locals())
    return HttpResponse(html)
def usa(request):
    template = get_template('usa.html')
    html = template.render(locals())
    return HttpResponse(html)







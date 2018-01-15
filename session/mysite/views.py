from mysite import models,forms
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
import datetime
from .models import Passage
import markdown
# Create your views here.
# home page
def index(request, pid=None, del_pass = None):
    if 'username' in request.COOKIES and 'usercolor' in request.COOKIES:
        username = request.COOKIES['username']
        usercolor = request.COOKIES['usercolor']
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    return HttpResponse(html)
# about page
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


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = models.User.objects.get(name=login_name)
                if user.password == login_password:
                    response = redirect('/')
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    return redirect('/')
                else:
                    message = '密码错误,请再检查一次'
            except:
                message = '目前无法登录'
            message = "登录成功"
        else:
            message = '请检查输入的字段内容'
    else:
        login_form = forms.LoginForm()
    template = get_template('login.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)
    response = HttpResponse(html)
    return response

def logout(request):
    response = redirect('/')
    response.delete_cookie('username')
    return response








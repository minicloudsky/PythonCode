
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
import time
import datetime

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'alex' and pwd == '123':
            request.session['IS_LOGIN'] = True
            request.session['USRNAME'] = 'alex'
            return redirect('/home/')
        elif username == 'eirc' and pwd == '123':
            request.session['IS_LOGIN'] = True
            request.session['USRNAME'] = 'eirc'
            return redirect('/home/')

    return render(request, 'login.html')

def home(request):
    is_login = request.session.get('IS_LOGIN', False)
    if is_login:
        username = request.session.get('USRNAME', False)
        return render(request, 'home.html', {'username': username})
    else:
        return redirect("/")








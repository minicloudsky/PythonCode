from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from myapp import models
# Create your views here.

def index(request):
    template = get_template('')
    html = template.render(locals())
    return HttpResponse(html)
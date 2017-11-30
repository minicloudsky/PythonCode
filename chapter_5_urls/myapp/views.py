from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from django.http import HttpResponse
def index(request):
    now = datetime.now()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)
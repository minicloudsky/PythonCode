from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.http import HttpResponse
def index(request):
    template  = get_template("index.html")
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        message = "cookie supported"
    else:
        message = "cookie not supported"
    request.session.set_test_cookie()
    html = template.render(locals())
    return HttpResponse(html)
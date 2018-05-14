from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import User
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    #     只有当请求为POST时候，才表示用户提交了注册信息
    # 从 get 或者 post 请求中获取 next 参数值
    # get 请求中，next 通过 url 传递，即 /?next=value
    # post 请求中，next 通过表单传递，即 <input type="hidden"
    # name="next" value="{{ next }}"/>
    redirect_to = request.POST.get('next',request.GET.get('next',''))

    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的save方法将用户数据保存到数据库
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:
                # 注册成功,跳转回首页
                return redirect('/')
    else:
        # 请求不是POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        # 渲染模板
        # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
        # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
        # 将记录用户注册前页面的 redirect_to 传给模板，以维持 next 参数在整个注册流程中的传递
        form = RegisterForm()
    return render(request,'users/register.html',context={'form' : form,'next':redirect_to})



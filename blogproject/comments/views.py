from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request,post_pk):
    """
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来。
    # 这里我们使用了 Django 提供的一个快捷函数 get_object_or_404，
    # 这个函数的作用是当获取的文章（Post）存在时，则获取；否则返回 404 页面给用户。
    """
    post = get_object_or_404(Post,pk=post_pk)
    # HTTP 请求有 get 和 post 两种，一般用户通过表单提交数据都是通过 post 请求，
    # 因此只有当用户的请求为 post 时才需要处理表单数据。
    if request.method =='POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来.
            comment.post = post
            # 最终将评论数据保存进数据库,调用模型实例的save方法
            comment.save()
            # 重定向到post 的详情页,实际上当redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的url。
            return redirect(post)
        else:
            # 检查到数据不合法，重新渲染详情页，并且渲染表单的错误。
            # 因此我们传了三个模板变量给 detail.html，
            # 一个是文章（Post），一个是评论列表，一个是表单 form
            # 注意这里我们用到了 post.comment_set.all() 方法，
            # 这个用法有点类似于 Post.objects.all()
            # 其作用是获取这篇 post 下的的全部评论，
            # 因为 Post 和 Comment 是 ForeignKey 关联的，
            # 因此使用 post.comment_set.all() 反向查询全部评论。
            # 具体请看下面的讲解。
            comment_list = post.comment_set.all()
            context = {'post' : post,
                       'form' : form,
                       'comment_list' : comment_list
            }
            return render(request,'blog/detail.html',context= context)

    #    不是post请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)
"""首先我们使用了 redirect 函数。这个函数位于 django.shortcuts 模块中，它的作用是对 HTTP 请求进行重定向
（即用户访问的是某个 URL，但由于某些原因，服务器会将用户重定向到另外的 URL）。redirect 既可以接收一个 URL 作为参数，
也可以接收一个模型的实例作为参数（例如这里的 post）。如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url
 方法，这样 redirect 会根据 get_absolute_url 方法返回的 URL 值进行重定向。
另外我们使用了 post.comment_set.all() 来获取 post 对应的全部评论。 Comment 和Post 是通过 ForeignKey 关联的，
回顾一下我们当初获取某个分类 cate 下的全部文章时的代码：Post.objects.filter(category=cate)
。这里 post.comment_set.all() 也等价于 Comment.objects.filter(post=post)，
即根据 post 来过滤该 post 下的全部评论。但既然我们已经有了一个 Post 模型的实例 post
（它对应的是 Post 在数据库中的一条记录），那么获取和 post 关联的评论列表有一个简单方法，
即调用它的 xxx_set 属性来获取一个类似于 objects 的模型管理器，然后调用其 all 方法来返回这个 post 关联的全部评论。 
其中 xxx_set 中的 xxx 为关联模型的类名（小写）。
例如 Post.objects.filter(category=cate) 也可以等价写为 cate.post_set.all()。"""
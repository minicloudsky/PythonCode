from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count
# 自定义模板标签
register = template.Library()


# 最新文章模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签,按照月份归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month','DESC')


# 分类模板标签

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入Category类
    #Count 计算分类下的文章数，其接受的参数为需要技术的模型的名称
    return Category.objects.annotate(num_posts = Count('post')).filter(num_posts__gt = 0)

@register.simple_tag
def get_tags():
    # 记得在顶部引入Tag model
    return Tag.objects.annotate(num_posts = Count('post')).filter(num_posts__gt = 0)

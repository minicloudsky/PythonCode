from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    #标题
    title = models.CharField(max_length=70)
    #正文
    body = models.TextField()
    #创建时间和修改时间
    created_time = models.DateTimeField(max_length=200,blank=True)
    modified_time = models.DateTimeField()
    #文章摘要
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

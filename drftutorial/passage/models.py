from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.

class Passage(models.Model):
    title = models.CharField('标题', max_length=100, default='title')
    content = models.TextField('正文内容')
    background_img = models.CharField('文章背景图片', max_length=2000, blank=True)
    like_count = models.IntegerField('点赞数', default=0)
    post_time = models.DateTimeField('发布时间')
    is_draft = models.BooleanField('是否为草稿', default=True)
    # add_time = models.DateTimeField('添加时间',auto_now_add=True,default=now)
    add_time = models.DateTimeField('修改时间',auto_now=True)
    
    def __str__(self):
        return self.title

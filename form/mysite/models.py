from django.db import models
# admin username: django pwd: admin123
# Create your models here.
from django.utils import timezone

class Mood(models.Model):
    status = models.CharField(max_length=10,null=False)

    def __unicode__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey('Mood',on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10,default='不愿透露身份的人')
    message = models.TextField(null=False)
    # 删除信息的密码
    del_pass = models.CharField(max_length=10)
    pub_date = models.DateTimeField(auto_now_add=True)
    # 是否显示到网站上
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.message

class Letter(models.Model):
    username = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField()

    def __unicode__(self):
        return self.username






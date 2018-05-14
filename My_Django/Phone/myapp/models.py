#coding: utf-8
from django.db import models

# Create your models here.

class Maker(models.Model):
    name = models.CharField(max_length= 10)
    country = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class PModel(models.Model):
    maker = models.ForeignKey(Maker,on_delete= models.CASCADE)
    name = models.CharField(max_length=20)
    url  = models.URLField(default='https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2185754641,3181969753&fm=11&gp=0.jpg')

    def __unicode__(self):
        return self.name

class Product(models.Model):
    pmodel = models.ForeignKey(PModel,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=15,default='智能手机')
    description = models.TextField(default='暂未说明')
    year = models.PositiveIntegerField(default=2015)
    price = models.PositiveIntegerField(default=0)
    def __unicode__(self):
        return self.nickname

class PPhoto(models.Model):
    product = models.ForeignKey(Product,on_delete= models.CASCADE)
    description = models.CharField(max_length=20,default='产品照片')
    url = models.URLField(default='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1512139141586&di=5849f10c51450f403d17054d65b00322&imgtype=0&src=http%3A%2F%2Fupload.techweb.com.cn%2F2017%2F1020%2F1508470841317.jpg')

    def __unicode__(self):
        return self.description
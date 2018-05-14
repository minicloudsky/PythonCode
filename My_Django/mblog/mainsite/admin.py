# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post, About
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('author','resume','update_date')


admin.site.register(Post,PostAdmin)
admin.site.register(About,AboutAdmin)
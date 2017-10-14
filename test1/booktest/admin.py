from django.contrib import admin
from .models import *
# Register your models here.

class BoonInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
admin.site.register(BookInfo,BoonInfoAdmin)
admin.site.register(HeroInfo)
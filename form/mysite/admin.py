from django.contrib import admin
from mysite import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','enabled','pub_date')
    ordering = ('-pub_date',)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('status',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age',)
    ordering = ('-age',)


admin.site.register(models.Mood,MoodAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Person,PersonAdmin)
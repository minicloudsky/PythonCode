from django.contrib import admin
from mysite import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('nickname','message','enabled','pub_date')
    ordering = ('-pub_date',)
class MoodAdmin(admin.ModelAdmin):
    list_display = ('status',)

class LetterAdmin(admin.ModelAdmin):
    list_display = ('username','city','school','email','content')

class PassageAdmin(admin.ModelAdmin):
    list_display = ('title','slug','body','pub_date')

admin.site.register(models.Mood,MoodAdmin)
admin.site.register(models.Post,PostAdmin)
admin.site.register(models.Letter,LetterAdmin)
admin.site.register(models.Passage,PassageAdmin)
admin.site.register(models.User)



from django.contrib import admin
from mysite import models
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(models.Account)


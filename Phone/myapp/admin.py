from django.contrib import admin
from myapp import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel','nickname','price','year')
    search_fields = ('nickname',)
    ordering = ('-price',)


class MakerAdmin(admin.ModelAdmin):
    list_display = ('name','country')
    search_fields = ('country',)
    ordering = ('name',)


class PModelAdmin(admin.ModelAdmin):
    list_display = ('maker','name','url')
    ordering = ('name',)


class PPhotoAdmin(admin.ModelAdmin):
    list_display = ('product','description','url')


admin.site.register(models.Product,ProductAdmin)
admin.site.register(models.Maker,MakerAdmin)
admin.site.register(models.PModel,PModelAdmin)
admin.site.register(models.PPhoto,PPhotoAdmin)

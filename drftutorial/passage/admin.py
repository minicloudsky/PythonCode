from django.contrib import admin
from passage.models import Passage


# Register your models here.
class PassageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',  'content', 'background_img', 'like_count',
                    'post_time', 'is_draft']
    search_fields = ['title', 'content']


admin.site.register(Passage, PassageAdmin)

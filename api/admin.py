from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category' ,'creat_content','updated_content','get_photo']
    list_display_links = ['id','title','category']
    search_fields = ['title','content']
    list_filter = ('category',)
    fields = (
        'title', 'category', 'creat_content', 'updated_content', 'content', 'photo', 'get_photo', 'views_posts'
    )
    readonly_fields = (
        'creat_content', 'updated_content','get_photo','views_posts'
    )
    save_on_top = True

    def get_photo(self,object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="60" >')
        else:
            return 'Photo dont has been'

    get_photo.short_description = 'Фоточка :з'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','quentity')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('title','quentity')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.site_title = 'Управление блогом'
admin.site.site_header = 'Повелитель,укажите путь...'
# Register your models here.

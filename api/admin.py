from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category' ,'creat_content','updated_content']
    list_display_links = ['id','title','category']
    search_fields = ['title','content']
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','quentity')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('title','quentity')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.

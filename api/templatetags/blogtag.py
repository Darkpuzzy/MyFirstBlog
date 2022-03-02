from django import template
from api.models import *
from django.db.models import *

register = template.Library()

@register.simple_tag()
def get_category():
    return Category.objects.all()

@register.inclusion_tag('api/list_categories.html')
def show_categories(arg1='Hello',arg2='World'):
    # categories = Category.objects.all()
    # categories = Category.objects.annotate(cnt=Count('blog')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('blog', filter=F('blog__category_id'))).filter(cnt__gt=0)
    return {"categories": categories,'arg1':arg1,'arg2':arg2,}
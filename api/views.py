from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class HomeBlog(ListView):
    model = Blog
    template_name = 'api/home_blog_list.html'
    context_object_name = 'Blog'
    paginate_by = 4
    # extra_context = {'title': 'Главная'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница' # в html изменить заголовок и будет этот титл
        return context


    def get_queryset(self):
        return Blog.objects.all().select_related('category')


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class BlogCategory(ListView):
    model=Blog
    template_name = 'api/home_blog_list.html'
    context_object_name = 'Blog'
    allow_empty = False
    # queryset = Blog.objects.select_related('category')

    def get_queryset(self):
        return Blog.objects.filter(category_id=self.kwargs['category_id']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id']) # в html изменить заголовок и будет этот титл
        return context


class ViewBlogPost(DetailView):
    model = Blog
    context_object_name = 'blog_item'
    # pk_url_kwarg = 'blog_id'


class CreateBlogPost(LoginRequiredMixin, CreateView):
    login_url = '/admin/'
    form_class = BlogForm
    template_name = 'api/add_blog.html'


# def counter():
#     counter_category = {}
#     cat_len = Category.objects.all()
#     for i in cat_len:
#         blogs = Blog.objects.filter(category=i.id)
#         objects = len(blogs)
#         i.quentity = int(objects)
#         i.save()
#         counter_category[f'{i}'] = int(objects)
#     return counter_category


# def index(request):
#     blog = Blog.objects.all()
#     context = {
#         'blog': blog,
#         'title': 'Заголовки',
#     }
#     if request:
#         counter()
#     return render(request, template_name='api/index.html',context=context)


# def get_category(request,category_id):
#     blogs = Blog.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'blog': blogs,
#         'category': category
#     }
#     return render(request,'api/category.html',context)


# def view_blog(request,blog_id):
#     #blog_item = Blog.objects.get(pk=blog_id)
#     blog_item =get_object_or_404(Blog,pk=blog_id)
#     context = {
#         "blog_item":blog_item,
#     }
#     return render(request, 'api/view_blog.html',context)


# def add_blog(request):
#     if request.method == 'POST':
#         form = BlogForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # blog_re = Blog.objects.create(**form.cleaned_data)
#             blog_re = form.save()
#             return redirect(blog_re)
#     else:
#         form = BlogForm()
#     if request:
#         counter()
#     return render(request, 'api/add_blog.html', {'form': form})

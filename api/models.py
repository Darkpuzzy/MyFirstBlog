from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length= 150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    creat_content = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_content = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фотография', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views_posts = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_blogs',kwargs={"pk":self.pk})


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-creat_content']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок категории')
    quentity = models.IntegerField(default=1, verbose_name = 'Кол-во статей')


    def get_absolute_url(self):
        return reverse('category',kwargs={"category_id":self.pk})



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'
        ordering = ['-quentity']

from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError





class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows":5}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'photo': forms.ImageField()
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title














# ФОРМА НЕ СВЯЗАННАЯ С МОДЕЛЬЮ
#title = forms.CharField(max_length=150, label="Название",
#                            widget=forms.TextInput(attrs={"class":"form-control"}))
#    content = forms.CharField(label="Текст",
 #                             widget=forms.Textarea(attrs={
  #                                "class":"form-control",
  #                                "rows": 5
 #                             })) # required = False ( необязательное заполнение )
  #  category = forms.ModelChoiceField(queryset=Category.objects.all(),
  #                                    label="Категория", empty_label="(Выберите категорию)",
  #                                    widget=forms.Select(attrs={
  #                                        "class":"form-control"
   #                                   }))
  #  photo = forms.ImageField(label='Загрузите фото')
    #photo = forms.ImageField
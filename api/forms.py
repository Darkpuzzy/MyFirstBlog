from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # username = forms.CharField(label="Имя пользователя", help_text ="", widget = )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
                    }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        # fields = '__all__'
        fields = ['title', 'content', 'category', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows":5}),
            'category': forms.Select(attrs={"class": "form-control"}),
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
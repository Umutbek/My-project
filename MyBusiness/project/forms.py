from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django import forms
class Addform(ModelForm):
    class Meta:
        model=Adding
        fields=['customer','Название','Количество','Стоимость','Категория']
class Soldform(ModelForm):
    class Meta:
        model=Sell
        fields="__all__"
        exclude=('customer',)
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

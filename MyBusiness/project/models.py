from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Category(models.Model):
    name=models.CharField(max_length=100)
class Adding(models.Model):
    cat=(
    ('Весенние','Весенние'),
    ('Летние','Летние'),
    ('Осенние','Осенние'),
    ('Зимние','Зимние'),
    ('Другие','Другие'),
    )
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    Название=models.CharField(max_length=100)
    Количество=models.IntegerField()
    Стоимость=models.IntegerField()
    Категория=models.CharField(max_length=100,choices=cat)
    total=models.IntegerField(null=True)
    def __str__(self):
        return self.Название
class Sell(models.Model):
    customer=models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    adding=models.ForeignKey(Adding,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    количество=models.IntegerField()
    def __str__(self):
        return self.adding.Название

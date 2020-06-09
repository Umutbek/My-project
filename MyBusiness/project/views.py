from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .decorators import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
            )
            messages.success(request,'Account was created for ' + username)
            return redirect('login')
    context={'form':form}
    return render(request,'register.html',context)
@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('my_html')
        else:
            messages.error(request, 'Username or Password incorrect')
    context={}
    return render(request,'login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def my_html(request):
    categ1=Category.objects.all()
    showing=request.user.customer.adding_set.all()
    for i in showing:
        i.total=i.Количество*i.Стоимость
        i.save()
    context={'showing':showing,'categ1':categ1}
    return render(request,'my_html.html',context)
@login_required(login_url='login')
def add1(request):
    categ1=Category.objects.all()
    customer=request.user
    form=Addform(initial={'customer':customer})
    if request.method=='POST':
        form=Addform(request.POST,initial={'customer':customer})
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'categ1':categ1}
    return render(request,'add.html',context)
@login_required(login_url='login')
def update(request,pk):
    update=Adding.objects.get(id=pk)
    categ1=Category.objects.all()
    form=Addform(instance=update)
    if request.method=='POST':
        form=Addform(request.POST, request.FILES, instance=update)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'categ1':categ1}
    return render(request,'add.html',context)
@login_required(login_url='login')
def delete_product(request,pk):
    categ1=Category.objects.all()
    del1=Adding.objects.get(id=pk)
    if request.method=="POST":
        del1.delete()
        return redirect('/')
    context={'del1':del1,'categ1':categ1}
    return render(request,'delete_product.html',context)
@login_required(login_url='login')
def show(request,pk):
    categ1=Category.objects.all()
    categ=Category.objects.get(id=pk)
    if categ.name=='Весенние':
        showing1=Adding.objects.filter(Категория="Весенние")
    elif categ.name=='Летние':
        showing1=Adding.objects.filter(Категория="Летние")
    elif categ.name=='Осенние':
        showing1=Adding.objects.filter(Категория="Осенние")
    elif categ.name=='Зимние':
        showing1=Adding.objects.filter(Категория="Зимние")
    else:
        showing1=Adding.objects.filter(Категория="Другие")
    context={'categ':categ,'showing1':showing1,'categ1':categ1}
    return render(request,'show.html',context)
@login_required(login_url='login')
def sell_product(request,pk):
    categ1=Category.objects.all()
    adding=Adding.objects.get(id=pk)
    umut=Sell.objects.all()
    form=Soldform(initial={'adding':adding})
    if request.method=='POST':
        form=Soldform(request.POST)
        if form.is_valid():
            if int(request.POST['количество'])>adding.Количество:
                messages.error(request,"У вас недостаточно товаров")
                return redirect("sell_product", pk=adding.id)
            else:
                form.save()
                for i in umut:
                    if i.adding.id==adding.id:
                        adding.Количество-=int(request.POST['количество'])
                        adding.save()
                        return redirect('/')
    context={'form':form,'categ1':categ1}
    return render(request,'add.html',context)
@login_required(login_url='login')
def sell(request):
    categ1=Category.objects.all()
    sell1=request.user.customer.sell_set.all()
    for i in sell1:
        i.adding.total=i.количество*i.adding.Стоимость
        i.save()
    context={'sell1':sell1,'categ1':categ1}
    return render(request,'sell.html',context)
@login_required(login_url='login')
def sell_delete(request,pk):
    categ1=Category.objects.all()
    del2=Sell.objects.get(id=pk)
    if request.method=="POST":
        del2.delete()
        return redirect('sell')
    context={'del2':del2,'categ1':categ1}
    return render(request,'sell_delete.html',context)

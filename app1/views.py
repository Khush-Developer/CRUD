from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.contrib import messages

# Create your views here.
def registration(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email is in Database")
        else:
            User.objects.create(name=name,email=email,password=password)
            return redirect("/login/")

def login(request):
    return render(request,'login.html')

def table(request):
    table_obj=User.objects.all()
    return render(request,'table.html',{'table_obj': table_obj}) 

def update(request,uid):
    update=User.objects.get(id=uid)
    return render(request,'update.html',{'update':update})

def update_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        name = request.POST["name"]
        email = request.POST["email"]
        User.objects.filter(id=uid).update(name=name, email=email)
        return redirect("/table/")

def index(request):
    return render(request,'index.html')

def user_login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(email=email).exists():
            obj= User.objects.get(email=email)
            password=obj.password
        if check_password(password,password):
            return redirect('/welcome/')
        else:
            return HttpResponse('password incorrect')
    else:
        return HttpResponse('Email is not registered')

def delete(request):
    id=request.GET['id']
    User.objects.get(id=id).delete()
    return redirect('/table/')       
def welcome(request):
    return render(request,'welcome.html')

from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages, auth 
from django.contrib.auth.models import User
from django.conf import settings
import os
from .models import Uploads,register,home

y=register
z=Uploads

def index(request):
  x=home.objects.all()
  return render(request,'realtekrealty/index.html',{"x":x})

def about(request):
    return render(request,'realtekrealty/about.html')

def contact(request):
    return render(request,'base.html')

def hse(request):
  vids=z.objects.all()
  return render(request,'realtekrealty/hse.html',{"vids":vids})
def register(request):
  if request.method == 'POST':
    y.firstname = request.POST['firstname']
    y.lastname = request.POST['lastname']
    y.username = request.POST['username']
    y.email = request.POST['email']
    y.password = request.POST['password']
    y.password2 = request.POST['password2']

    if y.password == y.password2:
      if User.objects.filter(username=y.username).exists():
        messages.error(request, 'That username is taken')
        return redirect('realtekrealty:register')
      else:
        if User.objects.filter(email=y.email).exists():
          messages.error(request, 'That email is being used')
          return redirect('realtekrealty:register')
        else:
          user = User.objects.create_user(username=y.username, password=y.password,email=y.email, first_name=y.first_name, last_name=y.last_name)
        
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('realtekrealty:login')
    else:
      messages.error(request, 'Passwords dont match')
      return redirect('realtekrealty:register')
  else:
    return render(request, 'realtekrealty/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are logged in')
      return redirect('realtekrealty:index')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('realtekrealty:login')
  else:
    return render(request, 'realtekrealty/login.html')

def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('realtekrealty:login')
  
  
def vhse(request):
  vids=z.objects.all()
  return render(request,"realtekrealty/vids.html",{"vids":vids})
    
def search(request):
  if request.method=="POST":
    search=request.POST["search"]
    searche=z.objects.filter(htp=search)
    return render(request,"realtekrealty/search.html",{"search":search,"searche":searche})
  else:
    return render(request,"realtekrealty/search.html")
    
def dashboard(request):
  return redirect("realtekrealty:index")
    

# Create your views here.

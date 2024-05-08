from django.shortcuts import render,redirect
from insta_clone_app.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from insta_clone_app.models import *
from django.contrib.auth.decorators import login_required
from insta_clone_app.forms import *

# Create your views here.
# from django.urls import reverse_lazy
@login_required(login_url='index')
def index(request):
    pname=Photo.objects.all()
    return render(request,'index.html',{'p':pname})


@login_required(login_url='index')
def home(request):    
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        user=User.objects.filter(username=username)
        if  password1!=password2:
            messages.info(request,'Password confirmaton wrong!!')
            return redirect('register')
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('register')
        c = User.objects.create_user(username=username,password=password1)
        c.save()
        messages.info(request,'Account created successfully')
        return redirect("register")
    
    return render(request,'register.html')
        
        
        
def login_main(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'user do not exist')
            return redirect('index')
        else:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')


def logout_main(request):
    logout(request)
    return redirect('index')


@login_required(login_url='index')

def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PhotoForm()
    photos = Photo.objects.all()
    return render(request, 'upload.html', {'form': form, 'photos': photos})
        
        
        
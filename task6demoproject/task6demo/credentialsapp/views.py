from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        name=request.POST['username']
        first=request.POST['first_name']
        last=request.POST['last_name']
        mail=request.POST['e-mail']
        password=request.POST['password']
        password1=request.POST['password_again']
        if password==password1:
            if User.objects.filter(username=name).exists():
                messages.info(request,"Username Laready Taken")
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                messages.info(request,"Mail id Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=name,first_name=first,last_name=last,email=mail,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

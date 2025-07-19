from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.

def register(request):
    if request.method == "POST":
        fullName = request.POST["fullName"]
        email = request.POST["eMail"]
        passw = request.POST["passw"]
        con_passw = request.POST["con_passw"]
        
        print(fullName, email, passw, con_passw)
        
        if passw != con_passw:
            return HttpResponse("<script>alert('❌ Password and Confirm Password do not match!'); window.history.back();</script>")

        if User.objects.filter(username=fullName).exists():
            return HttpResponse("<script>alert('⚠️ Username already exists!'); window.history.back();</script>")
        
        new_user = User.objects.create(
            username = fullName,
            email = email,
            password = passw,
        )
        new_user.set_password(passw)
        new_user.save()
        return redirect("/Accounts/Login")
    return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        fullName = request.POST['fullName']
        passw = request.POST['passw']
        
        user = auth.authenticate(
            username = fullName,
            password = passw
        )
        
        if user is None:
            return HttpResponse("<script>alert(' 😊 Please Register First!'); window.history.back();</script>")
        else:
            auth.login(request, user)
            return redirect("/")
    return render(request, "accounts/login.html")

def logout(request):
    auth.logout(request)
    return redirect("/Accounts/Login")
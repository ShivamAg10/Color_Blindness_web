from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    user = request.user
    parameter = {
        "user" : user,
    }
    return render(request, "home/homepage.html", parameter)
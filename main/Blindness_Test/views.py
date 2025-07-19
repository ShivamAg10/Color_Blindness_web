from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/Accounts/Login")
def test(request):
    return render(request, "Blindness_Test/test.html")

@login_required(login_url="/Accounts/Login")
def quiz(request):
    return render(request, "Blindness_Test/quiz.html")
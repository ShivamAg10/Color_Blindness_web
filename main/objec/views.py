from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/Accounts/Login")
def object(request):
    return render(request, "objec/object.html")
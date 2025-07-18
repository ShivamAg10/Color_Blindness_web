from django.shortcuts import render

# Create your views here.

def object(request):
    return render(request, "objec/object.html")
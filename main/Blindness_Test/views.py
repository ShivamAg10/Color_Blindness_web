from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "Blindness_Test/test.html")

def quiz(request):
    return render(request, "Blindness_Test/quiz.html")
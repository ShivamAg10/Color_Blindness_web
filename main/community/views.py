from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Experience
from django.contrib.auth.models import User


# @login_required(login_url='/Accounts/Login')
def community(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        print(request.user.username)
        print(request.user)
        if content:
            if request.user.is_authenticated:
                Experience.objects.create(user=request.user.username, content=content)
            else:
                Experience.objects.create(user="Unknown", content=content)
            return redirect('community')

    experiences = Experience.objects.all().order_by('-created_at')
    return render(request, 'community/community.html', {'experiences': experiences})

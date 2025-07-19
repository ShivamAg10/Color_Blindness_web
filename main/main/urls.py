from django.contrib import admin
from django.urls import path, include
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
    path("Accounts/", include('Accounts.urls')),
    path("Blindness_Test/", include('Blindness_Test.urls')),
    path("object/", include('objec.urls')),
]

'''
    username: shivamag_10
    password: shivamag_10
'''
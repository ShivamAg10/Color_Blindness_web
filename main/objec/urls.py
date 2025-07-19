# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path("", views.object, name="object"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.object, name='object'),
    path('video_feed/', views.original_feed, name='original_feed'),
    path('simulated_feed/', views.simulated_feed, name='simulated_feed'),
    path('video_feed/', views.video_feed, name='video_feed'),
]

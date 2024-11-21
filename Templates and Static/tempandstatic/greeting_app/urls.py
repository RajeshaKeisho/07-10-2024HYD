from django.urls import path 
from . import views

urlpatterns = [
    path('wish/', views.wish),
    path('wish1/', views.wish1),
    path('greet/', views.greet),
]
from django.urls import path 
from . import views
urlpatterns = [
    path('empdata/', views.employeeview),
]
from django.urls import path 
from . import views
urlpatterns = [
    path("filters/", views.filter_view),
]
from django.urls import path 
from . import views 
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('author/<int:author_id>/books/', views.author_books, name='author_books'),
    path('nested/', views.nested_relationship, name='nested_relationship'),
]
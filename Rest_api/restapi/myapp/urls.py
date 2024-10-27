# urls.py
from django.urls import path
from .views import book_list_create_view, book_delete_view

urlpatterns = [
    path('books/', book_list_create_view, name='book-list-create'),
    path('books/<int:pk>/', book_delete_view, name='book-delete'),
]

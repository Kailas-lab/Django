# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/<str:title>/', views.book_detail, name='book_detail'),
    path('book/edit/<str:title>/', views.book_update, name='book_update'),
    path('book/delete/<str:title>/', views.book_delete, name='book_delete'),
]

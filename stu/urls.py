from django.contrib import admin
from django.urls import path
from  . import  views
urlpatterns = [
   path('create_users/', views.create_users, name='create_users'),
   path('delete_users/', views.delete_users, name='delete_users')
]
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  path('',views.add_singer,name='add_singer'),
  path('edit/<int:id>',views.edit_singer,name='edit_singer'),
  path('delete/<int:id>',views.delete_singer,name='delete_singer')
    
]
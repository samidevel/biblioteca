from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('autor/', views.ListAutores.as_view(), name="autores"),
]

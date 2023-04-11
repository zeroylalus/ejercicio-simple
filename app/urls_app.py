from django.contrib import admin
from django.urls import path
from app import views 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista, name='lista'),
    path('lista_d/<int:id>', views.lista_d, name='lista_d'),
    path('formulario/', views.formulario, name='formulario'),
]
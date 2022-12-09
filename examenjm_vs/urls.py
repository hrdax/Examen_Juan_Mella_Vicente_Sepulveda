from django.urls import path
from . import views

urlpatterns = [
    path('filtrosectores', views.filtrosectores, name='filtrosectores'),
    path('index', views.index, name='index'),
]

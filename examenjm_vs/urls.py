from django.urls import path
from .import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('crearcliente', views.crearcliente, name='crearcliente'),
    path('listadoclientes', views.verclientes, name='verclientes'),
    path('listadoclientes_ac', views.verclientes_activos, name='verclientes_ac'),
    
]

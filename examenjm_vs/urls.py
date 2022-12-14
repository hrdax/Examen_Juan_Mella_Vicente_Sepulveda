from django.urls import path
from .import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('cerrarsesion', views.cerrarsesion, name='cerrarsesion'),
    path('clientedashboard', views.clientedashboard, name='clientedashboard'),
    path('filtrosectores', views.filtrosectores, name='filtrosectores'),
    path('', views.vlogin, name='vlogin'),
    path('login', views.login, name='login'),
    path('crearcliente', views.crearcliente, name='crearcliente'),
    path('vcrearcliente', views.vcrearcliente, name='vcrearcliente'),
    path('listadoclientes', views.verclientes, name='verclientes'),
    path('listadoclientes_ac', views.verclientes_activos, name='verclientes_ac'),
    path('listadoclientes_inac', views.verclientes_inactivos, name='verclientes_inac'),
    path('vmodificarcliente', views.vmodificarcliente, name='vmodificarcliente'),
    path('modificarcliente', views.modificarcliente, name='modificarcliente'),
    path('filtrarsector', views.filtrarsector, name='filtrarsector'),
    path('verallclientes', views.verallclientes, name='verallclientes'),
    path('filtrarall', views.filtrarall, name='filtrarall'),
    path('Pagos', views.Pagos, name='Pagos'),
    path('webpay', views.webpay, name='webpay'),
    path('transaccioncompleta', views.transaccioncompleta, name='transaccioncompleta'),
    path('VerCuentas', views.VerCuentas, name='VerCuentas'),
    path('HistorialPagos', views.HistorialPagos, name='HistorialPagos'),
    path('vcrearcuenta', views.vcrearcuenta, name='vcrearcuenta'),
    path('crearcuenta', views.crearcuenta, name='crearcuenta'),
]

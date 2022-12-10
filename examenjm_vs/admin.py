from django.contrib import admin
from examenjm_vs.models import *
# Register your models here.


class Usuariodisplay(admin.ModelAdmin):
    #ver clientes
    list_display = ("Nombre","Contrasena","Rol")
    #buscar clientes
    search_fields = ("Nombre",)
    #filtrar
    list_filter = ("Nombre","Contrasena","Rol",)

class Clientedisplay(admin.ModelAdmin):
    #ver clientes
    list_display = ("Rut","Nombre","Apellido","sector","estado")
    #buscar clientes
    search_fields = ("Rut","Nombre","Apellido","sector","estado",)
    #filtrar
    list_filter = ("Rut","Nombre","Apellido","sector","estado",)

class Cuentadisplay(admin.ModelAdmin):
    #ver clientes
    list_display = ("Codigo","NombreAS","Monto","Token")
    #buscar clientes
    search_fields = ("Codigo","NombreAS","Monto","Token",)
    #filtrar
    list_filter = ("Codigo","NombreAS","Monto","Token",)

class Historialdepagosdisplay(admin.ModelAdmin):
    #ver clientes
    list_display = ("Codigo","NombreAS","Monto","Estado","Token")
    #buscar clientes
    search_fields = ("Codigo","NombreAS","Monto","Estado","Token",)
    #filtrar
    list_filter = ("Codigo","NombreAS","Monto","Estado","Token",)


admin.site.register(Cliente,Clientedisplay)
admin.site.register(Cuenta,Cuentadisplay)
admin.site.register(Historialdepagos,Historialdepagosdisplay)
admin.site.register(Usuario,Usuariodisplay)
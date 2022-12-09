from django.shortcuts import render
from examenjm_vs.models import *

# Create your views here.

def index(request):

    return render(request, 'dashboard.html')

def filtrosectores(request):
    return render(request, 'filtroporsectores.html')

def crearcliente(request):
   rutclient = request.POST['rutid']
   nameclient = request.POST['nombreid']
   apellidoclient = request.POST['apellidoid']
   sectorcliente = request.POST['sectorid']
   estadoclient = request.POST['estadoid'] 
   clientenew = Cliente(Rut=rutclient,Nombre=nameclient,Apellido=apellidoclient,sector=sectorcliente,estado=estadoclient)
   clientenew.save()
   return render(request,'index.html')

 
def verclientes(request):
    clientes = Cliente.objects.all
    return render(request, "listadoclientes.html",{"clientes":clientes})

def verclientes_activos(request):
    clientes = Cliente.objects.all().filter(estado="activo")
    return render(request, "listadoclientes.html",{"clientes":clientes})
    return render(request, "listadoclientes.html",{"clientes":clientes})

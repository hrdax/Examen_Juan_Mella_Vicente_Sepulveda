from django.shortcuts import render
from examenjm_vs.models import *

# Create your views here.

def index(request):
    sectores = ['Colbún','Panimávida','Maule Sur','La Guardia','San Nicolas','Quinamavida','Rari','Capilla Palacio']
    estados = ['activo','inactivo']
    return render(request, 'index.html',{'sector':sectores, 'estado':estados})

def crearcliente(request):
   rutclient = request.POST['rutid']
   nameclient = request.POST['nombreid']
   apellidoclient = request.POST['apellidoid']
   sectorcliente = request.POST['sectorid']
   estadoclient = request.POST['estadoid'] 
   clientenew = Cliente(Rut=rutclient,Nombre=nameclient,Apellido=apellidoclient,sector=sectorcliente,estado=estadoclient)
   clientenew.save()
   return render(request,'index.html')
 
 
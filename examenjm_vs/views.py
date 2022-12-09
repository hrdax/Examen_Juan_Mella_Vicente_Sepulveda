from django.shortcuts import render
from examenjm_vs.models import *

# Create your views here.

sectores=["Colbún"
    ,"Panimávida"
    ,"Maule Sur"
    ,"La Guardia"
    ,"San Nicolas"
    ,"Quinamavida"
    ,"Rari",
    "Capilla Palacio"]

estados=["activo","inactivo"]

# NO TOCAR INDEX
def index(request):
    return render(request, 'dashboard.html')

def vcrearcliente(request):
    return render(request, 'vcrearcliente.html',{"sector":sectores,"estado":estados})

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
   return render(request,'dashboard.html')

 
def verclientes(request):
    clientes = Cliente.objects.all
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores})

def verclientes_activos(request):
    clientes = Cliente.objects.all().filter(estado="activo")
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":'activo'})
    
def verclientes_inactivos(request):
    clientes = Cliente.objects.all().filter(estado="inactivo")
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":'inactivo'})
    
def vmodificarcliente(request):
    rutclient = request.GET['rut']
    cliente = Cliente.objects.get(Rut=rutclient)

    return render(request,'modificarcliente.html',{"cliente":cliente,"sector":sectores,"estado":estados})

def modificarcliente(request):
   rutclient = request.POST['rutid']
   nameclient = request.POST['nombreid']
   apellidoclient = request.POST['apellidoid']

   try:
       sectorcliente = request.POST['sectorid']
       
   except:
       sectorcliente = ""
        
   try:
       estadoclient = request.POST['estadoid']
   except:
       estadoclient = ""

   cliente = Cliente.objects.get(Rut=rutclient)

   cliente.Nombre = nameclient
   cliente.Apellido = apellidoclient

   if sectorcliente == "" and estadoclient == "":
        None
   elif estadoclient == "" and sectorcliente != "":
        cliente.sector = sectorcliente
   elif sectorcliente == "" and estadoclient != "":
        cliente.estado = estadoclient
   else:
        cliente.sector = sectorcliente
        cliente.estado = estadoclient
        
        
   cliente.save()

   return render(request,'dashboard.html')

def filtrarsector(request):
    estado = request.POST['estadoid']

    try:
        sector = request.POST['sectorid']
        clientes = Cliente.objects.all().filter(sector=sector,estado=estado)
        return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})
    except:
        
        clientes = Cliente.objects.all().filter(estado=estado)
        return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})

    
    

def verallclientes(request):
    clientes = Cliente.objects.all
    return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})


def filtrarall(request):
    sectorse = request.POST['sectorid']
    estadose = request.POST['estadoid']

    if sectorse == "Cualquier Sector" and estadose == "Cualquier Estado":
        clientes = Cliente.objects.all()
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})
    elif estadose == "Cualquier Estado":
        clientes = Cliente.objects.all().filter(sector=sectorse)
        return render(request, "Verclientes.html",{"clientes":clientes,"estado":estados,"sector":sectores})
    elif sectorse == "Cualquier Sector":
        clientes = Cliente.objects.all().filter(estado=estadose)
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})
    else:
        clientes = Cliente.objects.all().filter(sector=sectorse,estado=estadose)
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})

 
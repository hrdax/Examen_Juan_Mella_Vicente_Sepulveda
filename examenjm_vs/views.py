from django.shortcuts import render
from examenjm_vs.models import *

# Create your views here.

# lista secotres
sectores=["Colbún"
    ,"Panimávida"
    ,"Maule Sur"
    ,"La Guardia"
    ,"San Nicolas"
    ,"Quinamavida"
    ,"Rari",
    "Capilla Palacio"]

# lista estados
estados=["activo","inactivo"]

# NO TOCAR INDEX
def index(request):
    return render(request, 'dashboard.html')

def vcrearcliente(request):
    return render(request, 'vcrearcliente.html',{"sector":sectores,"estado":estados})

def filtrosectores(request):
    return render(request, 'filtroporsectores.html')

def crearcliente(request):
    #guarda los datos del formulario desde el POST
   rutclient = request.POST['rutid']
   nameclient = request.POST['nombreid']
   apellidoclient = request.POST['apellidoid']
   sectorcliente = request.POST['sectorid']
   estadoclient = request.POST['estadoid']
   #crea un objeto cliente con los datos del formulario 
   clientenew = Cliente(Rut=rutclient,Nombre=nameclient,Apellido=apellidoclient,sector=sectorcliente,estado=estadoclient)
   #guarda el objeto cliente en la base de datos
   clientenew.save()
   #redirecciona a la pagina de inicio
   return render(request,'dashboard.html')

 
def verclientes(request):
    #obtiene todos los clientes de la base de datos
    clientes = Cliente.objects.all
    #renderiza la pagina de listado de clientes y le pasa los clientes
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores})

def verclientes_activos(request):
    #obtiene todos los clientes de la base de datos que esten activos
    clientes = Cliente.objects.all().filter(estado="activo")
    #renderiza la pagina de listado de clientes y le pasa los clientes
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":'activo'})
    
def verclientes_inactivos(request):
    #obtiene todos los clientes de la base de datos que esten inactivos
    clientes = Cliente.objects.all().filter(estado="inactivo")
    return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":'inactivo'})
    
def vmodificarcliente(request):
    #obtiene el rut del cliente a modificar mediante el metodo GET
    rutclient = request.GET['rut']
    #obtiene el cliente a modificar
    cliente = Cliente.objects.get(Rut=rutclient)

    return render(request,'modificarcliente.html',{"cliente":cliente,"sector":sectores,"estado":estados})

def modificarcliente(request):
    #obtiene los datos del formulario
   rutclient = request.POST['rutid']
   nameclient = request.POST['nombreid']
   apellidoclient = request.POST['apellidoid']
    #intenta obtener el sector sino, significa que este estaba vacio
   try:
       sectorcliente = request.POST['sectorid']
       
   except:
    #asigna el sectorcliente como vacio
       sectorcliente = ""
        
   try:
    #intenta obtener el estado sino, significa que este estaba vacio
       estadoclient = request.POST['estadoid']
   except:
    #asigna el estadoclient como vacio
       estadoclient = ""
    #obtiene el cliente con el rut
   cliente = Cliente.objects.get(Rut=rutclient)

    #modifica el nombre y apellido
   cliente.Nombre = nameclient
   cliente.Apellido = apellidoclient

    #verifica si el sector y el estado estan vacios, si es asi, no modifica nada en esos campos
   if sectorcliente == "" and estadoclient == "":
        None
    #verifica si solo el estado esta vacio, si es asi, solo modifica el sector
   elif estadoclient == "" and sectorcliente != "":
        cliente.sector = sectorcliente
    #verifica si solo el sector esta vacio, si es asi, solo modifica el estado
   elif sectorcliente == "" and estadoclient != "":
        cliente.estado = estadoclient
    #si ninguno esta vacio, modifica ambos
   else:
        cliente.sector = sectorcliente
        cliente.estado = estadoclient
        
    #guarda los cambios en la base de datos
   cliente.save()

   return render(request,'dashboard.html')

def filtrarsector(request):
    #obtiene el estado 
    estado = request.POST['estadoid']

    try:
        #intenta obtener el sector, si no, significa que este estaba vacio
        sector = request.POST['sectorid']
        #filtra los clientes por el sector y el estado
        clientes = Cliente.objects.all().filter(sector=sector,estado=estado)
        return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":estado})
    except:
        
        #filtra los clientes por el estado
        clientes = Cliente.objects.all().filter(estado=estado)
        return render(request, "listadoclientes.html",{"clientes":clientes,"sector":sectores,"estado":estado})

    
    

def verallclientes(request):
    clientes = Cliente.objects.all
    return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})


def filtrarall(request):
    #obtiene el sector y el estado
    sectorse = request.POST['sectorid']
    estadose = request.POST['estadoid']

    #verifica si el sector y el estado son "Cualquier Sector" y "Cualquier Estado" respectivamente
    if sectorse == "Cualquier Sector" and estadose == "Cualquier Estado":
        #si es asi, muestra todos los clientes
        clientes = Cliente.objects.all()
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})
    #verifica si el estado es "Cualquier Estado"
    elif estadose == "Cualquier Estado":
        #si es asi, muestra todos los clientes con el sector seleccionado
        clientes = Cliente.objects.all().filter(sector=sectorse)
        return render(request, "Verclientes.html",{"clientes":clientes,"estado":estados,"sector":sectores})
    #verifica si el sector es "Cualquier Sector"
    elif sectorse == "Cualquier Sector":
        #si es asi, muestra todos los clientes con el estado seleccionado
        clientes = Cliente.objects.all().filter(estado=estadose)
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})
    else:
        #si ninguno esta por default, muestra todos los clientes con el sector y el estado seleccionado
        clientes = Cliente.objects.all().filter(sector=sectorse,estado=estadose)
        return render(request, "Verclientes.html",{"clientes":clientes,"sector":sectores,"estado":estados})

 
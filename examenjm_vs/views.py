from django.shortcuts import render
from examenjm_vs.models import *
from random import randint
from transbank.webpay.webpay_plus.transaction import Transaction


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

def clientedashboard(request):

    user = request.GET['user']

    return render(request, 'clientedashboard.html',{"user":user})

def cerrarsesion(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def vlogin(request):
    return render(request, 'login.html')

def login(request):
    #obtiene el nombre de usuario y la contraseña desde el formulario
    user = request.POST['user']
    password = request.POST['pass']

    try :
        #obtiene el usuario de la base de datos
        usuario = Usuario.objects.get(Nombre=user)
        
    except:
        return render(request,'login.html', {'message':'Usuario o contraseña incorrectos'})

    if user == usuario.Nombre and password == usuario.Contrasena and usuario.Rol == 1:
            return render(request, 'dashboard.html')
    elif user == usuario.Nombre and password == usuario.Contrasena and usuario.Rol == 2:

        return render(request, 'clientedashboard.html',{"user":user})
    else:
        return render(request,'login.html', {'message':'Usuario o contraseña incorrectos'})

def vcrearcliente(request):
    usuarios = Usuario.objects.filter(Rol=2)
    return render(request, 'vcrearcliente.html',{"sector":sectores,"estado":estados,"usuarios":usuarios})

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

def Pagos(request):
    #hace un select a todos los clientes
    clientes = Cliente.objects.all()
    #envia todos los clientes al spinner de pago
    return render(request, "Pagos.html",{"ruts":clientes})

#crea la transaccion y redirige en caso de exito
def webpay(request):
    #obtiene el rut y el monto a pagar
    ccodigo = request.GET['Codigo']

    cuenta = Cuenta.objects.get(Codigo=ccodigo)

    #crea la transaccion
    resp = (Transaction()).create(str(randint(10,100000)), str(randint(10,100000)), float(cuenta.Monto), "http://localhost:8000/examenjm_vs/transaccioncompleta")

    cuenta.Token = resp['token']
    cuenta.save()


    #redirige a confirmar pago donde evia el monto a pagar tambien la url y el token devuelto por parte de transbank
    return render(request, "confirmarpago.html",{"token":resp['token'], "url":resp['url'], "cuenta":cuenta,"user":cuenta.NombreAS})

#redirige a la pagina de pago realizado en caso de se haya hecho el pago con un N de transaccion aleatorio
def transaccioncompleta(request):

    token = request.GET['token_ws']

    cuenta = Cuenta.objects.get(Token=token)

    phistorial = Historialdepagos(Codigo=cuenta.Codigo,NombreAS=cuenta.NombreAS,Monto=cuenta.Monto,Estado="Pagado",Token=token)
    phistorial.save()

    phistorial = Historialdepagos.objects.filter(NombreAS=cuenta.NombreAS)
    cuenta.delete()

    
    for phistorial in phistorial:

        user = phistorial.NombreAS

    return render(request, "pagorealizado.html",{ "TBK_NUM_TRANSACCION": randint(30,1000000), "user":user})

def VerCuentas(request):
    
    user = request.GET['user']

    cuenta = Cuenta.objects.filter(NombreAS=user)
    #envia todos los clientes al spinner de pago
    return render(request, "VerCuentas.html",{"cuentas":cuenta,"user":user})

def HistorialPagos(request):
    user = request.GET['user']
    #hace un select a todos los clientes
    hpago = Historialdepagos.objects.filter(NombreAS=user)
    #envia todos los clientes al spinner de pago
    return render(request, "HistorialPagos.html",{"hpagos":hpago,"user":user})

def vcrearcuenta(request):
    clientes = Cliente.objects.all()
    return render(request, "crearcuenta.html",{"clientes":clientes})

def crearcuenta(request):

    try:
        clientes = Cliente.objects.all()
        codigo = randint(10,100000)
        nombre = request.POST['nombre']
        monto = request.POST['monto']

        cuenta = Cuenta(Codigo=codigo,NombreAS=nombre,Monto=monto,Token="")
        cuenta.save()
        return render(request, "crearcuenta.html",{"clientes":clientes,"message":"Cargo monetario creado con exito"})
    except:
        return render(request, "crearcuenta.html",{"message","Error al crear la cuenta"})


    

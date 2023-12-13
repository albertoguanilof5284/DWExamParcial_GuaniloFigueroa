from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import tienda
from .models import producto

listaTiendas = []
listaProductos = []

# Create your views here.

def index(request):
    return HttpResponse("Bienvenidos a django")

def productos(request):
     return render(request,'productos.html',{
         'listaProductos':producto.objects.all()
         })


def tiendas(request):
    return render(request,'tiendas.html',{
         'listaTiendas':tienda.objects.all()
         })

def agregarTienda(request):
    print(request.POST)

    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        provincia = request.POST.get('provincia')
        region = request.POST.get('region')
        fechaCreacion = request.POST.get('fechaCreacion')
        telefono = request.POST.get('telefono')
        print(direccion)
        print(provincia)

        tienda.objects.create(
            direccion = direccion,
            provincia = provincia,
            region = region,
            fechaCreacion = fechaCreacion,
            telefonoContacto = telefono
        )

        return HttpResponseRedirect(reverse('gestionTienda:tiendas'))
    return render(request,'agregarTienda.html')

def agregarProducto(request):
     if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precioVenta = request.POST.get('precioVenta')
        cantidad = request.POST.get('cantidad')
       
        producto.objects.create(
            descripcion = descripcion,
            codigo = codigo,
            precioVenta = precioVenta,
            cantidad = cantidad,
        )

        return HttpResponseRedirect(reverse('gestionTienda:productos'))
     return render(request,'agregarProducto.html')

def editarProducto(request,idProducto):
    objProducto = producto.objects.get(id=idProducto)
    return render(request,'editarProducto.html',{
        'objProducto':objProducto, 'listaTiendas':tienda.objects.all()
    })

def saveProducto(request):
    
     codigo = request.POST['id']

     print(f'valor {{% codigo %}}')
     tienda = request.POST['tienda']
     Producto = producto.objects.get(id=codigo)

     Producto.tiendaRelacionada = tienda
     Producto.save()
     return HttpResponseRedirect(reverse('gestionTienda:productos'))


def eliminarProducto(request,idProducto):
    Producto = producto.objects.get(id=idProducto)
    Producto.delete()

    return HttpResponseRedirect(reverse('gestionTienda:productos'))

def eliminarTienda(request,idTienda):
    Tienda = tienda.objects.get(id=idTienda)
    Tienda.delete()

    return HttpResponseRedirect(reverse('gestionTienda:tiendas'))

def detalleTienda(request,idTienda):
    objProducto = producto.objects.get(id=idTienda)
    return render(request,'detalleTienda.html',{
        'objProducto':objProducto
    })





# Ruta: 127.1.1.0:800/gestionTienda
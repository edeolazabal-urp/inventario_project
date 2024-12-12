from django.shortcuts import render, redirect
from .models import Producto

# Create your views here.
def home(request):
    productos = Producto.objects.all()
    return render(request, 'gestionProductos.html', {"productos": productos}) 

def registrarProducto(request):
    id = request.POST.get('id')
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    marca = 'marca'
    cantidad_min = 0
    cantidad_max = request.POST.get('cantidad_max')
    precio = request.POST.get('precio')
    if id:
        producto = Producto.objects.get(id=id)
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.marca = marca
        producto.cantidad_min = cantidad_min
        producto.cantidad_max = cantidad_max
        producto.precio = precio
        producto.save()
    else:
        producto = Producto.objects.create(nombre=nombre, descripcion=descripcion, marca=marca, cantidad_min=cantidad_min, cantidad_max=cantidad_max, precio=precio)
    return redirect('/')

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/') 

def editarProducto(request, id):
    producto = Producto.objects.get(id=id)
    accion = "Edición"
    return render(request, 'editarProducto.html', {"producto": producto, "accion": accion})

def adicionarProducto(request):
    producto = None
    accion = "Adición"
    return render(request, 'editarProducto.html', {"producto": producto, "accion": accion})


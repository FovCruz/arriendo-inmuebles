from django.shortcuts import render, redirect
from .models import Vivienda, Propietario

def crear_vivienda(request):
    if request.method == 'POST':
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        precio = request.POST['precio']
        propietario_id = request.POST['propietario_id']
        propietario = Propietario.objects.get(id=propietario_id)
        nueva_vivienda = Vivienda(direccion=direccion, ciudad=ciudad, precio=precio, propietario=propietario)
        nueva_vivienda.save()
        return redirect('listar_viviendas')
    else:
        propietarios = Propietario.objects.all()
        return render(request, 'crear_vivienda.html', {'propietarios': propietarios})

def listar_viviendas(request):
    viviendas = Vivienda.objects.all()
    return render(request, 'listar_viviendas.html', {'viviendas': viviendas})

def actualizar_vivienda(request, id):
    vivienda = Vivienda.objects.get(id=id)
    propietarios = Propietario.objects.all()

    if request.method == 'POST':
        vivienda.direccion = request.POST['direccion']
        vivienda.ciudad = request.POST['ciudad']
        vivienda.precio = request.POST['precio']
        vivienda.propietario_id = request.POST['propietario_id']
        vivienda.save()
        return redirect('listar_viviendas')

    return render(request, 'actualizar_vivienda.html', {'vivienda': vivienda, 'propietarios': propietarios})

def eliminar_vivienda(request, id):
    vivienda = Vivienda.objects.get(id=id)
    vivienda.delete()
    return redirect('listar_viviendas')


# Create your views here.
def crear_propietario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        nuevo_propietario = Propietario(nombre=nombre, correo=correo)
        nuevo_propietario.save()
        return redirect('listar_propietarios')
    return render(request, 'crear_propietario.html')

def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'listar_propietarios.html', {'propietarios': propietarios})

def actualizar_propietario(request, id):
    propietario = Propietario.objects.get(id=id)
    if request.method == 'POST':
        propietario.nombre = request.POST['nombre']
        propietario.correo = request.POST['correo']
        propietario.save()
        return redirect('listar_propietarios')
    return render(request, 'actualizar_propietario.html', {'propietario': propietario})

def eliminar_propietario(request, id):
    propietario = Propietario.objects.get(id=id)
    propietario.delete()
    return redirect('listar_propietarios')

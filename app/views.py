from django.shortcuts import render, redirect
from .models import Propietario

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

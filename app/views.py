from django.shortcuts import render, redirect
from .models import Vivienda, Propietario, Comuna, Region,TipoInmueble
from django.http import JsonResponse
from django.template.loader import render_to_string

def crear_vivienda(request):
    if request.method == 'POST':
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        precio = request.POST['precio']
        propietario_id = request.POST['propietario_id']
        comuna_id = request.POST['comuna_id']
        tipo_inmueble_id = request.POST['tipo_inmueble_id']

        propietario = Propietario.objects.get(id=propietario_id)
        comuna = Comuna.objects.get(id=comuna_id)
        tipo_inmueble = TipoInmueble.objects.get(id=tipo_inmueble_id)

        nueva_vivienda = Vivienda(
            direccion=direccion, 
            ciudad=ciudad, 
            precio=precio, 
            propietario=propietario, 
            comuna=comuna,
            tipo_inmueble=tipo_inmueble  # Guardar el tipo de inmueble
        )
        nueva_vivienda.save()
        return redirect('listar_viviendas')
    else:
        propietarios = Propietario.objects.all()
        regiones = Region.objects.all()
        tipos_inmuebles = TipoInmueble.objects.all()  # Obtener todos los tipos de inmuebles

        return render(request, 'crear_vivienda.html', {
            'propietarios': propietarios,
            'regiones': regiones,
            'tipos_inmuebles': tipos_inmuebles  # Pasar los tipos de inmuebles al template
        })



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

def listar_inmuebles_por_comuna(request):
    inmuebles = Vivienda.objects.select_related('comuna').all()
    return render(request, 'listar_inmuebles_comunas.html', {'inmuebles': inmuebles})

def load_comunas(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    return render(request, 'comuna_dropdown_list_options.html', {'comunas': comunas})

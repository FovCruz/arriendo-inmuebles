from django.shortcuts import render, redirect, get_object_or_404
from .models import Vivienda, Propietario, Comuna, Region, TipoInmueble, Arrendatario
from django.http import JsonResponse
from .forms import LoginForm, RegistroForm, ModificarPerfilForm, ArrendatarioForm, PropietarioForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


def home(request):
    return render(request, 'home.html')


@login_required
def propietarios_home(request):
    return render(request, 'propietarios/home.html')

@login_required
def arrendatarios_home(request):
    return render(request, 'arrendatarios/home.html')


def mi_vista(request):
    es_propietario = request.user.groups.filter(name='Propietario').exists() if request.user.is_authenticated else False
    es_arrendatario = request.user.groups.filter(name='Arrendatario').exists() if request.user.is_authenticated else False

    context = {
        'es_propietario': es_propietario,
        'es_arrendatario': es_arrendatario,
    }
    return render(request, 'mi_template.html', context)


@login_required
def modificar_arrendatario(request, id):
    arrendatario = get_object_or_404(Arrendatario, id=id)
    if request.method == 'POST':
        form = ArrendatarioForm(request.POST, instance=arrendatario)
        if form.is_valid():
            form.save()
            return redirect('perfil_arrendatario', id=arrendatario.id)
    else:
        form = ArrendatarioForm(instance=arrendatario)
    return render(request, 'arrendatarios/modificar_arrendatario.html', {'form': form})


@login_required
def modificar_propietario(request, id):
    propietario = get_object_or_404(Propietario, id=id)
    if request.method == 'POST':
        form = PropietarioForm(request.POST, instance=propietario)
        if form.is_valid():
            form.save()
            return redirect('perfil_propietario', id=propietario.id)
    else:
        form = PropietarioForm(instance=propietario)
    return render(request, 'propietarios/modificar_propietario.html', {'form': form})


@login_required
def perfil_view(request):
    es_propietario = request.user.groups.filter(name='Propietario').exists()
    es_arrendatario = request.user.groups.filter(name='Arrendatario').exists()
    
    return render(request, 'usuarios/perfil.html', {
        'user': request.user,
        'es_propietario': es_propietario,
        'es_arrendatario': es_arrendatario
    })


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            tipo_usuario = form.cleaned_data['tipo_usuario']
            
            # Asigna el grupo basado en la selección
            if tipo_usuario == 'propietario':
                group = Group.objects.get(name='Propietario')
            else:
                group = Group.objects.get(name='Arrendatario')
            
            user.groups.add(group)
            user.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


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

        return render(request, 'inmuebles/crear_vivienda.html', {
            'propietarios': propietarios,
            'regiones': regiones,
            'tipos_inmuebles': tipos_inmuebles  # Pasar los tipos de inmuebles al template
        })


def load_comunas(request):
    region_id = request.GET.get('region')
    comunas = Comuna.objects.filter(region_id=region_id).order_by('nombre')
    return render(request, 'inmuebles/comuna_dropdown_list_options.html', {'comunas': comunas})


def listar_viviendas(request):
    viviendas = Vivienda.objects.all()
    paginator = Paginator(viviendas, 4)  # Muestra 4 propietarios por página

    page_number = request.GET.get('page')
    viviendas = paginator.get_page(page_number)

    return render(request, 'inmuebles/listar_viviendas.html', {'viviendas': viviendas})


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

    return render(request, 'inmuebles/actualizar_vivienda.html', {'vivienda': vivienda, 'propietarios': propietarios})


def eliminar_vivienda(request, id):
    vivienda = Vivienda.objects.get(id=id)
    vivienda.delete()
    return redirect('listar_viviendas')


def crear_propietario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')  # Usar get para evitar errores si no se encuentra
        correo = request.POST.get('correo', '')  # Usar get para evitar errores si no se encuentra
        if nombre and correo:
            nuevo_propietario = Propietario(nombre=nombre, correo=correo)
            nuevo_propietario.save()
            return redirect('listar_propietarios')
        else:
            # Manejar el caso en el que falta algún campo
            error_message = "Por favor, complete todos los campos."
            return render(request, 'propietarios/crear_propietario.html', {'error_message': error_message})
    return render(request, 'propietarios/crear_propietario.html')


def listar_propietarios(request):
    propietarios_list = Propietario.objects.all()
    paginator = Paginator(propietarios_list, 4)  # Muestra 4 propietarios por página

    page_number = request.GET.get('page')
    propietarios = paginator.get_page(page_number)

    return render(request, 'propietarios/listar_propietarios.html', {'propietarios': propietarios})


def actualizar_propietario(request, id):
    propietario = Propietario.objects.get(id=id)
    if request.method == 'POST':
        propietario.nombre = request.POST['nombre']
        propietario.correo = request.POST['correo']
        propietario.save()
        return redirect('listar_propietarios')
    return render(request, 'propietarios/actualizar_propietario.html', {'propietario': propietario})


def eliminar_propietario(request, id):
    propietario = Propietario.objects.get(id=id)
    propietario.delete()
    return redirect('listar_propietarios')


def listar_inmuebles_por_comuna(request):
    inmuebles_list = Vivienda.objects.select_related('comuna').all()
    paginator = Paginator(inmuebles_list, 4)  # Muestra 4 registros por página

    page_number = request.GET.get('page')
    inmuebles = paginator.get_page(page_number)

    return render(request, 'inmuebles/listar_inmuebles_comunas.html', {'inmuebles': inmuebles})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'usuarios/login.html', {'form': form})


@login_required
def modificar_perfil_view(request):
    if request.method == 'POST':
        form = ModificarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ModificarPerfilForm(instance=request.user)
    return render(request, 'usuarios/modificar_perfil.html', {'form': form})

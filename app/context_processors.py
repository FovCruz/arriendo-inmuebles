from django.contrib.auth.models import Group

def rol_usuario(request):
    if request.user.is_authenticated:
        es_propietario = request.user.groups.filter(name='Propietario').exists()
        es_arrendatario = request.user.groups.filter(name='Arrendatario').exists()
    else:
        es_propietario = False
        es_arrendatario = False

    return {
        'es_propietario': es_propietario,
        'es_arrendatario': es_arrendatario,
    }

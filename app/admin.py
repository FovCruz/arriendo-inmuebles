from django.contrib import admin
from .models import Propietario, Vivienda, Arrendatario, Arriendo

# Register your models here.
admin.site.register(Propietario)
admin.site.register(Vivienda)
admin.site.register(Arrendatario)
admin.site.register(Arriendo)

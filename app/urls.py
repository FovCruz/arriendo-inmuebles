from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_propietarios, name='listar_propietarios'),
    path('crear_usuario/', views.crear_propietario, name='crear_propietario'),
    path('actualizar_usuario/<int:id>/', views.actualizar_propietario, name='actualizar_propietario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
]

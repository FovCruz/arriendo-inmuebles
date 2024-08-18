from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_propietarios, name='listar_propietarios'),
    path('crear_usuario/', views.crear_propietario, name='crear_propietario'),
    path('actualizar_usuario/<int:id>/', views.actualizar_propietario, name='actualizar_propietario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
    path('viviendas/', views.listar_viviendas, name='listar_viviendas'),
    path('viviendas/crear/', views.crear_vivienda, name='crear_vivienda'),
    path('viviendas/actualizar/<int:id>/', views.actualizar_vivienda, name='actualizar_vivienda'),
    path('viviendas/eliminar/<int:id>/', views.eliminar_vivienda, name='eliminar_vivienda'),
]

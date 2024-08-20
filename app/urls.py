from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_propietario/', views.crear_propietario, name='crear_propietario'),
    path('actualizar_usuario/<int:id>/', views.actualizar_propietario, name='actualizar_propietario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_propietario, name='eliminar_propietario'),
    path('viviendas/', views.listar_viviendas, name='listar_viviendas'),
    path('viviendas/crear/', views.crear_vivienda, name='crear_vivienda'),
    path('viviendas/actualizar/<int:id>/', views.actualizar_vivienda, name='actualizar_vivienda'),
    path('viviendas/eliminar/<int:id>/', views.eliminar_vivienda, name='eliminar_vivienda'),
    path('inmuebles/comunas/', views.listar_inmuebles_por_comuna, name='listar_inmuebles_comunas'),
    path('ajax/load-comunas/', views.load_comunas, name='ajax_load_comunas'),
    path('login/', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/modificar/', views.modificar_perfil_view, name='modificar_perfil'),
    path('arrendatario/<int:id>/modificar/', views.modificar_arrendatario, name='modificar_arrendatario'),
    path('propietario/<int:id>/modificar/', views.modificar_propietario, name='modificar_propietario'),
    path('arrendatario/home/', views.arrendatarios_home, name='arrendatarios_home'),
    path('propietario/home/', views.propietarios_home, name='propietarios_home'),
    path('listar_propietarios/', views.listar_propietarios, name='listar_propietarios'),
]

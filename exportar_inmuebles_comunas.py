import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

django.setup()

from app.models import Vivienda
from django.db import connection

def exportar_inmuebles_por_comuna():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT c.nombre AS comuna, v.direccion, v.precio
            FROM app_vivienda v
            INNER JOIN app_comuna c ON v.comuna_id = c.id
            ORDER BY c.nombre;
        """)
        inmuebles = cursor.fetchall()

    with open('inmuebles_por_comuna.txt', 'w') as file:
        for inmueble in inmuebles:
            file.write(f"Comuna: {inmueble[0]}, Dirección: {inmueble[1]}, Precio: {inmueble[2]}\n")

if __name__ == "__main__":
    exportar_inmuebles_por_comuna()

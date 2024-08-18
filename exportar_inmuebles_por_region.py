import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
django.setup()

from app.models import Vivienda, Region
from django.db import connection

def exportar_inmuebles_por_region():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT r.nombre AS region, v.direccion, v.ciudad, v.precio, t.nombre AS tipo_inmueble
            FROM app_vivienda v
            INNER JOIN app_comuna c ON v.comuna_id = c.id
            INNER JOIN app_region r ON c.region_id = r.id
            INNER JOIN app_tipoinmueble t ON v.tipo_inmueble_id = t.id
            ORDER BY r.nombre, v.direccion;
        """)

        inmuebles_por_region = cursor.fetchall()

    # Guardar los resultados en un archivo de texto
    with open('inmuebles_por_region.txt', 'w') as file:
        current_region = None
        for row in inmuebles_por_region:
            region, direccion, ciudad, precio, tipo_inmueble = row
            if region != current_region:
                if current_region is not None:
                    file.write("\n")
                file.write(f"--- {region} ---\n")
                current_region = region
            file.write(f"Dirección: {direccion}, Ciudad: {ciudad}, Precio: {precio}, Tipo: {tipo_inmueble}\n")

if __name__ == "__main__":
    exportar_inmuebles_por_region()
    print("Exportación completada. Los resultados se han guardado en 'inmuebles_por_region.txt'.")

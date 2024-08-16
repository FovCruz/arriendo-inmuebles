from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Vivienda(models.Model):
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.direccion

class Arrendatario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    vivienda = models.ForeignKey(Vivienda, on_delete=models.CASCADE)
    arrendatario = models.ForeignKey(Arrendatario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f'Arriendo de {self.vivienda} por {self.arrendatario}'

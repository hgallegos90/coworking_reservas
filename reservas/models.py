from django.db import models

class Espacio(models.Model):
    TIPO_ESPACIO = [
        ('OF', 'Oficina'),
        ('SR', 'Sala de Reunión'),
    ]
    tipo = models.CharField(max_length=2, choices=TIPO_ESPACIO)
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Reserva(models.Model):
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=20, default='Activa')

    def __str__(self):
        return f"Reserva de {self.cliente} en {self.espacio} desde {self.fecha_inicio} hasta {self.fecha_fin}"
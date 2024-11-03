from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('crear_reserva/', views.crear_reserva, name='crear_reserva'),
    path('editar_reserva/', views.editar_reserva, name='editar_reserva'),
    path('eliminar_reserva/', views.eliminar_reserva, name='eliminar_reserva'),
    path('disponibilidad/', views.disponibilidad_espacios, name='disponibilidad_espacios'),
    path('reservas_activas/', views.reservas_activas, name='reservas_activas'),
]


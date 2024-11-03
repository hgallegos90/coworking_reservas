from django import forms
from .models import Reserva, Cliente, Espacio  # Asegúrate de importar Espacio

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_fin']  # Eliminado el campo 'cliente'
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'fecha_inicio': 'Fecha y hora de inicio',
            'fecha_fin': 'Fecha y hora de fin',
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'telefono': 'Teléfono',
        }

class EspacioForm(forms.ModelForm):
    class Meta:
        model = Espacio
        fields = ['tipo', 'nombre', 'capacidad', 'disponibilidad']
        labels = {
            'tipo': 'Tipo de Espacio',
            'nombre': 'Nombre del Espacio',
            'capacidad': 'Capacidad',
            'disponibilidad': 'Disponible',
        }
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del espacio'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
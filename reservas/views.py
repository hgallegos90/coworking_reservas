from django.shortcuts import render, get_object_or_404, redirect
from .models import Espacio, Cliente, Reserva
from .forms import ReservaForm, ClienteForm, EspacioForm
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    total_espacios = Espacio.objects.count()
    reservas_activas = Reserva.objects.filter(estado='Activa').count()
    
    # Evitar división por cero
    if total_espacios > 0:
        # Calcular porcentajes
        porcentaje_ocupado = (reservas_activas / total_espacios) * 100
        porcentaje_disponible = 100 - porcentaje_ocupado
    else:
        # Si no hay espacios, ambos porcentajes son 0
        porcentaje_ocupado = 0
        porcentaje_disponible = 0

    context = {
        'porcentaje_ocupado': round(porcentaje_ocupado, 2),
        'porcentaje_disponible': round(porcentaje_disponible, 2),
    }
    return render(request, 'reservas/inicio.html', context)

# Vista para visualizar la disponibilidad de espacios
def disponibilidad_espacios(request):
    # Filtrar espacios que no tienen reservas activas
    now = timezone.now()
    espacios_ocupados = Reserva.objects.filter(fecha_inicio__lte=now, fecha_fin__gte=now).values_list('espacio_id', flat=True)
    espacios_disponibles = Espacio.objects.exclude(id__in=espacios_ocupados)

    return render(request, 'reservas/disponibilidad.html', {
        'espacios': espacios_disponibles,
    })

# Vista para realizar una reserva
def crear_reserva(request):
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        
        if reserva_form.is_valid() and cliente_form.is_valid():
            # Guardar cliente y asociarlo a la reserva
            cliente = cliente_form.save()
            reserva = reserva_form.save(commit=False)
            reserva.cliente = cliente  # Asignar cliente guardado a la reserva
            
            # Agregar el espacio elegido (ejemplo con id de espacio)
            espacio_id = request.POST.get('espacio_id')
            reserva.espacio = Espacio.objects.get(id=espacio_id)
            reserva.estado = 'Activa'
            
            reserva.save()  # Guardar la reserva con el cliente asociado
            
            return redirect('inicio')  # Redirigir a inicio o reservas activas
    else:
        reserva_form = ReservaForm()
        cliente_form = ClienteForm()
        espacios = Espacio.objects.all()  # Obtener espacios para el dropdown

    return render(request, 'reservas/crear_reserva.html', {
        'reserva_form': reserva_form,
        'cliente_form': cliente_form,
        'espacios': espacios,  # Pasar espacios al template
    })

# Vista para editar una reserva existente
def editar_reserva(request):
    reservas = Reserva.objects.all()  # Obtiene todas las reservas

    if request.method == 'POST':
        reserva_id = request.POST.get('reserva_id')
        reserva = get_object_or_404(Reserva, id=reserva_id)
        form = ReservaForm(request.POST, instance=reserva)
        
        if form.is_valid():
            form.save()
            return redirect('editar_reserva')  # Redirige a la lista de reservas después de editar
    else:
        form = ReservaForm()  # Crea un formulario vacío si no se está editando

    return render(request, 'reservas/editar_reserva.html', {
        'reservas': reservas,
        'form': form,
    })

# Vista para eliminar una reserva
def eliminar_reserva(request):
    if request.method == 'POST':
        # Obtener IDs de reservas seleccionadas
        reservas_ids = request.POST.getlist('reservas_seleccionadas')
        
        # Eliminar las reservas seleccionadas
        Reserva.objects.filter(id__in=reservas_ids).delete()
        
        # Redirigir de vuelta a la misma página después de eliminar
        return redirect('eliminar_reserva')

    # Obtener todas las reservas para mostrarlas en la tabla
    reservas = Reserva.objects.all()

    return render(request, 'reservas/eliminar_reserva.html', {'reservas': reservas})

# Vista para mostrar las reservas activas
def reservas_activas(request):
    reservas = Reserva.objects.filter(estado='Activa')
    return render(request, 'reservas/reservas_activas.html', {'reservas': reservas})

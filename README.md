# Sistema de Reservas de Espacios de Coworking

Este es un proyecto académico desarrollado como parte de un concurso de programación de la Universidad UTEG. El sistema permite gestionar las reservas de espacios de coworking, proporcionando opciones para crear, editar y eliminar reservas, además de consultar la disponibilidad de espacios y ver un resumen de la capacidad de reservas actuales.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción

Este sistema fue creado como parte de un concurso de programación organizado por la Universidad UTEG. El objetivo es proporcionar una herramienta intuitiva y funcional para la administración de reservas de espacios de coworking. Con este sistema, los administradores pueden ver la disponibilidad de oficinas y salas, realizar reservas y consultar el estado de la capacidad ocupada o disponible.

## Características

- **Crear, editar y eliminar reservas**: Permite gestionar reservas con detalles como cliente, espacio, fecha y hora de inicio y fin.
- **Ver disponibilidad de espacios**: Lista de espacios no reservados, lo que facilita la consulta de disponibilidad.
- **Capacidad de reservas**: Muestra el porcentaje de ocupación y disponibilidad de los espacios.
- **Botones de navegación**: Cada sección incluye un botón para volver al inicio, facilitando la navegación.

## Requisitos

- **Python**: 3.8 o superior
- **Django**: 4.x
- **SQLite**: Base de datos utilizada para almacenamiento local en desarrollo

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1. **Clona el repositorio:**
```
git clone https://github.com/tuusuario/sistema-reservas.git
cd sistema-reservas
   ```
   
2. **Configura un entorno virtual:**
  ```
python3 -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. **Instala las dependencias:**
  ```
pip install -r requirements.txt
   ```

4. **Configura la base de datos: Ejecuta las migraciones para configurar la base de datos.**
  ```
python manage.py migrate
   ```

5. **Crea un superusuario: Esto te permitirá acceder al panel de administración de Django.**
  ```
   python manage.py createsuperuser
   ```

6. **Ejecuta el servidor:**
  ```
python manage.py runserver
   ```

7. **Accede a la aplicación en tu navegador en**
  ```
http://127.0.0.1:8000
   ```

## Uso
**Funcionalidades**
- **Inicio:** Muestra un resumen de la capacidad de reservas, incluyendo porcentajes de ocupación y disponibilidad.
- **Crear Reserva:** Permite registrar una nueva reserva seleccionando el espacio y las fechas.
- **Editar Reserva:** Lista las reservas activas y ofrece una opción para editarlas.
- **Eliminar Reserva:** Muestra las reservas actuales y permite seleccionar y eliminar una o varias.
- **Disponibilidad:** Visualiza los espacios que actualmente no están reservados.

**Navegación**
Cada vista incluye un botón para volver al inicio. La barra de navegación de la página principal incluye enlaces a cada funcionalidad clave del sistema.

## Estructura del Proyecto
La estructura principal de archivos del proyecto es la siguiente:

```
sistema-reservas/
├── reservas/                   # Aplicación principal
│   ├── migrations/              # Archivos de migración de la base de datos
│   ├── templates/reservas/      # Archivos de templates HTML
│   │   ├── inicio.html          # Página de inicio
│   │   ├── crear_reserva.html   # Formulario para crear reservas
│   │   ├── editar_reserva.html  # Lista y opciones para editar reservas
│   │   ├── eliminar_reserva.html# Lista y opciones para eliminar reservas
│   │   └── disponibilidad.html  # Muestra espacios disponibles
│   ├── views.py                 # Vistas para cada funcionalidad
│   ├── models.py                # Modelos de datos (Reserva, Espacio, Cliente)
│   ├── forms.py                 # Formularios para la creación y edición de reservas
│   ├── urls.py                  # Enrutamiento de URLs
├── static/                      # Archivos estáticos (imágenes, CSS)
├── manage.py                    # Archivo de gestión de Django
└── README.md                    # Documentación del proyecto
```

## Contribuciones
Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork de este repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia
No utiliza ninguna licencia ya que es un proyecto académico.


Este archivo README proporciona toda la información necesaria para que otros usuarios comprendan el propósito del proyecto, sus funcionalidades, cómo instalarlo y cómo utilizarlo en un entorno local.

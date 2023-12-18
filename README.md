# Gestor de Tareas

Este proyecto es una aplicación web para la gestión de tareas personales. Permite a los usuarios crear, organizar y priorizar sus tareas diarias de manera efectiva.

## Características

- Registro e inicio de sesión de usuarios.
- Creación y gestión de tareas personales.
- Marcar tareas como importantes.
- Visualizar y editar tareas pendientes.
- Registrar tareas completadas con fecha de finalización.
- Navegación intuitiva a través de un menú de usuario.

## Contribuciones Específicas (Branch - Saul Arturo Condori Machaca)

### Tareas Públicas (Public Tasks)

Mi contribución principal al proyecto fue el desarrollo de la funcionalidad "Tareas Públicas" (Public Tasks). Esta característica permite a los usuarios marcar sus tareas como públicas, haciéndolas accesibles a todos los usuarios de la plataforma. Fomenta la colaboración y transparencia, y añade una dimensión comunitaria a la gestión de tareas.

### Implementación de Casos de Prueba

Además, implementé varios casos de prueba para asegurar la funcionalidad y robustez de la aplicación. Estos tests incluyen:

- Pruebas para la creación de tareas, tanto con datos válidos como inválidos.
- Verificación del funcionamiento correcto del formulario de creación de tareas.
- Tests para la lógica de visualización y manejo de tareas públicas.

Estos casos de prueba fueron fundamentales para mantener la calidad y estabilidad del software durante el desarrollo.

## Tecnologías Utilizadas

- Django (Framework de Python para desarrollo web)
- SQLite (Base de datos)
- HTML/CSS (Frontend)
- Bootstrap (Framework de CSS)

## Instalación y Ejecución

Primero tener descargado sqlite e iniciar el ejecutable de sqlite3.
[Link de descarga del .zip](https://www.sqlite.org/2023/sqlite-tools-win-x64-3440200.zip)

1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`
6. Ingresar a tu navegador en el puerto 8000 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



Se crean nuevas tareas en una base de datos a parte y se eliminan una vez termine de ejecutarse el test

# Creacion de pruebas unitarias para el uso de fechas en la creacion de una nueva tarea:
## Pruebas Unitarias


![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/622dcff3-cedb-4c86-9dd3-078dd832a123)

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/d08eae43-4e1a-44c1-ab05-5800f4ea56b7)

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/af55bd76-1ee2-43de-9f6f-fc91ef28e29a)


Verifica que la fecha de creación de una tarea sea una fecha valida


![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/06901a4f-65e3-480f-8fb3-3338e8f42e9f)


## Lenguaje ubicuo:

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/bf5db47e-a12f-40ce-901e-02cd2b7fa9c4)

Modelo (Task): Se utiliza el término "Task" para referirse al modelo.el término "Task" representa la entidad que está siendo modelada en la base de datos.

ModelForm: El nombre TaskForm comunica que este formulario está específicamente diseñado para el modelo Task. Utilizar "Form" al final del nombre es una convención común para los formularios basados en modelos en Django.

Meta: En Django, la clase Meta se utiliza para proporcionar metainformación sobre el formulario, como el modelo al que está vinculado y los campos que deben incluirse.

fields = ['title', 'description', 'important', 'fecha_limite']: Al especificar los campos que deben incluirse en el formulario, se sigue utilizando el lenguaje del modelo. En este caso, los campos son 'title', 'description', 'important', y 'fecha_limite', que son los mismos campos definidos en el modelo Task.

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/e01775f5-1cd6-45fc-808a-446e63bfd7b6)


title: Un campo de caracteres que almacena el título de la tarea con una longitud máxima de 200 caracteres.

description: Un campo de texto más largo que almacena la descripción de la tarea con una longitud máxima de 1000 caracteres.

created: Un campo de fecha y hora que se establece automáticamente en la fecha y hora actual cuando se crea la tarea.

datecompleted: Un campo de fecha y hora que puede ser nulo y en blanco. Almacena la fecha y hora en que se completó la tarea.

important: Un campo booleano que indica si la tarea es importante o no. El valor predeterminado es False.

user: Una clave externa que se relaciona con el modelo de usuario (User). Utiliza on_delete=models.CASCADE, lo que significa que si un usuario se elimina, también se eliminarán todas sus tareas asociadas.

fecha_limite: Un campo de fecha que puede ser nulo y en blanco. Almacena la fecha límite para la tarea.

def __str__(self):: Un método que devuelve una representación de cadena del objeto. En este caso, devuelve una cadena que combina el título de la tarea y el nombre de usuario del propietario.

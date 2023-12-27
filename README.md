
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

**Modelo (Task):** Se utiliza el término "Task" para referirse al modelo.el término "Task" representa la entidad que está siendo modelada en la base de datos.

**ModelForm:** El nombre TaskForm comunica que este formulario está específicamente diseñado para el modelo Task. Utilizar "Form" al final del nombre es una convención común para los formularios basados en modelos en Django.

**Meta:** En Django, la clase Meta se utiliza para proporcionar metainformación sobre el formulario, como el modelo al que está vinculado y los campos que deben incluirse.

**fields = ['title', 'description', 'important', 'fecha_limite']:** Al especificar los campos que deben incluirse en el formulario, se sigue utilizando el lenguaje del modelo. En este caso, los campos son 'title', 'description', 'important', y 'fecha_limite', que son los mismos campos definidos en el modelo Task.

![image](https://github.com/SergioMenaQuispe/django-notes-ISII/assets/104391441/e01775f5-1cd6-45fc-808a-446e63bfd7b6)


**title:** Un campo de caracteres que almacena el título de la tarea con una longitud máxima de 200 caracteres.

**description:** Un campo de texto más largo que almacena la descripción de la tarea con una longitud máxima de 1000 caracteres.

**created:** Un campo de fecha y hora que se establece automáticamente en la fecha y hora actual cuando se crea la tarea.

**datecompleted:** Un campo de fecha y hora que puede ser nulo y en blanco. Almacena la fecha y hora en que se completó la tarea.

**important:** Un campo booleano que indica si la tarea es importante o no. El valor predeterminado es False.

**user:** Una clave externa que se relaciona con el modelo de usuario (User). Utiliza on_delete=models.CASCADE, lo que significa que si un usuario se elimina, también se eliminarán todas sus tareas asociadas.

**fecha_limite:** Un campo de fecha que puede ser nulo y en blanco. Almacena la fecha límite para la tarea.

**def __str__(self)::** Un método que devuelve una representación de cadena del objeto. En este caso, devuelve una cadena que combina el título de la tarea y el nombre de usuario del propietario.
Rama de Christian Pardavé Espinoza:

- Test vista tasks.
- Implementación de comentarios en tareas públicas.


Para la adición de comentarios en las tareas se creó la aplicación _comments_ dentro de django, para separar sus metodos de la aplicación _tasks_. Para esta implementación se identificó los modulos del proyecto.

![Modulo de Commets](https://github.com/SergioMenaQuispe/django-notes-ISII/blob/rama-christian/images/Captura%20de%20pantalla%202023-12-25%20225503.png)
# Pasos para iniciar proyecto

Primero tener descargado sqlite e iniciar el ejecutable de sqlite3.
[Link de descarga del .zip](https://www.sqlite.org/2023/sqlite-tools-win-x64-3440200.zip)


1. `pip install -r requirements.txt`
2. `python manage.py makemigrations`
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`
6. Ingresar a tu navegador en el puerto 8000 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


# FEATURE PROGRESS BAR 

Se agrego el feature de una barra de progreso de tareas completadas y por completar.

```python

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    tasks_completed = Task.objects.filter(user=request.user, datecompleted__isnull=False)

    count_completed = tasks_completed.count()
    count_not_completed = tasks.count()

    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    
    tasks_not_completed = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    count_not_completed = tasks_not_completed.count()
    count_completed = tasks.count()
    
    return render(request, 'tasks.html', {"tasks": tasks, "count_total": count_completed + count_not_completed, "count_completed": count_completed})

```

### Test

Se hizo una prueba de test para comprobar que la barra de progreso exista.


```python
class TasksTestCase(LiveServerTestCase):
    def setUp(self):
        # Configuración del navegador Selenium (puedes ajustar según tus necesidades)
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Ejecución en modo sin cabeza para pruebas en segundo plano
        self.selenium = webdriver.Chrome(options=chrome_options)
        self.selenium.implicitly_wait(10)  # Espera implícita de 10 segundos
        super(TasksTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(TasksTestCase, self).tearDown()

    def test_tasks_page(self):
        # Crear un usuario y tareas para ese usuario
        user = User.objects.create_user(username='testuser', password='testpass')
        Task.objects.create(user=user, description='Task 1')

        # Acceder a la página de tareas con Selenium
        self.selenium.get(f'{self.live_server_url}/signup/')
        self.selenium.find_element(By.NAME, 'username').send_keys('mena3')
        self.selenium.find_element(By.NAME, 'password1').send_keys('123qweop')
        self.selenium.find_element(By.NAME, 'password2').send_keys('123qweop')
        self.selenium.find_element(By.NAME, 'password2').send_keys(Keys.ENTER)
    
        # Verificar que la página de tareas se carga correctamente
        self.assertIn('tasks', self.selenium.find_element(By.CSS_SELECTOR, "h1").text.lower())
        
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'progress'))
        )

        # Verificar que la tarea se muestra en la página
        progress_bar = self.selenium.find_element(By.TAG_NAME, 'progress')
        self.assertIsNotNone(progress_bar, 'Progress bar not found')


        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, 'progress-message'))
        )

        progress_message = self.selenium.find_element(By.ID, 'progress-message')
        self.assertIn('Tasks completed 0/0', progress_message.text)
```


# MODELO DE DOMINIO

El modelo de dominio se centra en el dominio de "Task", del cual se extienden otros modelos como "TaskAdmin", "TaskForm", y "TaskConfig", y también otro modelo "User" que administras las tasks.

![Alt text](image.png)

## MÓDULO AUTH

Se agrego el módulo de "auth", en el que se incluyeron funciones como el "sigin", "signout", y "signup".

```python

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)  # Replace LoginFailure with login
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def signout(request):
    logout(request)
    return redirect('home')


```

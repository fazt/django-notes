from django.test import TestCase
# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .models import Task  # Reemplaza 'your_app' con el nombre real de tu aplicación

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
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm

# Constante para Test Description
TEST_TEMPLATE = 'Test Description'

class CreateTaskTestCase(TestCase):
    def setUp(self):
        # Crea un usuario para las pruebas
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_form_display(self):
        # Prueba que el formulario se muestra correctamente
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_form_submission_success(self):
        # Prueba la creación de una tarea con datos válidos
        response = self.client.post(reverse('create_task'), {
            'title': 'Test Task',
            'description': TEST_TEMPLATE,
            'important': True,
            
        })
        self.assertEqual(response.status_code, 302)  # Redirección después del éxito
        self.assertTrue(Task.objects.filter(title='Test Task').exists())

    def test_form_submission_failure(self):
        # Prueba la creación de una tarea con datos inválidos
        response = self.client.post(reverse('create_task'), {
            'title': '',  # Título vacío, debería fallar
            'description': TEST_TEMPLATE,
            'important': True,
        })
        self.assertEqual(response.status_code, 200)  # No hay redirección debido al fallo
        self.assertFalse(Task.objects.filter(description = TEST_TEMPLATE).exists())

    def tearDown(self):
        self.user.delete()

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
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task

class SharedTasksTestCase(TestCase):
    username_template = 'EGRM23'
    password_template = 'V6E388KR'
    title_template = 'Tarea Compartida'
    description_template = 'Esta es una tarea compartida'

    def setUp(self):
        user_exists = User.objects.filter(username=self.username_template).exists()
        if not user_exists:
            User.objects.create_user(
                username=self.username_template,
                password=self.password_template
            )
        
        users_data = [
            {'username': 'UsuarioPrueba1', 'password': 'contra1molde'},
            {'username': 'UsuarioPrueba2', 'password': 'contra2molde'},
            {'username': 'UsuarioPrueba3', 'password': 'contra3molde'},
        ]

        for user_data in users_data:
            user_exists = User.objects.filter(username=user_data['username']).exists()
            if not user_exists:
                User.objects.create_user(
                    username=user_data['username'],
                    password=user_data['password']
                )
        
        self.client.login(username=self.username_template, password=self.password_template)

    def test_create_shared_task(self):
        user1_id = User.objects.get(username='UsuarioPrueba1').id
        user2_id = User.objects.get(username='UsuarioPrueba2').id
        
        response = self.client.post(reverse('create_task'), {
            'title': self.username_template,
            'description': self.description_template,
            'shared': True,
            'shared_with': [user1_id, user2_id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title=self.username_template, shared=True).exists())

    def test_view_shared_tasks(self):
        response = self.client.get(reverse('shared_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.username_template)

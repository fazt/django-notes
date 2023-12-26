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

        # Acceder a la página de login para verificar un usuario existente.
        self.selenium.get(f'{self.live_server_url}/signin/')
        self.selenium.find_element(By.NAME, 'username').send_keys('marisol')
        self.selenium.find_element(By.NAME, 'password').send_keys('123456')
        self.selenium.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
    
        # Verificar que la página de tareas se carga correctamente
        self.assertIn('tasks', self.selenium.find_element(By.CSS_SELECTOR, "h1").text.lower())

        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'progress'))
        )

        # Acceder a la página de login para verificar un usuario no existente.
        self.selenium.get(f'{self.live_server_url}/signin/')
        self.selenium.find_element(By.NAME, 'username').send_keys('marisol')
        self.selenium.find_element(By.NAME, 'password').send_keys('123')
        self.selenium.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
    
        # Verificar que la página de tareas se carga correctamente
        self.assertIn('tasks', self.selenium.find_element(By.CSS_SELECTOR, "h1").text.lower())

        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'progress'))
        )

        progress_message = self.selenium.find_element(By.ID, 'progress-message')
        self.assertIn('Completed 0/0', progress_message.text)
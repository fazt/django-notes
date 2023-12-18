from django.test import TestCase
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

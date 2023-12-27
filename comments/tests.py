# tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from tasks.forms import TaskForm

class TaskFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_valid_form(self):
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'fecha_limite': '2023-12-31',  
            'important': True,
        }

        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        
        data = {
            'title': 'Test Task',
            'description': 'This is a test task',
            'fecha_limite': '54164651',  
            'important': True,
        }

        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('fecha_limite', form.errors)  # Verifica que haya errores en el campo de fecha

    def test_blank_fields(self):
        # Prueba que el formulario sea inv�lido si algunos campos requeridos est�n en blanco
        data = {
            'title': '',
            'description': '',
            'fecha_limite': '',
            'important': False,
        }

        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('description', form.errors)
       

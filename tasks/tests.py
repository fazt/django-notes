from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task

class SharedTasksTestCase(TestCase):
    def setUp(self):
        self.client.login(username='EGRM23', password='V6E388KR')

    def test_create_shared_task(self):
        response = self.client.post(reverse('create_task'), {
            'title': 'Tarea Compartida',
            'description': 'Esta es una tarea compartida',
            'shared': True,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='Tarea Compartida', shared=True).exists())

    def test_view_shared_tasks(self):
        response = self.client.get(reverse('shared_tasks'))

        # Verificar que la página se carga correctamente y contiene las tareas compartidas
        self.assertEqual(response.status_code, 200)  # 200 es el código de éxito
        self.assertContains(response, 'Tarea Compartida')
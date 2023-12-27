from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task

class SharedTasksTestCase(TestCase):
    username_template = 'EGRM23'
    password_template = 'V6E388KR'
    title_template = 'Tarea Compartida'
    description_template = 'Esta es una tarea compartida'

    def setUp(self):
        self.client.login(username=self.username_template, password=self.password_template)

    def test_create_shared_task(self):
        response = self.client.post(reverse('create_task'), {
            'title': self.username_template,
            'description': self.description_template,
            'shared': True,
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title=self.username_template, shared=True).exists())

    def test_view_shared_tasks(self):
        response = self.client.get(reverse('shared_tasks'))

        # Verificar que la página se carga correctamente y contiene las tareas compartidas
        self.assertEqual(response.status_code, 200)  # 200 es el código de éxito
        self.assertContains(response, self.username_template)
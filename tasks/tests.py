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
"""Pruebas unitarias para las vistas."""
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_registration_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('profile')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_profile_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')
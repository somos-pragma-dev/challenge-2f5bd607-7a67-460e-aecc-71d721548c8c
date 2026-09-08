"""Pruebas unitarias para los modelos."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from..models import Profile

User = get_user_model()

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(user.username, 'testuser')

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='12345')
        profile = Profile.objects.create(user=user, name='Test User', email='test@example.com')
        self.assertEqual(profile.user.username, 'testuser')
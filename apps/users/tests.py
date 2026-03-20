from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from apps.users.models import UserProfile

class AuthTests(TestCase):
    def setUp(self):
        # Admin / Manager
        self.admin_user = User.objects.create_superuser('admin', 'admin@chaplin.com', 'admin123')
        
        # Gestor
        self.gestor = User.objects.create_user('gestor', 'gestor@chaplin.com', 'gestor123')
        self.gestor.profile.role = 'gestor'
        self.gestor.profile.save()
        
        # Colaborador (Standard User)
        self.colaborador = User.objects.create_user('colab', 'colab@chaplin.com', 'colab123')
        self.colaborador.profile.role = 'colaborador'
        self.colaborador.profile.save()

    def test_register_view_access_anonymous(self):
        """Anonymous users should be redirected to login when trying to register."""
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('users:login')))

    def test_register_view_access_colaborador(self):
        """Standard users (colaborador) should be redirected to dashboard when trying to register."""
        self.client.login(username='colab', password='colab123')
        response = self.client.get(reverse('users:register'))
        self.assertRedirects(response, reverse('tasks:dashboard'))

    def test_register_view_access_admin(self):
        """Admins can access the registration page."""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Criar Conta')

    def test_register_view_post_admin(self):
        """Admins can create new users via the registration page."""
        self.client.login(username='admin', password='admin123')
        
        # Valid data
        data = {
            'username': 'newuser',
            'email': 'newuser@chaplin.com',
            'first_name': 'New',
            'password': 'strongpassword123',
            'password_confirm': 'strongpassword123'
        }
        
        response = self.client.post(reverse('users:register'), data)
        self.assertRedirects(response, reverse('users:admin_users_list'))
        
        # Check if user was created
        self.assertTrue(User.objects.filter(username='newuser').exists())
        new_user = User.objects.get(username='newuser')
        self.assertTrue(new_user.check_password('strongpassword123'))
        
        # Check if profile was created via signal with default role
        self.assertEqual(new_user.profile.role, 'colaborador')

    def test_register_form_validation(self):
        """Registration form validates password confirmation."""
        self.client.login(username='admin', password='admin123')
        
        # Passwords do not match
        data = {
            'username': 'baduser',
            'email': 'baduser@chaplin.com',
            'first_name': 'Bad',
            'password': 'strongpassword123',
            'password_confirm': 'differentpassword'
        }
        
        response = self.client.post(reverse('users:register'), data)
        self.assertEqual(response.status_code, 200) # Form re-renders with errors
        
        # Check if the error is in the form context
        form = response.context.get('form')
        self.assertIsNotNone(form)
        self.assertTrue(form.errors)
        self.assertIn('password_confirm', form.errors)
        self.assertEqual(form.errors['password_confirm'][0], 'As senhas não coincidem.')
        
        # Check that user was NOT created
        self.assertFalse(User.objects.filter(username='baduser').exists())

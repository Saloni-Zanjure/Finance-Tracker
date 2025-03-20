from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
import json
from authentication.utils import account_activation_token
from django.contrib.auth.tokens import PasswordResetTokenGenerator
 
 
class AuthenticationTestCases(TestCase):
 
    def setUp(self):
        """Create a test user for login and activation tests"""
        self.user = User.objects.create_user(username='testuser', email='test@email.com', password='password123')
        self.user.is_active = False
        self.user.save()
 
    ### 1. Email Validation Tests ###
    def test_invalid_email(self):
        response = self.client.post(reverse('validate_email'),
                                    json.dumps({'email': 'invalidemail'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn('email_error', response.json())
 
    def test_existing_email(self):
        response = self.client.post(reverse('validate_email'),
                                    json.dumps({'email': 'test@email.com'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertIn('email_error', response.json())
 
    def test_valid_email(self):
        response = self.client.post(reverse('validate_email'),
                                    json.dumps({'email': 'new@email.com'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn('email_valid', response.json())
 
    ### 2. Username Validation Tests ###
    def test_invalid_username(self):
        response = self.client.post(reverse('validate_username'),
                                    json.dumps({'username': 'invalid user@123'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn('username_error', response.json())
 
    def test_existing_username(self):
        response = self.client.post(reverse('validate_username'),
                                    json.dumps({'username': 'testuser'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 409)
        self.assertIn('username_error', response.json())
 
    def test_valid_username(self):
        response = self.client.post(reverse('validate_username'),
                                    json.dumps({'username': 'newuser'}),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIn('username_valid', response.json())
 
    ### 3. User Registration Tests ###
    def test_successful_registration(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'newuser', 'email': 'newuser@email.com', 'password': 'strongpass'})
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.assertTrue(User.objects.filter(username='newuser').exists())
 
    def test_existing_username_registration(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'testuser', 'email': 'new@email.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username already exists')
 
    def test_existing_email_registration(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'newuser', 'email': 'test@email.com', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email already exists')
 
    def test_short_password_registration(self):
        response = self.client.post(reverse('register'),
                                    {'username': 'newuser', 'email': 'newuser@email.com', 'password': '123'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Password too short')
 
    ### 4. Login Tests ###
 
    
 
    def test_empty_fields_login(self):
        response = self.client.post(reverse('login'), {})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please fill all fields')
 
    ### 5. Logout Test ###
    def test_logout(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirects to login page
 
 
    
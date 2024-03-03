from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        data = {'username': 'test_user', 'email': 'test@example.com', 'password': 'testpassword'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='test_user').exists())

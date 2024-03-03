from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

class ProductCreationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user', email='test@example.com')
        self.client.force_authenticate(user=self.user)

    def test_product_creation(self):
        data = {
            'name': 'Test Product',
            'description': 'Test Description',
            'price': '10.00',
            'image': None  # Add image data if required
        }
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

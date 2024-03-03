from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from marketplace.models import Product
from rest_framework.test import APIClient

class ProductPurchaseTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.client.force_authenticate(user=self.user)
        self.product = Product.objects.create(name='Test Product', description='Test Description', price='10.00', seller=self.user)


    def test_product_purchase(self):
        self.client.force_authenticate(user=self.user)
        data = {'product_id': self.product.id, 'purchase_price': '10.00'}
        response = self.client.post('/api/products/purchase/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework import serializers

#Product
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
    

#Purchase
class Purchase(models.Model):
    product_name = models.CharField(max_length=100)
    seller_username = models.CharField(max_length=100)
    buyer_username = models.CharField(max_length=100)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.product_name} by {self.buyer_username}"

#List and Filter
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    from .serializers import ProductSerializer
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'price']
    search_fields = ['name', 'description']


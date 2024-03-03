from django.urls import path
from .views import UserAPIView, UserLoginAPIView, ProductView,ProductPurchaseAPIView,ProductListAPIView

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserAPIView.as_view(), name='user_detail'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    
    path('products/', ProductView.as_view(), name='product_api'),
    path('products/<int:pk>', ProductView.as_view(), name='product_api'),
    path('products/purchase/', ProductPurchaseAPIView.as_view(), name='product_purchase'),
    path('products/list/', ProductListAPIView.as_view(), name='product_list')

]

'''
GET /api/users/ - UserAPIView.get() - List all users
POST /api/users/ - UserAPIView.post() - Create a new user
GET /api/users/<int:pk>/ - UserAPIView.get() - Retrieve a specific user
PUT /api/users/<int:pk>/ - UserAPIView.put() - Update a specific user
DELETE /api/users/<int:pk>/ - UserAPIView.delete() - Delete a specific user
POST /api/login/ - UserLoginAPIView.post() - User login

GET /api/products/ - ProductView.get() - List all products
POST /api/products/ - ProductView.post() - Create a new product
POST /api/products/purchase/ - ProductPurchaseAPIView.post() - Purchase a product

GET /api/products/list/ - ProductListAPIView.get() - List all products with filtering and sorting options
'''
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, UserLoginSerializer

from .models import Product,Purchase
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView

from django.core.mail import send_mail

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'username': user.username
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.data['seller'] = request.user.id  # Set the seller attribute to the authenticated user
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5  # You can adjust the page size as needed
        
        products = Product.objects.all()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)
    
class ProductPurchaseAPIView(APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        purchase_price = request.data.get('purchase_price')
        
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Ensuring seller's username is recorded
        seller_username = product.seller.username
        
        purchase_data = {
            'product_name': product.name,
            'seller_username': seller_username,
            'buyer_username': request.user.username,
            'purchase_price': purchase_price
        }
        
        purchase = Purchase.objects.create(**purchase_data)
        
        send_mail(
            'New Purchase Notification',
            f'Your product "{product.name}" has been purchased by {request.user.username}.',
            'workshivang@gmail.com',
            [product.seller.email],
            fail_silently=False,
        )
        return Response({'message': 'Purchase successful', 'purchase_data': purchase_data}, status=status.HTTP_200_OK)
    

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['name', 'price']
    search_fields = ['name', 'description']
# marketplace/serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Product

#User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

#User Login
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')  

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User account is disabled.")
                return user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")


#Product
class ProductSerializer(serializers.ModelSerializer):

    # seller = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image','seller']
    
    # def create(self, validated_data):
    #     # Automatically set the authenticated user as the seller
    #     validated_data['seller'] = self.context['request'].user
    #     return super().create(validated_data)
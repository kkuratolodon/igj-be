from django.conf import settings
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import GameUser
from .serializers import (UserRegisterSerializer, UserSerializer,
                          UserUpdateSerializer)


class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        # Validate the secret key
        secret = request.data.get('secret')
        if secret != settings.GAME_SECRET_KEY:
            return Response({"error": "Invalid secret key"}, status=status.HTTP_403_FORBIDDEN)
            
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDataView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        # Validate the secret key
        secret = request.data.get('secret')
        if secret != settings.GAME_SECRET_KEY:
            return Response({"error": "Invalid secret key"}, status=status.HTTP_403_FORBIDDEN)
            
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"error": "Username and password are required"}, 
                            status=status.HTTP_400_BAD_REQUEST)
                            
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({"error": "Invalid credentials"}, 
                            status=status.HTTP_401_UNAUTHORIZED)
                            
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UpdateUserView(APIView):
    permission_classes = [AllowAny]
    
    def put(self, request):
        # Validate the secret key
        secret = request.data.get('secret')
        if secret != settings.GAME_SECRET_KEY:
            return Response({"error": "Invalid secret key"}, status=status.HTTP_403_FORBIDDEN)
            
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({"error": "Username and password are required"}, 
                            status=status.HTTP_400_BAD_REQUEST)
                            
        user = authenticate(username=username, password=password)
        
        if not user:
            return Response({"error": "Invalid credentials"}, 
                            status=status.HTTP_401_UNAUTHORIZED)
        
        # Update user data
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            # Handle username update if provided
            new_username = serializer.validated_data.get('new_username')
            if new_username:
                user.username = new_username
            
            # Update other fields
            for field in ['hp', 'money', 'level', 'score', 'last_completed_level',
                         'archer_level', 'catapult_level', 'magic_level', 'guardian_level']:
                if field in serializer.validated_data:
                    setattr(user, field, serializer.validated_data[field])
            
            user.save()
            return Response(UserSerializer(user).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

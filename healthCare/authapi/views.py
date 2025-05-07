from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            return Response({'error':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)
        
        user = authenticate(username=username,password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            })
        else:
            return Response({"error":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
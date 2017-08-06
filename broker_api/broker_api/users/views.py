from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserListSerializer, CreateUserSerializer
# Create your views here.

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class GetUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
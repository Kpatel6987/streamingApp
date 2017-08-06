from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountListSerializer

# class CreateUser(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer

class GetAccounts(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer
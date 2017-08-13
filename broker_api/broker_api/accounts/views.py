from django.shortcuts import render
from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer

class ListCreateAccount(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class RetrieveAccount(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
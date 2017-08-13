from django.shortcuts import render
from rest_framework import generics
from .models import Position
from .serializers import PositionSerializer

class ListCreatePosition(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class RetrievePosition(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
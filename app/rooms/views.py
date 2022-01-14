from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Rooms
from .serializers import RoomsSerializer
from rest_framework import filters
from rest_framework.response import Response
class RoomsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Rooms.objects.all()
    serializer_class=RoomsSerializer

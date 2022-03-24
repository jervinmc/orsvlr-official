from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Settings
from .serializers import SettingsSerializer
from rest_framework import filters
from rest_framework.response import Response
class SettingsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Settings.objects.all()
    serializer_class=SettingsSerializer

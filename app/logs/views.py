from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Log
from .serializers import LogSerializer
from rest_framework import filters
from rest_framework.response import Response
class LogView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Log.objects.all()
    serializer_class=LogSerializer

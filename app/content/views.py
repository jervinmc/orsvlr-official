from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Content
from .serializers import ContentSerializer
from rest_framework import filters
from rest_framework.response import Response
class ContentView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Content.objects.all()
    serializer_class=ContentSerializer

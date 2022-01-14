from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Gallery
from .serializers import GallerySerializer
from rest_framework import filters
from rest_framework.response import Response
class GalleryView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Gallery.objects.all()
    serializer_class=GallerySerializer

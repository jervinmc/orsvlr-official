from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Amenities
from .serializers import AmenitiesSerializer
from rest_framework import filters
from rest_framework.response import Response
class AmenitiesView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Amenities.objects.all()
    serializer_class=AmenitiesSerializer

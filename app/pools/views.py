from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Pools
from .serializers import PoolsSerializer
from rest_framework import filters
from rest_framework.response import Response
class PoolsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Pools.objects.all()
    serializer_class=PoolsSerializer

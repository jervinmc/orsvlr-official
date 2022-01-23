from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Promo
from .serializers import PromoSerializer
from rest_framework import filters
from rest_framework.response import Response
class PromoView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Promo.objects.all()
    serializer_class=PromoSerializer

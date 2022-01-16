from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Payment
from .serializers import PaymentSerializer
from rest_framework import filters
from rest_framework.response import Response
class PaymentView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer

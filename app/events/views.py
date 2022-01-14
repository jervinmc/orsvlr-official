from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Events
from .serializers import EventsSerializer
from rest_framework import filters
from rest_framework.response import Response
class EventsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Events.objects.all()
    serializer_class=EventsSerializer

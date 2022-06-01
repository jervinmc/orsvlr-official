from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Faq
from .serializers import FaqSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from users.models import User
from users.serializers import UserSerializer
# from color.serializers import ColorSerializer
# from color.serializers import Color
from decouple import config
import pusher
class FaqView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Faq.objects.all()
    serializer_class=FaqSerializer



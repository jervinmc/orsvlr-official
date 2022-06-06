from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import AdPend
from .serializers import AdPendSerializer
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
class AdPendView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=AdPend.objects.all()
    serializer_class=AdPendSerializer

    def create(self,request):
        res = request.data
        AdPend.objects.filter(book_id = res.get('book_id')).delete()
        serializer = AdPendSerializer(data = res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class AdPendBookID(generics.GenericAPIView):
    def get(self,request,format=None,product_id=None,book_id=None):
        try:
            ads = AdPend.objects.filter(book_id=book_id)
            serializers = AdPendSerializer(ads,many=True)
            return Response(data=serializers.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

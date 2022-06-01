from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Ads
from .serializers import AdsSerializer
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
class AdsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Ads.objects.all()
    serializer_class=AdsSerializer



class AdsBookID(generics.GenericAPIView):
    def get(self,request,format=None,product_id=None):
        try:
            ads = Ads.objects.filter(product_id=product_id)
            serializers = AdsSerializer(ads,many=True)
            return Response(data=serializers.data)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class AdsEditProduct(generics.GenericAPIView):
    def post(self,request,format=None,product_id=None):
        try:
            res = request.data
            ads = Ads.objects.filter(book_id=res.get('book_id')).delete()
            # color = Color.objects.filter(book_id=res.get('book_id')).delete()
            print(res.get('ads_label'))

            ads_label = res.get('ads_label')
            ads_price = res.get('ads_price')
            # color_label = res.get('color_label')
            serializers_ads = ''
            if(res.get('ads_label') != ['']):
                for (x,i) in enumerate(ads_label):
                    if(ads_price[x]!='' and ads_label[x]!=''):
                        serializers_ads = AdsSerializer(data={"book_id":res.get('book_id'),"price":ads_price[x],"label":i})
                        serializers_ads.is_valid(raise_exception=True)
                        serializers_ads.save()  
            # if(res.get('color_label') != ['']):
            #     for (x,i) in enumerate(color_label):
            #         if(color_label[x]!=''):
            #             serializers_color = ColorSerializer(data={"product_id":res.get('product_id'),"label":color_label[x]})
            #             serializers_color.is_valid(raise_exception=True)
            #             serializers_color.save()
            #     return Response(data=serializers_ads.data)
            return Response(data=[])
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
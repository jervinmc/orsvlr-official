from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.response import Response
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import datetime
from rest_framework import status, viewsets
from email.mime.text import MIMEText
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.template import Context

from datetime import datetime

now = datetime.now()
class BookView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def create(self,request):
        res = request.data
        print(res.get('transaction_date'))
        message = get_template('mail.html').render({'code':request.data.get('code')})
        msg = EmailMultiAlternatives('Status', message,'vleonoradonotreply@gmail.com', [res.get('email')])
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg.content_subtype = "html"
        msg.send()
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def list(self,request):
        print('okay')
        items = Book.objects.all()
        items = BookSerializer(items,many=True)
        return Response(status=status.HTTP_200_OK,data=items.data)

class GetCode(generics.GenericAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def post(self,request,format=None):
        try:
            items=[]
            items=Book.objects.filter(code=request.data.get('code'))
            serializer=BookSerializer(items,many=True)
            book_data = serializer.data
            return Response(status=status.HTTP_200_OK,data=book_data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

# class Reschedule(generics.GenericAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
#     def post(self,request,format=None):
#         try:
#             res = request.data
#             items = 
#         except Exception as e:
#             print(e)
#             return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class ConfirmedStatus(generics.GenericAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    def post(self,request,format=None):
        try:
            if(request.data.get('status')=='Request For Cancellation'):
                message = get_template('req_for_cancellation.html').render({'code':request.data.get('code')})
            if(request.data.get('status')=='cancelled'):

                message = get_template('cancelled.html').render({'code':request.data.get('code')})
            if(request.data.get('status')=='confirmed'):
                message = get_template('confirm.html').render({'code':request.data.get('code')})
            
            elif(request.data.get('status')=='rejected'):
                message = get_template('rejected.html').render({'code':request.data.get('code')})
            
            elif(request.data.get('status')=='completed'):
                message = get_template('completed.html').render({'code':request.data.get('code')})
            
            elif(request.data.get('status')=='pending'):
                message = get_template('completed.html').render({'code':request.data.get('code')})
            elif(request.data.get('status')=='archive'):
                message = get_template('completed.html').render({'code':request.data.get('code')})
            
            # message = get_template('confirm.html').render({'code':request.data.get('code')})
            msg = EmailMultiAlternatives('Status', message,'vleonoradonotreply@gmail.com', [request.data.get('email')])
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg.content_subtype = "html"
            msg.send()
            print(request.data.get('cancellation_description'))
            Book.objects.filter(id=request.data.get('id')).update(status=request.data.get('status'),cancellation_description=request.data.get('cancellation_description'))
            return Response(status=status.HTTP_200_OK,data=[])
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class OTP(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            message = get_template('otp.html').render({"code":request.data.get('code')})
            msg = EmailMultiAlternatives('OTP', message,'autootoncst@gmail.com', [request.data.get('email')])
            html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg.content_subtype = "html"
            msg.send()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class BulkDeleteArchived(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            print("nice")
            res = request.data
            for x in res.get('items'):
                print(x)
                Book.objects.filter(id=x['id']).delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class BulkSetCompleted(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            for x in res.get('items'):
                Book.objects.filter(id=x['id']).update(status='completed')
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class BulkSetArchived(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            for x in res.get('items'):
                Book.objects.filter(id=x['id']).update(status='archived')
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
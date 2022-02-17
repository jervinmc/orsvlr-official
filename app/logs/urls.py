from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

routers=DefaultRouter()
routers.register(r'',views.LogView)
urlpatterns=[
    path('',include(routers.urls))
]

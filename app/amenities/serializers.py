from rest_framework import serializers
from .models import Amenities

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Amenities
        fields="__all__"

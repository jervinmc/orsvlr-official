from rest_framework import serializers
from .models import AdPend

class AdPendSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdPend
        fields="__all__"

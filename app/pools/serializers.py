from rest_framework import serializers
from .models import Pools

class PoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pools
        fields="__all__"

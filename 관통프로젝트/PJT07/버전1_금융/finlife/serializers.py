from .models import DepositOptions, DepositProducts
from rest_framework import serializers

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DepositProducts

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = DepositOptions
        read_only_fields = ('product',)

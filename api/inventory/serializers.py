from rest_framework import serializers
from .models import Product, Purchase, Sales

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Purchaseserializer(serializers.ModelSerializer):
    class Meta:
        model  = Purchase
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
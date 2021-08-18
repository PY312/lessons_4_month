from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name parent '.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "  id title description price  category tags".split()


class CategoryWithProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = 'id name parent products'.split()

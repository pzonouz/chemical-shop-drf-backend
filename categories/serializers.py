from rest_framework import serializers

from categories.models import Category
from products.serializers import ProductSerializer


class CategoryAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "image"]


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "image", "products"]

from rest_framework import serializers

from categories.models import Category
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ["id", "name", "english_name", "price", "image", "category"]

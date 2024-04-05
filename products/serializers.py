from rest_framework import serializers

from categories.models import Category
from favorites.serializers import FavoriteSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )
    favorites = FavoriteSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "english_name",
            "price",
            "image",
            "category",
            "favorites",
        ]

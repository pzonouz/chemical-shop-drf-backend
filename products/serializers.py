from rest_framework import serializers

from categories.models import Category
from favorites.models import Favorite
from favorites.serializers import FavoriteSerializer
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )
    favorites = serializers.SerializerMethodField()

    def get_favorites(self, obj):
        user = self.context.get("request").user  # type: ignore
        return FavoriteSerializer(
            Favorite.objects.filter(product=obj, user_id=user.id), many=True
        ).data

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


class ProductSerializerForOrder(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "english_name",
            "price",
            "image",
            "category",
            # "favorites",
        ]

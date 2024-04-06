from rest_framework import serializers

from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = Favorite
        fields = ("product", "user")
        read_only_fields = ("user",)

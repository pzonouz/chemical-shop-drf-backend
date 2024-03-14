from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ("file", "user")

    def create(self, validated_data):
        return super().create(validated_data)

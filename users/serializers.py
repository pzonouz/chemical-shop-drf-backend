from users.models import CustomUser, UserProfile
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "image", "address", "mobile", "created_at")


class CustomUserSerializer(ModelSerializer):
    profile = UserProfileSerializer()
    id = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ("id", "email", "is_staff", "is_active", "profile")
        read_only_fields = ("email", "id")

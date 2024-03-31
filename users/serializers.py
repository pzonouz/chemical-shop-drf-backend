from users.models import CustomUser, UserProfile
from rest_framework.serializers import ModelSerializer


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name", "image", "address", "mobile", "created_at")


class CustomUserSerializer(ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ("id", "email", "is_staff", "is_active", "profile")
        read_only_fields = ("email", "id")

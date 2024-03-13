from users.models import CustomUser
from rest_framework.serializers import ModelSerializer


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "address",
            "created_at",
            "mobile",
            "image",
        )

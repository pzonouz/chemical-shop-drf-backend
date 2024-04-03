from rest_framework.serializers import ModelSerializer
from .models import Process


class ProcessSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ("order_id",)
        write_only_fields = ("order_id",)


class ListProcessSerializer(ModelSerializer):
    class Meta:
        model = Process
        fields = ("created_at", "status")

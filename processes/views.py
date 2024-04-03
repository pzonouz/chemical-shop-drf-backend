from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from processes.serializers import ProcessSerializer
from .models import Process


class ProcessViewSet(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin, GenericViewSet
):
    permission_classes = [IsAdminUser]
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

    def create(self, request, *args, **kwargs):
        processes = Process.objects.filter(order__id=request.data.get("order_id"))
        process_status = None
        if processes.count() == 0:
            process_status = "I"
        if processes.count() == 1 and processes[0].status == "I":
            process_status = "R"

        if (
            processes.count() == 2
            and processes[0].status == "I"
            and processes[1].status == "R"
        ):
            process_status = "D"

        request.data["status"] = process_status
        print(request.data["status"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Process.objects.create(
            status=request.data.get("status"), order_id=request.data.get("order_id")
        )
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from store.models import Store
from store.serializers import StoreSerializer


class StoreViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from products.models import Product
from products.serializers import ProductSerializer


class ProductListRetrieve(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAdminViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

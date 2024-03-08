from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from products.serializers import ProductSerializer
from products.models import Product


class ProductListRetrieve(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAdminViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

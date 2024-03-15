from django.db import models

from products.models import Product
from users.models import CustomUser


class CartItem(models.Model):
    user = models.OneToOneField(
        CustomUser, related_name="cart", on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Product, related_name="products")

    def __str__(self) -> str:
        return self.user.email

from django.db import models

from config.models import TimeStampedModel
from orders.models import Order
from products.models import Product
from users.models import CustomUser


class CartItem(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items",
    )
    quantity = models.PositiveBigIntegerField(
        default=1,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        related_name="cart_items",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.user.email

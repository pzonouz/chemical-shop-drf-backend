from django.db import models

from config.models import TimeStampedModel
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
        # unique=True
    )
    quantity = models.PositiveBigIntegerField(
        default=1,
    )

    def __str__(self) -> str:
        return self.user.email

from django.db import models

from config.models import TimeStampedModel
from users.models import CustomUser

delivery_methods = (("P", "POST"), ("I", "INPLACE"))


class Order(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, related_name="orders", on_delete=models.CASCADE
    )
    delivery_method = models.CharField(choices=delivery_methods, max_length=1)

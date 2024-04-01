from django.db import models

from config.models import TimeStampedModel
from users.models import CustomUser

delivery_methods = (("P", "POST"), ("I", "INPLACE"))
process_status = (("I", "IN_PROGRESS"), ("R", "READY"), ("D", "DELIVERED"))


class Order(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, related_name="orders", on_delete=models.CASCADE
    )
    delivery_method = models.CharField(choices=delivery_methods, max_length=1)


class Process(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="processes")
    status = models.CharField(choices=process_status, max_length=1)

# Create your models here.
from django.db import models
from config.models import TimeStampedModel
from orders.models import Order

process_status = (("I", "IN_PROGRESS"), ("R", "READY"), ("D", "DELIVERED"))


class Process(TimeStampedModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="processes")
    status = models.CharField(
        choices=process_status, max_length=1, default="I", null=True
    )
    description = models.TextField(null=True, blank=True)

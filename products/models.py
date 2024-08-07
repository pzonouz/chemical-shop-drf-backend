from django.db import models

from categories.models import Category
from config.models import TimeStampedModel
from users.models import CustomUser


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=255, default="English Name")
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    is_customized = models.BooleanField(default=False, blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True
    )
    kind = models.CharField(max_length=64, default="")
    modified_by = models.CharField(max_length=256, default="")
    diameter = models.CharField(max_length=64)
    state = models.CharField(max_length=100, default="")
    analyze = models.CharField(max_length=100, default="")
    quantity = models.CharField(max_length=64)
    unit = models.CharField(max_length=100, default="")
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name + "," + str(self.pk) + "," + self.image  # type: ignore

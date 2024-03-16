from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=255, default="English Name")
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

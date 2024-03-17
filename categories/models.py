from django.db import models

from config.models import TimeStampedModel


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

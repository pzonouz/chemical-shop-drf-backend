from django.db import models

from users.models import CustomUser

# from users.models import CustomUser


class Image(models.Model):
    # name = models.CharField(max_length=255)
    file = models.FileField()
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="images",
    )

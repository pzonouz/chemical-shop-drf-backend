from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        pass

    # class Meta:
    #     db_table = ""
    #     managed = True
    #     verbose_name = "User
    #     verbose_name_plural = "Users"

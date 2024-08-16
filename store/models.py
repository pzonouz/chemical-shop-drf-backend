from django.db import models


class Store(models.Model):
    aboutus = models.TextField(null=True, blank=True)
    supportNumber = models.CharField(max_length=25, null=True)
    telegram = models.CharField(max_length=128, null=True)
    whatsapp = models.CharField(max_length=128, null=True)
    address = models.TextField(null=True)
    phoneNumber = models.CharField(null=True)
    mobileNumber = models.CharField(max_length=25, null=True)

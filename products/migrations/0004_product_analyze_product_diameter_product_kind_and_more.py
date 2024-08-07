# Generated by Django 5.0.4 on 2024-08-01 07:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_is_customized_product_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="analyze",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="diameter",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="kind",
            field=models.CharField(default="", max_length=64),
        ),
        migrations.AddField(
            model_name="product",
            name="modified_by",
            field=models.CharField(default="", max_length=256),
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="state",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="unit",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="user",
            field=models.ForeignKey(
                blank=True,
                default=0,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
# Generated by Django 5.0.3 on 2024-04-03 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0004_delete_process'),
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('I', 'IN_PROGRESS'), ('R', 'READY'), ('D', 'DELIVERED')], max_length=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processes', to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

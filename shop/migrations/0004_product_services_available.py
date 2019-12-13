# Generated by Django 2.1.5 on 2019-08-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_service_conversion_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='services_available',
            field=models.ManyToManyField(blank=True, default='', related_name='services_for', to='shop.Service'),
        ),
    ]
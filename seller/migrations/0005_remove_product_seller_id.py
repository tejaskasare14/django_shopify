# Generated by Django 4.2.6 on 2024-07-13 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_rename_sid_product_seller_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller_id',
        ),
    ]

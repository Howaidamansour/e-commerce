# Generated by Django 4.0 on 2022-01-03 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_productname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='productname',
        ),
    ]
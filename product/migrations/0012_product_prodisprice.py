# Generated by Django 4.0 on 2021-12-29 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_rename_slug_product_proslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProDisPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='product Discound'),
            preserve_default=False,
        ),
    ]
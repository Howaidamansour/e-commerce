# Generated by Django 4.0 on 2021-12-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_probrand_product_procategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ProImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/%y/%m/%d'),
        ),
    ]

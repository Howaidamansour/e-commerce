# Generated by Django 4.0 on 2022-01-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productname',
            field=models.CharField(blank=True, max_length=66, null=True),
        ),
    ]
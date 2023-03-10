# Generated by Django 4.0 on 2021-12-30 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
        ('product', '0012_product_prodisprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProBrand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.brand', verbose_name='product Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Main Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProCreated',
            field=models.DateTimeField(verbose_name='product date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProDisPrice',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='product Discount'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ProImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/%y/%m/%d', verbose_name='product image'),
        ),
    ]

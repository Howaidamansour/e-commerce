# Generated by Django 4.0 on 2022-01-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_probrand_alter_product_procategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='CatParent',
        ),
        migrations.AlterField(
            model_name='category',
            name='CatImage',
            field=models.ImageField(blank=True, null=True, upload_to='category/%y/%m/%d', verbose_name='Image'),
        ),
    ]

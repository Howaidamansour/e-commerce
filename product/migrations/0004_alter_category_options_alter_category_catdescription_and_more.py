# Generated by Django 4.0 on 2021-12-23 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='CatDescription',
            field=models.TextField(verbose_name='Category description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CatImage',
            field=models.ImageField(upload_to='category/%y/%m/%d', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CatName',
            field=models.CharField(max_length=50, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='CatParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CatParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Category parent'),
        ),
        migrations.CreateModel(
            name='ProductAlternatev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.product')),
                ('ProAlternatev', models.ManyToManyField(related_name='Alternatev_product', to='product.Product')),
            ],
            options={
                'verbose_name': 'Product Alternatev',
                'verbose_name_plural': 'Product Alternatevs',
            },
        ),
    ]

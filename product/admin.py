from django.contrib import admin
from .models import Product, productImage, Category

admin.site.register(Product)
admin.site.register(productImage)
admin.site.register(Category)
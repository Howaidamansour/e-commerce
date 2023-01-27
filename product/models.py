from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):
    ProName = models.CharField(max_length=50, verbose_name=_('product name'))
    ProPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('product price'))
    ProDisPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('product Discount'))
    ProDescription = models.TextField(verbose_name=_('product description'))
    ProImage = models.ImageField(upload_to='product/%y/%m/%d', blank=True, null=True, verbose_name=_('product image'))
    ProColor = models.CharField(max_length=50, verbose_name=_('product Color'), blank=True, null=True)
    ProSize = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('product Size'), blank=True, null=True)
    ProCreated = models.DateTimeField(verbose_name=_("product date"))
    ProCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Main Category'))
    ProBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('product Brand'))
    ProSlug = models.SlugField(blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.ProSlug})

    def save(self, *args, **kwargs):
        if not self.ProSlug:
            self.ProSlug = slugify(self.ProName)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.ProName


class productImage(models.Model):
    ProIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'))
    ProductImage = models.ImageField(upload_to='product/%y/%m/%d', verbose_name=_('Image'))

    def __str__(self):
        return str(self.ProIProduct)


class Category(models.Model):
    CatName = models.CharField(max_length=50, verbose_name=_('Category Name'))

    CatDescription = models.TextField(verbose_name=_('Category description'))
    CatImage = models.ImageField(upload_to='category/%y/%m/%d', verbose_name=_('Image'), blank=True, null=True)

    def __str__(self):
        return self.CatName

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class ProductAlternatev(models.Model):
    PALproduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product')
    ProAlternatev = models.ManyToManyField(Product, related_name='Alternatev_product')

    class Meta:
        verbose_name = _('Product Alternatev')
        verbose_name_plural = _('Product Alternatevs')

    def __str__(self):
        return str(self.PALproduct)

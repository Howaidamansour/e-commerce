from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Brand(models.Model):
    BrandName = models.CharField(max_length=40)
    BrandDescription = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return str(self.BrandName)


class Varint(models.Model):
    VarintName = models.CharField(max_length=40)
    VarintDescription = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _('Varint')
        verbose_name_plural = _('Varints')

    def __str__(self):
        return str(self.VarintName)

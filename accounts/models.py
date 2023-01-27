import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import post_save
from product.models import Product


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("User"), on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(verbose_name=_("Image"), upload_to='profile/%y/%m/%d', blank=True, null=True)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    join_date = models.DateTimeField(verbose_name=_("Join date"), default=datetime.datetime.now)
    ebooks = models.ManyToManyField(Product, blank=True)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = ("Profiles")

    def __str__(self):
        return '%s' % (self.user)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs=
        {"slug": self.slug})


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)

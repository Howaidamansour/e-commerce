from django.db import models


# Create your models here.
class ContactUs(models.Model):
    email = models.EmailField(blank=False, null=False)
    message = models.TextField()

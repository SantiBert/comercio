from django.db import models
from django.db.models.fields import CharField
from django_countries.fields import CountryField
from django.utils import timezone
# Create your models here.


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    domicilio = models.CharField(max_length=250)
    city = models.CharField(max_length=250, null=True, blank=True)
    provorstate = models.CharField(max_length=250, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    zipcode = models.CharField(max_length=4, null=True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=250, null=True, blank=True)

from django.db import models


class Photo(models.Model):
    flat = models.ForeignKey(
        'flats.Flat', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=True, blank=True)
    file = models.FileField(null=True, blank=True)


class Flat(models.Model):
    available_from = models.DateField(null=True, blank=True)
    property = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.CharField(max_length=255)
    area = models.CharField(max_length=255, null=True, blank=True)
    room = models.CharField(max_length=255, null=True, blank=True)
    price_one = models.DecimalField(max_digits=6, decimal_places=2)
    price_two = models.DecimalField(max_digits=6, decimal_places=2)
    bills = models.CharField(max_length=255, null=True, blank=True)
    licensor = models.CharField(max_length=255, null=True, blank=True)
    n_b = models.IntegerField(default=0)
    deposit_rent = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    extra = models.CharField(max_length=255, null=True, blank=True)
    profile = models.CharField(max_length=255, null=True, blank=True)
    photos_url = models.URLField(max_length = 200, null=True, blank=True) 
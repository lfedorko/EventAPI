from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True) # concert, teatr
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    text = models.CharField(max_length=4000, blank=True, null=True) # description
    price = models.CharField(max_length=300, blank=True, null=True)
    w_from = models.TimeField(auto_now=False, auto_now_add=False)
    expire_date = models.CharField(max_length=10, blank=True, null=True)
    place = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        managed = True #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
        db_table = 'events'
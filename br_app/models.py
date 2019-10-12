from django.db import models

# Create your models here.

class Officers(models.Model):
    badge = models.IntegerField(blank=True, null=True)
    first = models.CharField(max_length=64, blank=True, null=True)
    last = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    profileid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'officers'

from django.db import models

# Create your models here.

class Officer(models.Model):
    officer_id = models.IntegerField()
    name = models.CharField(max_length=30)

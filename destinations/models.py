
# Create your models here.
from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

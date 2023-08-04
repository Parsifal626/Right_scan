from django.db import models

# Create your models here.
class Bird(models.Model):
    name = models.CharField(max_length=100)
    feather_color = models.CharField(max_length=100)
from django.db import models

# Create your models here.

class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=200)

# class Feature:
#     id: int
#     name: str
#     details: str
#     is_true: bool

from django.db import models

# Create your models here.
class User(models.Model):
    First=models.CharField(max_length=10,unique=false)

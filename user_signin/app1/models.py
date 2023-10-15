

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)

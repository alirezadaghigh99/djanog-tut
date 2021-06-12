from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True, null=False)
    name      = models.CharField(max_length=30, unique=False, null=False)
    password  = models.CharField(max_length=100, null=False)
    email     = models.CharField(max_length=50)


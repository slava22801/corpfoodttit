from django.db import models

class users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

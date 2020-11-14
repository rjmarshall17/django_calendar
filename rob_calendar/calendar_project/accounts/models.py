from django.db import models
from django.utils.timezone import now

# Create your models here.


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(default=now())


from django.db import models
from django.utils.timezone import now


class Account(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100,default="temppass")
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(default=now())

    def __str__(self):
        return self.email

    def set_password(self,password):
        self.password = password

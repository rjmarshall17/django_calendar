from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from accounts import models as accounts_models
# Create your models here.


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500,null=True)
    start_time = models.DateTimeField(default=now())
    end_time = models.DateTimeField(default=now())
    location = models.CharField(max_length=200)
    account = models.ForeignKey(accounts_models.Account,on_delete=models.CASCADE,default=0)

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('appointment_edit',args=(self.id,))
        return f'<p>{self.title}</p><a href="{url}">edit</a>'



from rest_framework import serializers
from . import models
# Create your views here.


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ['id', 'first_name', 'last_name','email', 'date_created']


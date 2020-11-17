from rest_framework import serializers
from ..models import Account
# Create your views here.


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name','email', 'password', 'date_created']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only':True},
        }

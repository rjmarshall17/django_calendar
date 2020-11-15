from rest_framework import serializers
from ..models import Account
# Create your views here.


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name','email', 'password', 'date_created']


class RegistrationSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password', 'password_confirmation']
        extra_kwargs = {
            'password': {'write_only':True},
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirm']

        if password != password_confirmation:
            raise serializers.ValidationError({'password':'Passwords do not match'})
        account.set_password(password)
        account.save()
        return account

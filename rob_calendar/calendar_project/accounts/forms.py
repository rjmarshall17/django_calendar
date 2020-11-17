from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

from .models import Account


class AccountForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password', 'password_confirm')

    def save(self):
        print("\n************ RJM: In the account form save function\n")
        print("\n************\n%s\n***********\n" % (self.cleaned_data))
        account = Account(
            email=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
        )
        password = self.cleaned_data.get('password')
        account.set_password(make_password(password))
        account.save()
        return account

    def clean_password(self):
        print('\n**************\n%s\n%s\n**************' % (dir(self),self.cleaned_data))
        password = self.cleaned_data['password']
        password_confirmation = self.data.get('password_confirm')

        try:
            password_validation.validate_password(self.cleaned_data['password'])
        except ValidationError as err:
            raise forms.ValidationError(err.messages[0])
        if password != password_confirmation:
            raise forms.ValidationError({'password':'Passwords do not match'})
        return password

    # error_messages = {
    #     'password_mismatch': 'The two password fields did not match.',
    # }
    #
    # password1 = forms.CharField(
    #     label= "Password",
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     help_text=password_validation.password_validators_help_text_html(),
    # )
    #
    # password2 = forms.CharField(
    #     label= "Password confirmation",
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    #     help_text= "Enter the same password as before, for verification.",
    # )

    # def clean_password2(self):
    #     # password1 = self.cleaned_data.get("password1")
    #     password1 = self.get_password1()
    #     # password2 = self.cleaned_data.get("password2")
    #     password2 = self.get_password2()
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )
    #     return password2
    #
    # def _post_clean(self):
    #     super()._post_clean()
    #     # Validate the password after self.instance is updated with form data
    #     # by super().
    #     password = self.get_password2()
    #     try:
    #         password_validation.validate_password(password, self.instance)
    #     except ValidationError as error:
    #         self.add_error('password2', error)

    # def save(self, commit=True):
    #     print("RJM - In the save function")
    #     account = super().save(commit=False)
    #     print("self=%s" % self)
    #     # account.set_password(self.cleaned_data["password1"])
    #     # account.set_password(self.get_password1())
    #     if commit:
    #         account.save()
    #     return account

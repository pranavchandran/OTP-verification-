from django import forms
from passwords.fields import PasswordField
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from passwords.fields import PasswordField

from django.contrib.auth.models import User

class loginform(UserCreationForm):
    Email = forms.EmailField()
    Phone = PhoneNumberField()
    class Meta:

        model = User
        fields = ['username', 'Email', 'Phone', 'password1', 'password2']








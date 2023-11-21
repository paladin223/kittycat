from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

import users.models


class Authentication(AuthenticationForm):
    class Meta:
        order_fields = ["name", "email", "password"]
        model = users.models.User
        fields = ["name", "email", "password"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "login-input"}),
            "password": forms.PasswordInput(
                attrs={"class": "input-add-login"}
            ),
        }


class Register(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = users.models.User
        fields = ["name", "email", "password1", "password2"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

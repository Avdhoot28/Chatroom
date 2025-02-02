from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    language = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'language', 'password1', 'password2']
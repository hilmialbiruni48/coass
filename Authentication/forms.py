from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django import forms
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        # fields = ['username', 'first_name', 'last_name',
        #           'email', 'password1', 'password2']
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

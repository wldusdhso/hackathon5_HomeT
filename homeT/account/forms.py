from django.contrib.auth.models import User
from .models import User
from django import forms

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
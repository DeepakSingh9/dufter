from django import forms
from .models import UserLogin

class LoginForm(forms.ModelForm):
    username=forms.CharField(max_length=128)
    password=forms.CharField(max_length=128)

    class Meta:
        model=UserLogin
        fields=('username','password',)
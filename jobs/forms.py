from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.html import strip_tags
from .models import Profile,Job_Application


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=('username','password','first_name','last_name','email',)





class UserProfileForm(forms.ModelForm):


    class Meta:
        model=Profile
        fields=('date_of_birth','keyskills','photo','experience',)



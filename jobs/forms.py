from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.utils.html import strip_tags
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model=User
        fields=('username','email','first_name',)

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords dont match')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email',)

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('keyskills','experience',)





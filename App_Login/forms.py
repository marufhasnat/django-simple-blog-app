from dataclasses import fields

from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from pyexpat import model

from App_Login.models import UserProfile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address', required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        
        
class ProfilePic(forms.ModelForm):
    profile_pic = forms.ImageField(label='Profile Pciture')
    class Meta:
        model = UserProfile
        fields = ['profile_pic', ]
        
        
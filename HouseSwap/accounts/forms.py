from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email',]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
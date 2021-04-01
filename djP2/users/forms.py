from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileRegisterForm(forms.ModelForm):
    carrera = forms.ChoiceField(choices=(('Math','Math'),('Physics','Physics')))
    gender = forms.CharField(strip=True)

    class Meta:
        model = Profile
        fields = ['carrera', 'gender']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    carrera = forms.ChoiceField(choices=(('1','Math'),('2','Physics')))
    gender = forms.CharField(strip=True)

    class Meta:
        model = Profile
        fields = ['carrera', 'gender']

from django import forms
from .models import Register
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password','password1']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['phone_no','age','id_proof','gender','class1']

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ['username','password']
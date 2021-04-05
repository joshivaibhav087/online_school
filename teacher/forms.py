from django import forms
from .models import Admin
from django.contrib.auth.models import User

class AddForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['class1','subject','chapter','video','notes']
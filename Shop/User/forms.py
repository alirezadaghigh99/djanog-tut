from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.widgets import Widget
from .models import User
class Login_Form(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'password']

class Register_Form(forms.Form):
    user_name = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
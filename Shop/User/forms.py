from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.widgets import Widget
from django.core.exceptions import ValidationError
from .models import User as User
class Login_Form(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    def clean(self):
        data = super().clean()
        user_name = data["user_name"]
        password = data["password"]

        try:
            user = User.objects.get(user_name = user_name)
            if user.password != password:
                raise ValidationError("this user name and password does not match")
            else:
                return data

        except User.DoesNotExist:
            raise ValidationError("this user does not exists")

class Register_Form(forms.Form):
    user_name = forms.CharField(max_length=100)
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    def clean(self) :
        print("clean in register ")
        cleaned_data =  super().clean()
        pass1 = cleaned_data["password1"]
        pass2 = cleaned_data['password2']
        if pass1 != pass2:
            raise ValidationError("Your entered password didn't match")
        return cleaned_data

    def clean_user_name(self):
        user_name = self.cleaned_data["user_name"]
        
        
        try:
            User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            return user_name
        raise ValidationError("this user name has already exists")
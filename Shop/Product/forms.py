from django import forms
from django.db.models import fields
from .models import *
  
class ProductForm(forms.ModelForm  ):
    class Meta:
        model = Product
        fields = ['name', 'price', 'photo']
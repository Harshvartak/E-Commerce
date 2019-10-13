
from django import forms
from .models import Product


class ProductCreate(forms.Form):
    title=forms.CharField()
    description=forms.CharField(widget=forms.Textarea)
    image=forms.ImageField()
    cost=forms.DecimalField()

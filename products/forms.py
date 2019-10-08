
from django import forms
from .models import Product


class ProductCreate(forms.Form):
    title=forms.CharField()
    description=forms.TextField()
    image=forms.ImageField()
    cost=forms.DecimalField()

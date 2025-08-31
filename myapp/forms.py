# "C:\Users\ryota\myproject\myapp\forms.py"

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']
        # categoryフィールドをラジオボタンウィジェットで表示
        widgets = {
            'category': forms.RadioSelect(),
        }
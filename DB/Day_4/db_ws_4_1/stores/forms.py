from django import forms
from .models import Store, Product

class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'amount', 'price', 'adult',)

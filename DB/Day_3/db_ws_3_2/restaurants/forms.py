from .models import Restaurant, Menu
from django import forms

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        widgets = {
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'})
        }


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('name', 'price', 'is_vegan',)
        
class MenuUpdateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('price', 'is_vegan',)

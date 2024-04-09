from .models import Author
from django import forms

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nickname',)
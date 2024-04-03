from .models import Author, Book
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('author',)
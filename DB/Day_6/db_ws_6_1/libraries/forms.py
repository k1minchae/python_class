from .models import Author, Book
from django import forms

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('nickname',)

class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'